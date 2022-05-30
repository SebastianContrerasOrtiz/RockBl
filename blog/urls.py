from django.urls import path 
from blog.views import home, form_post, form_mod_post, form_del_post


urlpatterns = [
    path('',home,name='home'),
    path('form-post',form_post,name='form_post'),
    path('form_mod_post/<id>',form_mod_post,name='form_mod_post'),
    path('form_del_post/<id>',form_del_post,name='form_del_post'),


]