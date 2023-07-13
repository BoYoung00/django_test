# from django.http import HttpResponse
from  django.shortcuts import render
from .models import MainContent

def index(requset):
    # return HttpResponse("Hello world")

    # 가장 최신 컨텐츠를 상단에 노출
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    # render() 함수는 content_list의 데이터를 mysite/content_list.html 파일에 적용 후 html을 리턴
    return render(requset, 'mysite/content_list.html', context)
    # mysite / content_list.html는 템플릿임