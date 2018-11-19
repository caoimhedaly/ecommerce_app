
from django.contrib import admin
from django.urls import path, include
from products.views import product_list
from accounts.views import signup, show_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', show_profile, name = 'show_profile')
]
