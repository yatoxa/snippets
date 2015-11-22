
class EventEmitter(object):

    def __init__(self):
        self._listeners = {}

    def on(self, event, listener):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(listener)
        return self

    def once(self, event, listener):
        def once_listener_wrapper(*args, **kwargs):
            self.remove_listener(event, once_listener_wrapper)
            listener(*args, **kwargs)
        self.on(event, once_listener_wrapper)
        return self

    def remove_listener(self, event, listener):
        try:
            self._listeners[event].remove(listener)
        except KeyError or ValueError:
            pass
        return self

    def remove_all_listeners(self, event=None):
        if event is None:
            self._listeners = {}
        else:
            try:
                del self._listeners[event]
            except KeyError:
                pass
        return self

    def listeners(self, event):
        try:
            return self._listeners[event]
        except KeyError:
            return {}

    def emit(self, event, *args, **kwargs):
        try:
            l_count = len(self._listeners[event])
        except KeyError:
            return False
        for l_item in self._listeners[event]:
            l_item(*args, **kwargs)
        return l_count
