from django.urls import path
from . import views
from .views import ToDoViewsets
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as v

router = DefaultRouter()
router.register(r'todo_viewsets', ToDoViewsets, basename='todo')
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('todo_class/', views.TodoClass.as_view()),
    path('token/', v.obtain_auth_token),
]
urlpatterns += router.urls
