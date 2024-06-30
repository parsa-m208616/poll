from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question_detail, name='question'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('test', views.test_page, name='test')
]
