from io import BytesIO
from django.shortcuts import render,redirect,HttpResponse

from app01 import models
from app01.utils.pagnation import Pagination
from app01.form.form import LoginFrom
from app01.utils.code import check_code
def task_list(request):
    return render(request,'task_list.html')