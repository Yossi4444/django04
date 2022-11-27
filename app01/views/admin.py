from django.shortcuts import render,redirect

from app01 import models
from app01.utils.pagnation import Pagination
from app01.form.form import AdminModelForm
def admin_list(request):
    data_dict = {}
    value = request.GET.get('q', '')
    if value:
        data_dict['name__contains'] = value
    queryset = models.Admin.objects.filter(**data_dict).order_by('id')
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'value':value
    }
    return render(request,'admin_list.html',context)
def admin_add(request):
    if request.method == 'GET':
        form  = AdminModelForm()
        return render(request,'info_add.html',{'form':form,'title':'添加管理员'})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'info_add.html',{'form':form,'title':'添加管理员'})
def admin_delete(request):
    nid = request.GET.get('nid')
    models.Admin.objects.filter(id =nid).delete()
    return redirect('/admin/list/')
def admin_edit(request):
    context= '页面不存在'
    nid = request.GET.get('nid')
    row_object = models.Admin.objects.filter(id=nid).first()
    # 验证页面是否存在无效：
    # if not row_object:
    #     return render(request,'error.html',{'context':context})
    title = '编辑管理员'
    if request.method == 'GET':
        form = AdminModelForm(instance=row_object)
        return render(request,'info_edit.html',{'form':form,'title':title})
    # row_object = models.Admin.objects.filter(id=nid).first()
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    else:
        return render(request, 'info_edit.html', {'form': form})
