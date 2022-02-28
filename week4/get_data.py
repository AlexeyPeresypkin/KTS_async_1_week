from aiohttp import web


def get_data(request: web.Request):
    data = {
        'method': request.method,
        'host': request.host,
        'path': request.path,
        "query_string": request.query_string,
        "query": request.secure,
        "scheme": request.scheme,
        "secure": request.secure,
        "http_version": request.version,
        "headers": {
            "Host": request.headers['User-Agent'],
            "Accept": request.version,
            "User-Agent": request.scheme,
            "Accept-Language": request.headers['Host'],
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        },
        "cookies": 'request.cookies',
        "json": 'json'
    }
    return data



