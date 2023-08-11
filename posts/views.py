from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostCreateForm , CommentForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from datetime import date, datetime, timedelta


# Create your views here.
def post_list_view(request):
    
    if request.method=='GET':
        selected_category = request.GET.get("category")
        if selected_category  is None:
            selected_category  = '전체'
        notice_list = Post.objects.filter(category='공지') #공지사항 글
        event_list = Post.objects.filter(category= '이벤트')
        filter_list = Post.objects.exclude(writer__username='alltogether') # 일반 사용자들 글
            
        if selected_category  == '전체': # 전체글 : 공지, 이벤트, 나머지
            context = {
                'notice_list' : notice_list,
                'event_list': event_list,
                'post_list' : filter_list,
            }
        elif selected_category == '공지':
            context = {
                'notice_list' : notice_list,
            }
        elif selected_category == '이벤트':
            context = {
                'event_list' : event_list,
            }
        elif selected_category == '인기글':
            filter_list = filter_list.order_by('-view_count')
            context = {
                'post_list':filter_list,
            }
            
        else:
            filter_list = filter_list.filter(category=selected_category) 
            context = {
                'post_list' : filter_list,
            }
        return render(request,'posts/post-all.html',context)
    

def post_create_view(request):
    if request.method=='GET':
        form = PostCreateForm()
        context = {'form':form}
        return render(request, 'posts/post-create.html',context)
    elif request.method == 'POST':
        title = request.POST.get("post_title")
        content = request.POST.get("post_content")
        category = request.POST.get("post_category")
        writer = request.user
        post = Post.objects.create(
            title = title,
            content = content,
            writer = writer,
            category = category,
        )
        return redirect('posts:post-list-all')
    else:
        return redirect('posts:post-list-all')

def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = {
            'post': post,
            'commentForm': CommentForm(),
        }

        # 쿠키 처리
        cookie_name = f'cookie_{id}'
        if cookie_name not in request.COOKIES:
            post.view_count +=1
            post.save()
            
            expires = datetime.utcnow() + timedelta(seconds=30)  # 쿠키 만료 시간 (1일로 설정할 경우 days=1, 일단 테스트하기 위해 30초마다 쿠키 만료)
            expires = expires.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
            response = HttpResponse(render(request, 'posts/post-detail.html',context))
            response.set_cookie(cookie_name, 'true', expires=expires)
            return response
        return render(request, 'posts/post-detail.html', context)
    if request.method =='POST':
        post = Post.objects.get(id=id)
        content = request.POST.get('comment_content')
        if content:
            comment = Comment.objects.create(
                content = content,
                post = post,
                writer = request.user,
            )
        else: 
            pass
        context = {
            'post':post,
        }
        return render(request,'posts/post-detail.html',context)
    return render(request,'post/post-detail.html')

def like_view(request, bid):
    post = get_object_or_404(Post, id=bid)
    user = request.user
    if post.like.filter(id =user.id).exists():
        post.like.remove(user)
        return JsonResponse({'message':'delete','like_count':post.like.count()})
    else:
        post.like.add(user)
        return JsonResponse({'message':'ok','like_count':post.like.count()})
    