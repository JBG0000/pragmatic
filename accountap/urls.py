from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountap.views import hello_world, AccountCreateView

app_name = "accountap"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountap/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),    #로그인 로그아웃은 뷰에서 따로 함수 만들지 않아도 장고에서 제공

    path('create/', AccountCreateView.as_view(), name='create'),
]