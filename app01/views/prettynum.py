from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django.core.validators import RegexValidator
from django import forms
from app01.utils.pagnation import Pagination
from app01.form.form import UserModelForm,PrettyNumModelForm,PrettyNumEditModelForm
# Create your views here.
# 靓号管理
def prettynum_list(request):
    # for i in range(200):
    #     models.PrettyNum.objects.create(mobile='13265478974',price=100,level=2,status=2)

    # import copy
    # query_dict = copy.deepcopy(request.GET)
    # query_dict._mutable = True
    #
    # query_dict.setlist('page',[5])
    # for i in range(100):
    #     models.PrettyNum.objects.create(mobile='13245698714',level=2,price=100,status=2)
    # 分页展示
    # page_size = 10
    # page = int(request.GET.get('page',1))
    # start = (page - 1)*page_size
    # end = page*page_size


    # 查询操作
    data_dict = {}
    value = request.GET.get('q','')
    if value:
        data_dict['mobile__contains'] = value

    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('id')
    page_object = Pagination(request,queryset)
    # page_queryset = page_object.page_queryset
    # page_string = page_object.html()

    contex={
        'queryset': page_object.page_queryset,
        "value": value,
        'page_string': page_object.html()
    }

    # 总条数
    # total_count = models.PrettyNum.objects.all().count()
    # # 总页面数
    # total_page_count,div = divmod(total_count,page_size)
    # if div:
    #     total_page_count+=1
    # 显示当前前五后五页
    # plus = 4
    # start_page = page - plus
    # end_page = page + plus +1
    # if start_page <= 0:
    #     start_page = 1
    #     end_page = 10
    # if end_page > total_page_count+1:
    #     end_page = total_page_count+1
    #     start_page = total_page_count - 8
    # #页码
    # page_str_list = []
    # # 首页
    # page_first = '<li ><a href="?page={}">首页</a></li>'.format(1)
    # page_str_list.append(page_first)
    # # 上一页
    # if page>1:
    #     page_pre = '<li ><a href="?page={}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(page-1)
    # else:
    #     page_pre = '<li ><a href="?page={}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(1)
    # page_str_list.append(page_pre)
    # for i in range(start_page,end_page):
    #     if i == page:
    #         ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
    #     else:
    #         ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
    #     page_str_list.append(ele)
    # if page < total_page_count:
    #     page_after = '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'.format(page + 1)
    # else:
    #     page_after = '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'.format(total_page_count)
    # page_str_list.append(page_after)
    # # 尾页
    # page_last= '<li><a href="?page={}">尾页</a></li>'.format(total_page_count)
    # page_str_list.append(page_last)
    # search_string = """
    # <div class="input-group" style="width:100px;float:right">
    #   <input type="text" class="form-control" name="page">
    #   <span class="input-group-btn">
    #     <button class="btn btn-default" type="submit">跳转</button>
    #   </span>
    # </div>
    # """
    # page_str_list.append(search_string)
    # page_string = mark_safe("".join(page_str_list))
    return render(request,'prettynum_list.html',contex)
def prettynum_add(request):
    if request.method =='GET':
        form = PrettyNumModelForm()
        return render(request,'prettynum_add.html',{'form':form})
    form = PrettyNumModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/prettynum/list/")
    else:
        return render(request, 'prettynum_add.html', {'form': form})
def prettynum_delete(request):
    nid = request.GET.get('nid')
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/prettynum/list/')
def prettynum_edit(request):
    nid = request.GET.get('nid')
    if request.method == 'GET':
        row_object = models.PrettyNum.objects.filter(id=nid).first()
        form = PrettyNumEditModelForm(instance=row_object)
        return render(request, 'prettynum_edit.html', {'form': form})
    # 不能实现更新功能
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    form = PrettyNumEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/prettynum/list/")
    else:
        return render(request, 'prettynum_edit.html', {'form': form})