from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):
    
    def process_request(self,request):
        url = request.path
        print("url==",url)
        if url.startswith("/book/"):
            #后台管理
            urlInfoList = ["/book/register/","/book/login/"]
            if url not in urlInfoList:
                loginFlag = request.session.get("adminLogin","")
                if not loginFlag:
                    return redirect("book:login")
                
                
        # if url.startswith("/lend/"):
        #     #前台管理
        #     urlInfoList = ["/lend/register/","/lend/login/"]
        #     if url not in urlInfoList:
        #         loginFlag =  request.session.get("lendLogin","")
        #         if not loginFlag:
        #             return redirect("lend:login")