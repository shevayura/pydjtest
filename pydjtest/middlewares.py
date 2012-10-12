from pydjtest.models import Request

class RequestLog():
    
    def process_template_response(self, request, response):
        r = Request()
        r.url    = request.path
        r.method = request.method
        r.code   = response.status_code

        r.save()

        return response