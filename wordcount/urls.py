from django.urls import path
from . import views
from . import new

urlpatterns = [
    path('',views.hello),
    path('count/',new.count,name='count'),
]
