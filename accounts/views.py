from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm, SignUpForm
    
def signup_view(request):
    
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = { 'form' : form }
        return render(request, 'accounts/signup.html', context)
    
    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        
        # 폼이 유효하다명 회원가입 처리
        if form.is_valid():
            instance = form.save()
            # home.html으로 렌더링
            return render(request, 'home.html')
            
        # 그렇지 않다면 다시 회원가입 창 띄우기
        else:
            return redirect('accounts:signup')
    