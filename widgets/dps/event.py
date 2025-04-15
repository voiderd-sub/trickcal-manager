class Event:
    def __init__(self, time, event_type, process_fn, cancellable=True):
        """
        :param time: time to start event
        :param event_type: 'effect' or 'status'
        :param process_fn: function to execute when this event applies
        :param cancellable: ??
        """
        self.time = time
        self.event_type = event_type
        self.process_fn = process_fn
        self.cancellable = cancellable

    def process(self):
        self.process_fn()

    def __lt__(self, other):
        return self.time < other.time
