from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers

from Authentication.views import AccountViewSet, LoginView, LogoutView
from demoproject.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # ... URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
        
)
