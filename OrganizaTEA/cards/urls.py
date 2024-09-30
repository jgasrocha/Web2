from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import card_list, card_create, card_edit, card_delete, card_management

urlpatterns = [
    path('', card_list, name='card_list'),
    path('create/', card_create, name='card_create'),
    path('edit/<int:pk>/', card_edit, name='card_edit'),
    path('delete/<int:pk>/', card_delete, name='card_delete'),
    path('manage/', card_management, name='card_management'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
