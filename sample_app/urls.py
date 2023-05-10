from rest_framework.routers import DefaultRouter
from django.urls import path, include
from sample_app import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('chatgpt/', views.chat, name='chatgpt-create'),
]
