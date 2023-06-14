from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="main_home" ),
    path('pdf_file/<int:id>',views.display_files,name='display_files')

]