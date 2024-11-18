# Chain of Responsibility Pattern
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor:
            return self._successor.handle_request(request)
        return None

class AuthHandler(Handler):
    def handle_request(self, request):
        if request.get("user") == "admin":
            return "User authenticated"
        return super().handle_request(request)

class LoggingHandler(Handler):
    def handle_request(self, request):
        print(f"Logging request: {request}")
        return super().handle_request(request)

class DataHandler(Handler):
    def handle_request(self, request):
        if "data" in request:
            return f"Data processed: {request['data']}"
        return super().handle_request(request)

# Usage
chain = AuthHandler(LoggingHandler(DataHandler()))
request = {"user": "admin", "data": "Important data"}
print(chain.handle_request(request))
