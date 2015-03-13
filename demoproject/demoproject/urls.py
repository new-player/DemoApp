from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from demoapp.views import AccountViewSet
from demoproject.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
        
)
                       
