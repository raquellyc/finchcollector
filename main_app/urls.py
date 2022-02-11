from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name='birds_delete'),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/assoc_seed/<int:seed_id>/', views.assoc_seed, name='assoc_seed'),
    path('birds/<int:bird_id>/unassoc_seed/<int:seed_id>/', views.unassoc_seed, name='unassoc_seed'),
    path('seeds/', views.SeedList.as_view(), name='seeds_index'),
    path('seeds/<int:pk>/', views.SeedDetail.as_view(), name='seeds_detail'),
    path('seeds/create/', views.SeedCreate.as_view(), name='seeds_create'),
    path('seeds/<int:pk>/update/', views.SeedUpdate.as_view(), name='seeds_update'),
    path('seeds/<int:pk>/delete/', views.SeedDelete.as_view(), name='seeds_delete'),
]