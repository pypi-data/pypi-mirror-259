from fake_useragent import UserAgent


class UAMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random