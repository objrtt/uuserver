from django.conf.urls import url
from kyc.apps.upload import views

urlpatterns = [
    # 匹配`upload/`成功就调用`views`中的`kyc`函数
    url(r'^upload/$', views.upload),
]