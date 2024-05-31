from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_buildings', views.show_buildings, name='show-buildings'),
    path('show_flats/<int:id>', views.show_flats, name='show-flats'),
    path('add_building', views.add_building, name='add-building'),
    path('add_flat', views.add_flat, name='add-flat'),
    path('my_flats', views.my_flats, name='my-flats'),
    path('dashboard', views.dashboard, name='dash-board'),
    path('userlist', views.userlist, name='user-list'),
    path('get_rent/<int:id>', views.get_rent, name='get-rent'),
    path('edit_flat/<int:id>', views.edit_flat, name='edit-flat'),
    path('delete_flat/<int:id>', views.delete_flat, name='delete-flat'),
]
