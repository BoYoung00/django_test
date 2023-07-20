# from django.http import HttpResponse
from  django.shortcuts import get_object_or_404, render
from .models import MainContent

def index(requset):
    # return HttpResponse("Hello world")

    # 가장 최신 컨텐츠를 상단에 노출
    content_list = MainContent.objects.order_by('-pub_date') # order_by('-pub_date')는 정렬
    context = {'content_list':content_list}
    # render() 함수는 content_list의 데이터를 mysite/content_list.html 파일에 적용 후 html을 리턴
    return render(requset, 'mysite/content_list.html', context)
    # mysite / content_list.html는 템플릿임

def detail(request, content_id):
    # http://localhost:8000/mysite/2/
    # content_list = MainContent.objects.get(id=content_id) # content_id는 url의 2
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = { 'content_list': content_list}
    return  render(request, 'mysite/content_detail.html', context)