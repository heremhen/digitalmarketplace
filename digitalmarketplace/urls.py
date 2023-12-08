from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('hideout/', admin.site.urls),           # Admin url
    path("", include("_store.urls")),            # Store app
    path("cart/", include("_cart.urls")),        # Cart app
    path("account/", include("_account.urls")),  # Account app
    path("payment/", include("_payment.urls")),  # Payment app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
