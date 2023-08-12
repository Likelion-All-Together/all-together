from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from informations.models import RegionAndMulticultural, Afterschool

# 회원가입
def signup_view(request):
    
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm()
        context = { 'form' : form }
        return render(request, 'accounts/signup.html', context)
    
    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        
        if form.is_valid(): # 폼이 유효하다면 회원가입 처리
            instance = form.save()
            return redirect('accounts:login') # 로그인으로 리다이렉트
            
        else: # 그렇지 않다면 다시 회원가입 창 띄우기
            return redirect('accounts:signup')

# 로그인
def login_view(request):
    
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()}) # 로그인 HTML 응답
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            return redirect('diamoyeo:home') # 응답
        # 응답
        
        else: # 비즈니스 로직 처리 - 로그인 실패
            return render(request, 'accounts/login.html', {'form' : form})
        
# 로그아웃
def logout_view(request):
    if request.user.is_authenticated: # 데이터 유효성 검사
        logout(request) # 비즈니스 로직 처리
    return redirect('diamoyeo:home') # 응답

# 마이페이지
@login_required
def mypage_view(request):
    
    # 일단 기존 데이터 조회
    introduction = request.user.introduction
    profile_image = request.user.profile_image
    
    if request.method == 'GET': # GET이면 홈페이지 보여주기
        return render(request, 'accounts/mypage.html')
    
    else: # POST이면 유저 정보 업데이트
        
        # 새로운 정보 가져오기
        new_introduction = request.POST.get('introduction').strip()
        new_profile_image = request.FILES.get('image')
        
        # 소개를 비교
        if (introduction != new_introduction):
            request.user.introduction = new_introduction
        else:
            request.user.introduction = introduction
            
        # 프로필 이미지를 비교
        if (profile_image != new_profile_image):
            # 프로필 이미지에 대한 업데이트
            request.user.profile_image = new_profile_image
        else:
            request.user.profile_image = profile_image
        
        # 새 프로필 이미지를 제출하지 않는 경우 기존 이미지 값 넣어주기 - 중요!
        if (new_profile_image == None):
            request.user.profile_image = profile_image
        
        # 유저 업데이트
        request.user.save()
        
        return redirect('accounts:mypage')
    
# 내 활동 보기
def activities_view(request):
    category = request.GET.get('category', 'posts')  # 기본 posts
    
    # 내가 작성한 글
    if category == 'posts':
        item_list = Post.objects.filter(writer=request.user).order_by('-created_at')
    # 내가 작성한 댓글
    elif category == 'comments':
        item_list = Comment.objects.filter(writer=request.user).order_by('-created_at')
    # 내가 좋아요 누른 글
    elif category == 'likes':
        item_list = Post.objects.filter(like=request.user).order_by('-created_at')
    # 내가 스크랩 한 글
    elif category == 'scraps':
        region_and_multicultural_list = RegionAndMulticultural.objects.filter(scrap=request.user).order_by('-created_at')
        afterschool_list = Afterschool.objects.filter(scrap=request.user).order_by('-created_at')
        item_list = list(region_and_multicultural_list) + list(afterschool_list)
        item_list.sort(key=lambda x: x.created_at, reverse=True)
        
    context = {
        'category': category,
        'item_list': item_list,
    }
    
    return render(request, 'accounts/activities.html', context)