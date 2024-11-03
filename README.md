# dottoml
Environment in TOML format.

### Install
```shell
pip install dottoml
```

### Usage
`.env.toml` 
```toml
[production]
DEBUG = false
DB_ENGINE = "django.db.backends.postgresql"
DB_NAME = "ragx"
DB_USER = "postgres"
DB_PASSWORD = "1q2w3e"
DB_HOST = "127.0.0.1"
DB_PORT = 5432


[development]
DEBUG = true
DB_ENGINE = "django.db.backends.mysql"
DB_NAME = "ragx"
DB_USER = "postgres"
DB_PASSWORD = "1q2w3e"
DB_HOST = "127.0.0.1"
DB_PORT = 5432


[test]
DEBUG = true
DB_ENGINE = "django.db.backends.mysql"
DB_NAME = "ragx"
DB_USER = "postgres"
DB_PASSWORD = "1q2w3e"
DB_HOST = "127.0.0.1"
DB_PORT = 5432
```

your python code:
```python
from toml_env import load_env

env = load_env(".env.toml")

project = env.get("PROJECT")
db_name = env.get_str("DB_NAME")
db_user = env.get_str("DB_USER", "root")
db_pass = env.get_str("DB_PASS", "password")
db_host = env.get_str("DB_HOST", "localhost")
db_port = env.get_int("DB_PORT", 3306)

debug = env.get_bool("DEBUG", False)
sentry_dsn = env.get_str("SENTRY_DSN", None, nullable=True)

print(debug, db_name, db_user, db_pass, db_host, db_port, sentry_dsn)
```

### Methods
#### `get` method
- `get(key: str, default=None, nullable=False) -> Any`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_str` method
- `get_str(key: str, default=None, nullable=False) -> str`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_int` method
- `get_int(key: str, default=None, nullable=False) -> int`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_float` method
- `get_float(key: str, default=None, nullable=False) -> float`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_bool` method
- `get_bool(key: str, default=None, nullable=False) -> bool`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;