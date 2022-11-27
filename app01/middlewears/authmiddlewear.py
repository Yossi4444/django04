from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class AuthMiddlewear(MiddlewareMixin):
    def process_request(self,request):
        # 1、排除不需要登录就能访问的页面
        if request.path_info in[ '/login/','/image/code/']:
            return
        # 2、读取当前访问用户session信息，如果读到则通过，如果没读到则放回登录页面
        cookies = request.session.get('info')
        if cookies:
            return
        return redirect('/login/')