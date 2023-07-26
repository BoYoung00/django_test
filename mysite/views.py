# from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from  django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment
from .forms import CommentForm

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

# 로그아웃 상태에서 댓글을 달려고 하면 로그인 페이지로 보내줌
@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
    # 댓글 폼이 유효하기 작성 되었다면
    if form.is_valid():
        # 커밋하지 않을 상태로 DB에 저장
        comment = form.save(commit=False)
        comment.content_list = content_list
        comment.author = request.user
        comment.save()
        return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()

    context = {'content_list': content_list, 'form': form}
    return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # 작성자가 아닌 사용자가 update를 시도한다면 오류 발생시킴
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        # 수정 시 최초 작성했던 댓글을 화면에 출력
        form = CommentForm(instance=comment)
        context = {'comment': comment, 'form': form}
        return render(request, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
        return redirect('detail', content_id=comment.content_list.id)