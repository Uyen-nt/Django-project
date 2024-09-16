from django.urls import get_resolver

# Lấy tất cả các URL patterns từ dự án
resolver = get_resolver()
for pattern in resolver.url_patterns:
    print(pattern)
