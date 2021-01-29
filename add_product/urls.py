from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.product_form, name='product_insert'), #get and post request for insert operation 
    path('<int:id>/',views.product_form, name='product_update'), # get and post request for update operation
    path('delete/<int:id>', views.product_delete, name='product_delete'), 
    path('list/', views.product_list, name = 'product_list') # get request to retrive and display all records
]
