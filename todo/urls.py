from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('delete/<id>',views.deletetodo,name='delete'),
    path('mark/<id>',views.marktodo,name='marktodo'),
    path('unmark/<id>',views.unmarktodo,name='unmarktodo'),
    path('add',views.addtodo,name='addtodo'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('',views.home,name='home')

]
