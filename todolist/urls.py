from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list',views.list,name='list'),
    path('add/<str:content>/<int:done>',views.add,name='add'),
    path('modify/<int:id>/<int:done>',views.modify,name='modify'),
    path('del/<int:id>',views.delete,name='delete'),
]