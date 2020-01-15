from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator,OriginValidator

from chat import consumers



application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("chat/<username>",consumers.ChatConsumer),
            ])
        ),
    ),

})