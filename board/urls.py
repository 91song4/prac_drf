from django.urls import path
from board import views

urlpatterns = [
    # path('', views.route_def),
    path('create/', views.create_board),
    path('read/', views.read_boards),
    path('read/<int:board_id>/', views.read_board),
    path('update/<int:board_id>/', views.update_board),
    path('delete/<int:board_id>/', views.delete_board),
]
