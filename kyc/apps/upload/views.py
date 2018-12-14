# Create your views here.
from django.http import HttpResponse
# 测试项目逻辑
def upload(request):
    return HttpResponse('测试数据')