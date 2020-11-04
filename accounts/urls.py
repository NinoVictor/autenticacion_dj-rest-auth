from django.urls import path, include
from accounts import views
from rest_framework import routers
from rest_framework.authtoken import views as restViews
router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

app_name = 'accounts'

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', restViews.obtain_auth_token)
]
