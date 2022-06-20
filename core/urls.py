from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from . import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('secure/', views.HelloSecureView.as_view(), name='hellosecure'),
    path('listusers/', views.ListUsers.as_view(), name='listusers'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('get/', views.hello_world, name='hello_world'),
    path('both/', views.hello_world_both, name='hello_world_both'),

]

