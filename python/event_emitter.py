from collections import defaultdict


class EventEmitter(object):

    def __init__(self):
        self._listeners = defaultdict(list)

    def on(self, event, listener):
        self._listeners[event].append(listener)
        return self

    def once(self, event, listener):
        def once_listener_wrapper(*args, **kwargs):
            self.remove_listener(event, once_listener_wrapper)
            listener(*args, **kwargs)
        self.on(event, once_listener_wrapper)
        return self

    def remove_listener(self, event, listener):
        self._listeners[event].remove(listener)
        return self

    def remove_all_listeners(self, event=None, each=False):
        if each:
            self._listeners = defaultdict(list)
        else:
            del self._listeners[event]
        return self

    def listeners(self, event):
        return self._listeners[event]

    def emit(self, event, *args, **kwargs):
        l_count = len(self._listeners[event])
        for l_item in self._listeners[event]:
            l_item(*args, **kwargs)
        return l_count
