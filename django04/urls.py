"""django03 URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import depart,user,prettynum,admin,account,task,cool,upload
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/edit/', depart.depart_edit),
    path('depart/upload/', depart.depart_upload),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/delete/', user.user_delete),
    path('user/edit/', user.user_edit),
    # 靓号管理
    path('prettynum/list/', prettynum.prettynum_list),
    path('prettynum/add/', prettynum.prettynum_add),
    path('prettynum/delete/', prettynum.prettynum_delete),
    path('prettynum/edit/', prettynum.prettynum_edit),
    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/delete/', admin.admin_delete),
    path('admin/edit/', admin.admin_edit),
    # 登录、注销
    path('login/', account.login),
    path('logout/', account.logout),
    # 图片验证码
    path('image/code/', account.image_code),
    #  任务管理
    path('task/list/', task.task_list),
    # 酷炫界面
    path('cool/yanhua/', cool.cool_yanhua),
    # 文件操作
    path('upload/list/',upload.upload_list)

]
