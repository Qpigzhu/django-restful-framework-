"""DjangoDrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from .settings import MEDIA_ROOT
from django.views.static import serve
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsList

router = DefaultRouter()
router.register('goods',GoodsList)



urlpatterns = [
    # path('admin/', admin.site.urls),

    #rest_framewor的Url,方便测试
    path('api-auth/', include('rest_framework.urls')),
    #xadmin后台Url
    path('xadmin/', xadmin.site.urls),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    #rest_framework自动化文档,1.11版本中注意此处前往不要加$符号
    path('docs/',include_docs_urls(title='mtianyan生鲜超市文档')),

    #食品列表
    # path('goods/',GoodsList.as_view(),name="食品列表"),
    #使用router注册Url
    path('', include(router.urls))

]
