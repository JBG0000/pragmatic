from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy  # accountap 내부의 hello_world로 재접속하라
from django.views.generic import CreateView, DetailView

from accountap.models import HelloWorld #models에 있던 DB저장 유형틀 쓸거다!


def hello_world(request):

    if request.method == "POST":    #post : 객체를 생성할때 주로 사용
        temp = request.POST.get('hello_world_input')    #작성한걸 읽는다!
        
        new_hello_world = HelloWorld()  #models에서 정의한 틀 쓰겠다! 그 변수다!
        new_hello_world.text = temp #text 읽어온거 저장
        new_hello_world.save()  #DB 저장
        
        # hello_world_list = HelloWorld.objects.all() #헬로우 월드의 모든 저장내용을 리스트에 저장
        
        return HttpResponseRedirect(reverse('accountap:hello_world'))    #temp에 저장된 써진 내용, 읽어온 걸 반환하는 함수(hello_world.html로 가서 출력된다) : ㄲ
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountap/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):    #회원가입 창 : 파라미터 넘겨주기~
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountap:hello_world') #성공시 연결 url
    template_name = 'accountap/create.html'

class AccountDetailView(DetailView):    #마이페이지
    model = User
    context_object_name = 'target_user' #다른 사람이 내 마이페이지에 들어와도 내용을 잘 볼 수 있도록
    template_name = 'accountap/detail.html'
