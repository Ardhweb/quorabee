from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid
from django.urls import reverse


class Question(models.Model):
    question = models.CharField(max_length=255,verbose_name='Add Question', blank=False,null=True,help_text='Start your question with Why, What, How etc.')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uquest_id = models.CharField(verbose_name='Unique ID',max_length=25,default=uuid.uuid4().hex[:12], editable=False, null=True , blank=False)
    
    class Meta:
        ordering = ('-created_on',)

    def get_absolute_url(self):
       return reverse('question_detail',args=[self.id])

  
    


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField(help_text='Write your thought or answer comment.', max_length=450,blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uans_id = models.CharField(verbose_name="Unique ID",max_length=25,default=uuid.uuid4().hex[:12], editable=False, null=True , blank=False)
    
    class Meta:
        ordering = ('-created_on',)
       
    

class Liked(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_likes')

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f'{self.user} liked {self.answer}'