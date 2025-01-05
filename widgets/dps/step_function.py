from widgets.dps.enums import *

import numpy as np


class StepFunction:
    def __init__(self, points_values):
        """
        points_values: [(point, value), (point, value), ...]
        breakpoints와 values는 각각 동일 길이이며,
        마지막 구간은 +∞까지 이어진다고 가정.
        """
        if len(points_values) == 0:
            raise ValueError("빈 리스트입니다.")
        
        self.breakpoints = np.array([pv[0] for pv in points_values], dtype=float)
        self.values = np.array([pv[1] for pv in points_values], dtype=float)
        
        if len(self.breakpoints) != len(self.values):
            raise ValueError("point와 value의 개수는 동일해야 합니다.")
        
        if not np.all(np.diff(self.breakpoints) > 0):
            raise ValueError("point들은 엄격히 증가해야 합니다.")

    @classmethod
    def from_constant(cls, start, value):
        """
        [start, +∞)에서 value인 상수 StepFunction 생성
        """
        return cls([(start, value)])
    
    def copy(self):
        points_values = list(zip(self.breakpoints.copy(), self.values.copy()))
        return StepFunction(points_values)

    def evaluate(self, x):
        """
        x < breakpoints[0] => values[0]
        breakpoints[i] <= x < breakpoints[i+1] => values[i]
        x >= breakpoints[-1] => values[-1]
        """
        idx = np.searchsorted(self.breakpoints, x, side='right') - 1
        idx = np.clip(idx, 0, len(self.values) - 1)
        return self.values[idx]

    def smooth(self, start, end, dt=DELTA_T, return_stepfn = False):
        if dt <= 0:
            raise ValueError("dt > 0 이어야 합니다.")
        if end <= start:
            raise ValueError("end > start 이어야 합니다.")

        new_breakpoints = np.arange(start, end + dt*1e-3, dt, dtype=float)
        if len(new_breakpoints) == 0 or new_breakpoints[-1] < end:
            new_breakpoints = np.append(new_breakpoints, end)

        new_values = self.evaluate(new_breakpoints)
        
        if return_stepfn:
            points_values = list(zip(new_breakpoints, new_values))
            return StepFunction(points_values)
        else:
            return new_breakpoints, new_values

    def _resample(self, new_breakpoints):
        return self.evaluate(new_breakpoints)

    def align(self, other):
        new_breakpoints = np.unique(np.concatenate([self.breakpoints, other.breakpoints]))
        val_self = self._resample(new_breakpoints)
        val_other = other._resample(new_breakpoints)
        return new_breakpoints, val_self, val_other

    def __add__(self, other):
        if isinstance(other, StepFunction):
            new_bk, val_a, val_b = self.align(other)
            new_vals = val_a + val_b
            points_values = list(zip(new_bk, new_vals))
            return StepFunction(points_values)
        else:
            new_vals = self.values + other
            points_values = list(zip(self.breakpoints, new_vals))
            return StepFunction(points_values)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, StepFunction):
            new_bk, val_a, val_b = self.align(other)
            new_vals = val_a * val_b
            points_values = list(zip(new_bk, new_vals))
            return StepFunction(points_values)
        else:
            new_vals = self.values * other
            points_values = list(zip(self.breakpoints, new_vals))
            return StepFunction(points_values)

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def average(step_functions, start, end, dt):
        if len(step_functions) == 0:
            raise ValueError("빈 리스트입니다.")
        if end <= start:
            raise ValueError("end는 start보다 커야 합니다.")
        if dt <= 0:
            raise ValueError("dt는 양의 실수여야 합니다.")
        
        n_steps = int(np.ceil((end - start) / dt))
        new_breakpoints = start + np.arange(n_steps + 1) * dt
        new_breakpoints[-1] = end

        vals_list = []
        for sf in step_functions:
            vals_list.append(sf.evaluate(new_breakpoints))
        vals_list = np.array(vals_list)  # shape=(N_sf, len(new_breakpoints))

        mean_vals = np.mean(vals_list, axis=0)
        points_values = list(zip(new_breakpoints, mean_vals))
        return StepFunction(points_values)
    
    def restrict_domain(self, a, b):
        if a > b:
            raise ValueError("a는 b 이하이어야 합니다.")

        in_range = self.breakpoints[(self.breakpoints >= a) & (self.breakpoints <= b)]
        candidate_bk = np.concatenate([in_range, [a, b]])
        new_breakpoints = np.unique(candidate_bk)
        new_breakpoints.sort()

        new_values = self.evaluate(new_breakpoints)
        points_values = list(zip(new_breakpoints, new_values))
        return StepFunction(points_values)