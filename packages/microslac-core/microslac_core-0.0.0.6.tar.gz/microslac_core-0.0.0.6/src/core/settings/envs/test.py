from core.settings import env

DEBUG = True

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

# Database
REPLICATION_DB_ALIAS = "replication"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_TEST_NAME"),
        "USER": env("DB_TEST_USER"),
        "PASSWORD": env("DB_TEST_PASSWORD"),
        "HOST": env("DB_TEST_HOST"),
        "PORT": env("DB_TEST_PORT"),
    },
    REPLICATION_DB_ALIAS: {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_TEST_NAME"),
        "USER": env("DB_TEST_USER"),
        "PASSWORD": env("DB_TEST_PASSWORD"),
        "HOST": env("DB_TEST_HOST"),
        "PORT": env("DB_TEST_PORT"),
        "TEST": {
            "MIRROR": "default",
        },
    },
}

# Logging
LOGGING = {}
