import numpy as np
import matplotlib.pyplot as plt

class StepFunction:
    def __init__(self, breakpoints, values, check_valid=True):
        if check_valid:
            if len(breakpoints) != len(values) + 1:
                raise ValueError("breakpoints 길이는 values 길이+1 이어야 합니다.")
            if not np.all(np.diff(breakpoints) > 0):
                raise ValueError("breakpoints는 엄격히 증가하는 순서여야 합니다.")
        
        self.breakpoints = breakpoints
        self.values = values

    @classmethod
    def from_constant(cls, start, end, value):
        return cls(np.array([start, end], dtype=float), np.array([value], dtype=float))
    
    def copy(self):
        return StepFunction(self.breakpoints.copy(), self.values.copy(), check_valid=False)

    def domain(self):
        return self.breakpoints[0], self.breakpoints[-1]
    
    def evaluate(self, x):
        idx = np.searchsorted(self.breakpoints, x, side='right') - 1
        idx = np.clip(idx, 0, len(self.values)-1)
        return self.values[idx]

    def smooth(self, dt):
        start, end = self.domain()
        n_steps = int(np.ceil((end - start) / dt))
        new_breakpoints = start + np.arange(n_steps+1)*dt
        new_breakpoints[-1] = end
        
        sample_points = new_breakpoints[:-1]
        new_values = self.evaluate(sample_points)
        
        return StepFunction(new_breakpoints, new_values, check_valid=False)

    def align(self, other):
        new_breakpoints = np.unique(np.concatenate([self.breakpoints, other.breakpoints]))
        val_self = self._resample(new_breakpoints)
        val_other = other._resample(new_breakpoints)
        return new_breakpoints, val_self, val_other

    def _resample(self, new_breakpoints):
        sample_points = new_breakpoints[:-1]
        return self.evaluate(sample_points)

    def __add__(self, other):
        if isinstance(other, StepFunction):
            new_bk, val_a, val_b = self.align(other)
            return StepFunction(new_bk, val_a + val_b, check_valid=False)
        else:
            return StepFunction(self.breakpoints, self.values + other, check_valid=False)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, StepFunction):
            new_bk, val_a, val_b = self.align(other)
            return StepFunction(new_bk, val_a * val_b, check_valid=False)
        else:
            return StepFunction(self.breakpoints, self.values * other, check_valid=False)

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def average(step_functions, dt=None):
        if len(step_functions) == 0:
            raise ValueError("빈 리스트입니다.")
        
        if dt is not None:
            start = min(sf.breakpoints[0] for sf in step_functions)
            end = max(sf.breakpoints[-1] for sf in step_functions)
            n_steps = int(np.ceil((end - start) / dt))
            new_breakpoints = start + np.arange(n_steps+1)*dt
            new_breakpoints[-1] = end
            
            vals = []
            for sf in step_functions:
                val = sf._resample(new_breakpoints)
                vals.append(val)
            vals = np.array(vals)
            mean_vals = np.mean(vals, axis=0)
            return StepFunction(new_breakpoints, mean_vals, check_valid=False)
        else:
            all_bk = np.unique(np.concatenate([sf.breakpoints for sf in step_functions]))
            vals = []
            for sf in step_functions:
                val = sf._resample(all_bk)
                vals.append(val)
            vals = np.array(vals)
            mean_vals = np.mean(vals, axis=0)
            return StepFunction(all_bk, mean_vals, check_valid=False)

    def plot(self, ax=None, **kwargs):
        """
        dt가 주어지면 dt 간격으로 smoothing한 뒤, step plot을 그린다.
        dt가 None이면 현재 breakpoints/values 그대로 step plot을 그린다.
        """
        
        x = self.breakpoints
        y = np.append(self.values, self.values[-1])  # 마지막 구간까지 값 유지
        
        if ax is None:
            fig, ax = plt.subplots()

        # where='post' 옵션을 사용하여 step 형태로 그린다.
        ax.step(x, y, where='post', **kwargs)
        return ax
    
    @staticmethod
    def plot_multiple(step_functions, labels=None, ax=None, **kwargs):

        if len(step_functions) == 0:
            raise ValueError("빈 리스트입니다.")
        
        if labels is not None and len(labels) != len(step_functions):
            raise ValueError("labels의 길이는 step_functions의 길이와 같아야 합니다.")

        if ax is None:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()

        for i, sf in enumerate(step_functions):
            x = sf.breakpoints
            y = np.append(sf.values, sf.values[-1])
            lbl = labels[i] if labels is not None else None
            ax.step(x, y, where='post', label=lbl, **kwargs)

        if labels is not None:
            ax.legend()

        return ax


# 사용 예시
if __name__ == "__main__":
    sf1 = StepFunction(np.array([0, 1, 2, 3]), np.array([2, 3, 1]))
    sf2 = StepFunction(np.array([0, 1, 3]), np.array([5, 10]))

    sf_sum = sf1 + sf2
    sf_mul = sf1 * sf2
    ax = StepFunction.plot_multiple([sf1, sf2, sf_sum, sf_mul], ["f1", "f2", "f1+f2", "f1*f2"])
    plt.legend()
    plt.show()