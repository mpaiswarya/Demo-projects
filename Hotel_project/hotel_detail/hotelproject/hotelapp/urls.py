from . import views
from django.urls import path,include
app_name='hotelapp'
urlpatterns = [

    path('',views.data,name='data'),
    path('data/<int:data_id>/',views.detail,name='detail'),
    path('add/',views.add_trivago,name='add_trivago'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]