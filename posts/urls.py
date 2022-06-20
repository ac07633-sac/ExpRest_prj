from django.urls import path, include
from . import views

urlpatterns = [
    path('help/', views.help, name='help'),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostRetrieveDestroy.as_view()),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    
]