class ServerDatabase(object):
    def request_server_name():
        pass

    def retire_server_name():
        pass

class RateLimiter()
    def process(self, request):
        sig = self._get_signature(request)
        self.assert_within_limits(sig)
        self.increment_request_counters(sig)

    def _get_signature(self, request):
        return request.username

    def assert_within_limits():
        self.table[]