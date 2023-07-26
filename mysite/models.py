from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    # 제목이 obj형태가 아닌 문자열로 반환해서 보여주기
    def __str__(self): return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 자신과 다대일 관계
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)