from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('test/',views.test,name='test'),
    path('about/',views.about,name='about'),
    path('branch/',views.branch,name='branch'),
    path('package/',views.package,name='package'),
    path('blog/',views.blog,name='blog'),
    path('gal/',views.gal,name='gal'),
]