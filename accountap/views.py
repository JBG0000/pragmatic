from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):

    if request.method == "POST":    #post : 객체를 생성할때 주로 사용
        return render(request, 'accountap/hello_world.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'accountap/hello_world.html', context={'text': 'GET METHOD!!!'})