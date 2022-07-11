from xml.etree.ElementInclude import include
from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('todo/completed', views.ListCompletedTodoItems)

urlpatterns = [
    path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoUpdate.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
]
