import environ

from pathlib import Path
from split_settings.tools import optional, include

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

APP_ENVIRONMENT = env.str("APP_ENVIRONMENT", default="prod")

_base_settings = (
    "configs/[!_]*.py",
    f"envs/{APP_ENVIRONMENT}.py",
    optional("optional.py"),
)

include(*_base_settings)
