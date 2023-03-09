"""filtrumautocom URL Configuration created by ABhishek kokate  at 24/1/2023

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  patsh('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('form1',views.fun1,name='form1'),
    path('',views.logdata),
    path( 'd', views.dashbord ),
    # # path('form2',views.fun2,name='form2'),
    # # path('form3',views.fun3,name='form3'),
    # # path('form4',views.a.fun4,name='form4'),
    # path('obj',views.obj1)
    path('form',views.fun1,name='fun1'),
    path('csv',views.export_csv,name='csv'),
    path('approv',views.approve,name="approve"),
    path('emplogin',views.elogin,name='login'),
    path('empleave',views.empLeave,name='empleave'),

    path('punch_in/', views.punch_in, name='punch_in'),
    path('punch_out/', views.punch_out, name='punch_out'),
    path('punch_list/', views.punchList, name='punch_List'),

    # path('id',views.ids)
  ]