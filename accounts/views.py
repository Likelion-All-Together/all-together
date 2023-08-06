from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm

# 회원가입
def signup_view(request):
    
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
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