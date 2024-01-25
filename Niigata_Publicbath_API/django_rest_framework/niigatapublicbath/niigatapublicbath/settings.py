INSTALLED_APPS = [
    'publicbath.apps.PublicbathConfig',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ORIGIN_WHITELIST = [
    #設定したURL
]
