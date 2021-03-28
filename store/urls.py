from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('shop/', views.products_all, name='products_all'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/categories/<slug:category_slug>/', views.category_list, name='category_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
