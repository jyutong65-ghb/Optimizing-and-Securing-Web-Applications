from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def sports(request, sp_id=None):
    # 处理GET参数
    if request.GET:
        print(request.GET)
    
    # 如果有sp_id参数
    if sp_id is not None:
        # 重定向示例：如果ID大于10，重定向到首页
        if sp_id > 10:
            # 使用HttpResponseRedirect (302临时重定向)
            # return HttpResponseRedirect('/')
            
            # 使用redirect shortcut (302临时重定向)
            return redirect('index')
            
            # 使用301永久重定向
            # return redirect('index', permanent=True)
            
        return HttpResponse(f"<h1>Articles by sports</h1><p>Article ID: {sp_id}</p>")
    
    return HttpResponse('<h1>Articles by sports</h1>')

def sports_by_year(request, year):
    return HttpResponse(f"<h1>Articles from year</h1><p>{year}</p>")

def about(request):
    return HttpResponse('<h1>About us</h1>')

def contacts(request):
    return HttpResponse('<h1>Contact information</h1>')

# 404错误处理页面
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 - Page Not Found</h1><p>Sorry, the page you are looking for does not exist.</p>')

