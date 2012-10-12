
def request_to_context(request):
    return { 
        'request': request,
        'testvar': "hello!",
        }