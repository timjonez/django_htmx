def htmx_middleware(get_response):

    def middleware(request):
        request.is_htmx = request.headers.get('HX-Request') == 'true'

        response = get_response(request)
        response.is_htmx = request.is_htmx

        return response

    return middleware
