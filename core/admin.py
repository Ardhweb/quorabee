from django.contrib import admin

# Register your models here.
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id']