from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee_index, name='coffee_index'),
    path('coffee/<int:coffee_id>/', views.coffee_detail, name='coffee_detail'),
    path('coffee/create/', views.CoffeeCreate.as_view(), name='coffee_create'),
    path('coffee/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffee_update'),
    path('coffee/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffee_delete'),
    path('maker/', views.maker_index, name='maker_index'),
    path('maker/<int:maker_id>/', views.maker_detail, name='detail'),
    path('maker/create/', views.MakerCreate.as_view(), name='maker_create'),
    path('maker/<int:pk>/update/', views.MakerUpdate.as_view(), name='maker_update'),
    path('maker/<int:pk>/delete/', views.MakerDelete.as_view(), name='maker_delete'),
]


