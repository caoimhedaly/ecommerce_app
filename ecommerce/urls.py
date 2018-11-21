from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import product_list, product_detail
from cart.views import add_to_cart, view_cart, remove_from_cart
from accounts.views import signup, show_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', show_profile, name = 'show_profile'),
    path('product/product_list', product_list, name = 'product_list'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('product/<int:id>/product_detail', product_detail, name = 'product_detail'),
    path('cart/add', add_to_cart, name = 'add_to_cart'),
    path('cart/view', view_cart, name= 'view_cart'),
    path('cart/remove', remove_from_cart, name = 'remove_from_cart')

]
