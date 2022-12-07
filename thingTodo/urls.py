from django.urls import path 
from . import views 


app_name = "thingTodo"
urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("edit_topic/<int:topic_id>/", views.edit_topic, name="edit_topic"),
]