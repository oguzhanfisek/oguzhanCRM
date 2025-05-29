from django.urls import path
from .views.auth_views import register, login_view, logout_view, users_page, reports_view, settings_view
from .views.dashboard_views import dashboard_view
from .views.product_view import (
    product_list, add_product, delete_product, edit_product, publish_product,
    product_list_store, toggle_publish, published_products, category_list, category_add
)
from .views.category_views import category_edit, category_delete

from .views.user_views import profile_view, change_password
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', dashboard_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', users_page, name='users_page'),
    path('products/', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('products/delete/<int:pk>/', delete_product, name='delete_product'),
    path('products/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('profile/', profile_view, name='profile'),
    path('profile/change-password/', change_password, name='change_password'),
    path('raporlar/', reports_view, name='reports'),
    path('ayarlar/', settings_view, name='settings'),
    path('product/<int:product_id>/publish/', publish_product, name='publish_product'),
    path('store/', product_list_store, name='store'),
    path('products/toggle/<int:product_id>/', toggle_publish, name='toggle_publish'),
    path('urunler/', published_products, name='published_products'),
    path('store/', product_list_store, name='store'),
    path('kategoriler/ekle/', category_add, name='category_add'),
    path('kategoriler/', category_list, name='category_list'),
    path('kategoriler/edit/<int:category_id>/', category_edit, name='category_edit'),
    path('kategoriler/delete/<int:category_id>/', category_delete, name='category_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
