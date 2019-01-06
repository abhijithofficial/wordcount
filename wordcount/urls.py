from django.urls import path
from . import views
from . import new

urlpatterns = [
    path('',views.hello,name='home'),
    
    path('count/',new.count,name='count'),

    path('aboutus/',new.aboutus,name='about'),
]
