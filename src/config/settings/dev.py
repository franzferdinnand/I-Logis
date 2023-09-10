from config.settings.base import *  # NOQA

DEBUG = True

SECRET_KEY = "django-insecure-!zi6yb5w0%s_hx()f^3@-%$w!p9-+5!gr03&an*i(x(niu8lwr"

ALLOWED_HOSTS = []

STATIC_URL = "static/"


from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = []

# mongoengine.connect(host="mongodb://admin:admin@mongodb:27017/mongodb_content?authSource=admin")

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default_local": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "ecargo",
            "USER": "postgres",
            "PASSWORD": "admin",
            "HOST": "localhost",
            "PORT": 5432,
        },
        "default_sqllite": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT"),
        },
    }

# "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": os.environ.get("POSTGRES_DB"),
#             "USER": os.environ.get("POSTGRES_USER"),
#             "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
#             "HOST": os.environ.get("POSTGRES_HOST"),
#             "PORT": os.environ.get("POSTGRES_PORT"),

# "default": {
#     "ENGINE": "django.db.backends.postgresql",
#     "NAME": "ecargo",
#     "USER": "postgres",
#     "PASSWORD": "admin",
#     "HOST": "localhost",
#     "PORT": 5432,
