# from scrapy_proxy_pool.policy import BanDetectionPolicy

# class CustomBanDetectionPolicy(BanDetectionPolicy):
#     def response_is_ban(self, request, response):
#         return super().response_is_ban(request, response) or "captcha" in response.text.lower()

#     def exception_is_ban(self, request, exception):
#         return None
