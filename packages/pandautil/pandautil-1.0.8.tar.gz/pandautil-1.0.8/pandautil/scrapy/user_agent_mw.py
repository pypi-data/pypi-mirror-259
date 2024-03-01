from fake_useragent import UserAgent


class UserAgentRandomMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random

class UserAgentChromeRandomMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent(browsers=['chrome'])
        request.headers['User-Agent'] = ua.random

class UserAgentHighMiddleware:
    def process_request(self, request, spider):
        ua =UserAgent(min_percentage=3.0)
        request.headers['User-Agent'] = ua.random