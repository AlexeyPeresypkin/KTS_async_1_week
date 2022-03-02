from aiohttp import web


def get_data(request: web.Request):
    data = {
        'method': request.method,
        'host': request.host,
        'path': request.path,
        "query_string": request.query_string,
        "query": request.query_string,
        "scheme": request.scheme,
        "secure": request.secure,
        "http_version": request.version,
        "headers": {
            "Host": request.host,
            "Accept": request.version,
            "User-Agent": request.headers['User-Agent'],
            "Accept-Language": request.headers['Accept-Language'],
            "Accept-Encoding": request.headers['Accept-Encoding'],
            "Connection": request.headers["Connection"]
        },
        "cookies": request.cookies['csrftoken'],
        "json": request.json().cr_await,
    }
    return data



