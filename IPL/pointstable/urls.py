from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from . import views

urlpatterns = {
    url(r'^points/$', CreateView.as_view(), name="create"),
    path('points/<int:pk>/', views.PostDetail.as_view()),
    url(r'^$', views.home, name='home'),
    # url(r'^send/$', views.send, name='send'),
}

urlpatterns = format_suffix_patterns(urlpatterns)