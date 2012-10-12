import settings

def request_to_context(request):
    return {
        'settings': settings,
        'request' : request,
        'testvar' : "hello!",
        }