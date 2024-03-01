from core.services import ProxyService
from django.conf import settings


class AuthService(ProxyService):
    _host = settings.MICROSERVICE_AUTH_HOST
    _port = settings.MICROSERVICE_AUTH_PORT


class TeamService(ProxyService):
    _host = settings.MICROSERVICE_TEAMS_HOST
    _port = settings.MICROSERVICE_TEAMS_PORT


class UserService(ProxyService):
    _host = settings.MICROSERVICE_USERS_HOST
    _port = settings.MICROSERVICE_USERS_PORT


class ConversationService(ProxyService):
    _host = settings.MICROSERVICE_CONVERSATIONS_HOST
    _port = settings.MICROSERVICE_CONVERSATIONS_PORT
