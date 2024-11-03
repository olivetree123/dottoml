import json

from dottoml import (
    load_env,
    EnvObject,
    TomlEnvError,
)


def test_load():
    env = load_env()

    DATABASES = {
        'default': {
            'ENGINE': env.get_str("DB_ENGINE"),
            'NAME': env.get_str("DB_NAME"),
            "USER": env.get_str("DB_USER"),
            "PASSWORD": env.get_str("DB_PASSWORD"),
            "HOST": env.get_str("DB_HOST"),
            "PORT": env.get_int("DB_PORT"),
            "HAHA": env.get_str("HAHA", default=None, nullable=True),
        }
    }

    print(json.dumps(DATABASES, indent=4))