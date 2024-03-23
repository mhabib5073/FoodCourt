from django.urls import path
from foodApp import views

# namespacing
app_name = 'foodApp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>/',views.ItemDetail.as_view(),name='detail'),
    # Add Item
    path('create/', views.CreateItem.as_view(), name='create_item'),
    # edit/1
    path('update/<int:id>/',views.update_item,name='update'),
    # delete
    path('delete/<int:id>/',views.delete_item,name='delete')

]