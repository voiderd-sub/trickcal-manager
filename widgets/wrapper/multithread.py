from PySide6.QtCore import QObject, Signal, QRunnable, Slot


# Worker class for multithreading
class WorkerSignals(QObject):
    finished = Signal()
    result = Signal(object)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            print(e)          
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()