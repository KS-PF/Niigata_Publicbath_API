INSTALLED_APPS = [
    'publicbath.apps.PublicbathConfig',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5500'
]
