from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.lvl4index, name='lvl4index'),
    url(r'^other/$', views.other, name='other'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^register/', views.register, name='register'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^advanceindex/', views.TemplateView.as_view()),

]