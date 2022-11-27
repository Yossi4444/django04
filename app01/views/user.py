from django.shortcuts import render,redirect
from app01 import models
from app01.utils.pagnation import Pagination
from app01.form.form import UserModelForm,PrettyNumModelForm,PrettyNumEditModelForm
# Create your views here.

#用户管理
def user_list(request):
    data_dict = {}
    value = request.GET.get('q', '')
    if value:
        # name__contains要变
        data_dict['name__contains'] = value
    # models.Admin.objects.filter中Admin要变
    queryset = models.UserInfo.objects.filter(**data_dict).order_by('id')
    # queryset = models.UserInfo.objects.all()
    page_object = Pagination(request, queryset)
    contex = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'value':value
    }
    return render(request,'user_list.html',contex)
def user_add(request):
    context = {
        'gender_choices':models.UserInfo.gender_choices,
        'depart_list':models.Department.objects.all(),
    }
    if request.method=='GET':
        return render(request,'user_add.html',context)
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    password = request.POST.get('password')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    depart = request.POST.get('depart')
    context ='页面无'
    if len(name)==0 or len(password)==0:
        return render(request,'error.html',{'context':context})
    models.UserInfo.objects.create(name=name,age=age,gender=gender,password=password,account=account,create_time=create_time,depart_id=depart)
    return redirect('/user/list/')
def user_model_form_add(request):
    """添加用户（ModelForm版本）"""
    if request.method=='GET':
        form= UserModelForm()
        # return redirect("/user/list/")
        return render(request,'user_model_form_add.html',{'form':form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    else:
       return render(request,'user_model_form_add.html',{'form':form})
def user_delete(request):
    nid=request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
def user_edit(request):
    nid = request.GET.get('nid')
    if request.method=='GET':
        row_object=models.UserInfo.objects.filter(id=nid).first()
        form=UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{'form':form})
    # 不能实现更新功能
    row_object= models.UserInfo.objects.filter(id = nid).first()
    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    else:
        return render(request, 'user_edit.html', {'form': form})