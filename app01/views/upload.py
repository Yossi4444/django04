from django.shortcuts import render,redirect,HttpResponse
from app01 import models
def upload_list(request):
    if request.method == 'GET':
        return render(request,'upload_list.html')
    file_object = request.FILES.get('files')
    # f = open('a1.png', mode='wb')
    f = open(file_object.name,mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse('success!!')