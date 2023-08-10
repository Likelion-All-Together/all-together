from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostCreateForm , CommentForm

# Create your views here.
def post_list_view(request):
    if request.method=='GET':
        selected_category = request.GET.get("category")
        if selected_category  is None:
            selected_category  = '전체'
            
        if selected_category  == '전체':
            notice_list = Post.objects.filter(writer__username='alltogether') #공지사항 글
            filter_list = Post.objects.exclude(writer__username='alltogether') # 일반 사용자들 글

            context = {
                'notice_list' : notice_list,
                'post_list' : filter_list,
            }
            return render(request,'posts/post-all.html',context)
        else:
            filter_list = Post.objects.exclude(writer__username='alltogether').filter(category=selected_category) # 일반 사용자들 글
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

def post_detail_view(request,id):
    post = Post.objects.get(id=id)
    user = request.user
    if request.method == 'GET':
        context = {
            'post':post,
            'commentForm':CommentForm(),
        }
        return render(request,'posts/post-detail.html',context)
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
    