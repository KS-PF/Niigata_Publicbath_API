INSTALLED_APPS = [
    'publicbath.apps.PublicbathConfig',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

# CORS_ORIGIN_WHITELIST = [
#     'アクセスを制限したい場合はこちらに記述',
# ]
CORS_ALLOW_ALL_ORIGINS = True
