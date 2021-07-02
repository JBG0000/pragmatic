from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountap.models import HelloWorld #models에 있던 DB저장 유형틀 쓸거다!


def hello_world(request):

    if request.method == "POST":    #post : 객체를 생성할때 주로 사용
        temp = request.POST.get('hello_world_input')    #작성한걸 읽는다!
        new_hello_world = HelloWorld()  #models에서 정의한 틀 쓰겠다! 그 변수다!
        new_hello_world.text = temp #text 읽어온거 저장
        new_hello_world.save()  #DB 저장
        return render(request, 'accountap/hello_world.html', context={'hello_world_output': new_hello_world})    #temp에 저장된 써진 내용, 읽어온 걸 반환하는 함수(hello_world.html로 가서 출력된다)
    else:
        return render(request, 'accountap/hello_world.html', context={'text': 'GET METHOD!!!'})