from django.urls import path
from . import views

app_name='food'

urlpatterns = [
    path('', views.IndexClassView.as_view(),name='index'),
    path('<int:item_id>/', views.ItemDetailView.as_view(),name='detail'),
    path('add/',views.ItemCreateView.as_view(),name='create-item'),
    path('update/<int:id>/',views.ItemUpdateView.as_view(),name='update-item'),
    path('delete/<int:id>/',views.ItemDeleteView.as_view(),name='delete-item')
]
