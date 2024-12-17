from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="plants"

urlpatterns=[
    path("", views.MainView.as_view(), name="all"),
    path("open", views.OpenView.as_view(), name="open"),
    path("create/", views.PlantCreateView.as_view(), name="plant_create"),
    path('success/', views.PlantSuccessView.as_view(), name='plant_success'),
    path('plant/<int:pk>/', views.PlantDetailView.as_view(), name='plant_detail'),
    path('plant/<int:pk>/update/', views.PlantUpdateView.as_view(), name='plant_update'),
    path('plant/<int:pk>/delete/', views.PlantDeleteView.as_view(), name='plant_delete'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)