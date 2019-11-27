_handlers = {}
class EventManager:

	def add_handler(event, handler):
		if handler not in _handlers:
			_handlers.setdefault(event, [])
			_handlers[event] = [handler]
			#print(_handlers)

	def emit(event):
		for handler in _handlers[event]:
			handler()