from django.urls import path
from .views import home, login_view, admin_panel, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('logout/', logout_view, name='logout'),  # Certifique-se que isso esteja aqui
]
