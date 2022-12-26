from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome/'),
    path('cbvdetail/<int:pk>/', views.DetailListView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.UpdateListView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.DetailListView.as_view(), name='cbvdelete'),
]