import re
from types import SimpleNamespace
from core.settings import env

MICROSERVICE = SimpleNamespace(
    ADMIN_HOST=env.str("MICROSERVICE_ADMIN_HOST", default="admin"),
    ADMIN_PORT=env.int("MICROSERVICE_ADMIN_HOST", default=8010),

    AUTH_HOST=env.str("MICROSERVICE_AUTH_HOST", default="auth"),
    AUTH_PORT=env.int("MICROSERVICE_AUTH_HOST", default=8011),

    TEAMS_HOST=env.str("MICROSERVICE_TEAMS_HOST", default="teams"),
    TEAMS_PORT=env.int("MICROSERVICE_TEAMS_HOST", default=8012),

    USERS_HOST=env.str("MICROSERVICE_USERS_HOST", default="users"),
    USERS_PORT=env.int("MICROSERVICE_USERS_HOST", default=8013),
)

MICROSERVICE_BASE_HOST = env.str("MICROSERVICE_BASE_HOST", default="")  # localhost
if MICROSERVICE_BASE_HOST:
    hosts = [host for host in vars(MICROSERVICE) if re.match(r".*_HOST$", host)]
    for host in hosts:
        setattr(MICROSERVICE, host, MICROSERVICE_BASE_HOST)
