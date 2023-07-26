from django.urls import path
from . import views


urlpatterns = [
    path("", views.home,name="home"),
    path('add_question',views.create_question, name="add_question"),
    path('question/<int:pk>/', views.question_detail, name="question_detail"),
    path('answer/like/<int:pk>/', views.like_answer, name='like_answer'),
]