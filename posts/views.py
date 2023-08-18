from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostCreateForm , CommentForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from itertools import chain
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def post_list_view(request):
    
    if request.method=='GET':
        selected_category = request.GET.get('category')
        page = request.GET.get('page')
        
        if selected_category  is None:
            selected_category  = '전체'
        
        notice_list = Post.objects.filter(category = '공지').order_by('-created_at') #공지사항 글
        event_list = Post.objects.filter(category = '이벤트').order_by('-created_at')
        filter_list = Post.objects.exclude(writer__username = '관리자').order_by('-created_at') # 일반 사용자들 글
        
        if selected_category  == '전체': # 전체글 (완료)
            
            notice_list = notice_list[:5] # 공지 5개
            
            page_obj, paginator = make_page_obj(filter_list, page, 8) # 일반글 8개
            
            context = {
                'notice_list' : notice_list, # 공지글 5개
                'page_obj' : page_obj,
                'paginator' : paginator,
                'category' : selected_category,
            }
        elif selected_category == '공지': # 공지 글만 보이게 (완료)
            
            page_obj, paginator = make_page_obj(notice_list, page, 13)
            
            context = {
                'page_obj' : page_obj,
                'paginator' : paginator,
                'category' : selected_category,
            }
        elif selected_category == '이벤트': # 이벤트 글만 보이게 (완료)
            
            page_obj, paginator = make_page_obj(event_list, page, 13)
            
            context = {
                'page_obj' : page_obj,
                'paginator' : paginator,
                'category' : selected_category,
            }
            
        elif selected_category == '인기글': # 인기글만 보이게
            
            # 조회수가 0인 게시글 제외
            filter_list = filter_list.exclude(view_count=0).order_by('-view_count')
            
            page_obj, paginator = make_page_obj(filter_list, page, 13)
            
            context = {
                'post_list': filter_list,
                'page_obj' : page_obj,
                'paginator' : paginator,
                'category' : selected_category,
            }
            
        else: # 공지 5개, 선택된 카테고리에 해당하는 글 14개
            
            notice_list = notice_list[:5] # 공지 5개
            filter_list = filter_list.filter(category=selected_category) # 선택된 카테고리 글
            
            page_obj, paginator = make_page_obj(filter_list, page, 8)
            
            context = {
                'notice_list' : notice_list,
                'page_obj' : page_obj,
                'paginator' : paginator,
                'category' : selected_category,
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
        category = request.POST.get("align_mode")
        image = request.FILES.get("image")
        file = request.FILES.get("file")
        writer = request.user
        if image and file :
            post = Post.objects.create(
                title = title,
                content = content,
                writer = writer,
                category = category,
                image = image,
                file = file,
            )
        elif image :
            post = Post.objects.create(
                title = title,
                content = content,
                writer = writer,
                category = category,
                image = image,
            )
        elif file :
            post = Post.objects.create(
                title = title,
                content = content,
                writer = writer,
                category = category,
                file = file
            )
        else:
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
    comments = post.comment_set.all().order_by('-created_at')
    if request.method == 'GET':
        context = {
            'post': post,
            'commentForm': CommentForm(),
            'comments':comments,
        }

        # 쿠키
        cookie_name = f'cookie_{id}'
        if cookie_name not in request.COOKIES:
            post.view_count +=1
            post.save()
            
            expires = datetime.utcnow() + timedelta(seconds=30)  # 쿠키 만료 시간 (30초마다 쿠키 만료)
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

# 만들 리스트, 현재 페이지, 한 페이지당 보여줄 포스트 개수
def make_page_obj(post_list, page, num_of_post,):
    paginator = Paginator(post_list, num_of_post)
    try:
        page_obj = paginator.page(page)
        return page_obj, paginator
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
        return page_obj, paginator
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
        return page_obj, paginator

def delete_comment(request, id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:post-detail', id=id)