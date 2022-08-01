from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    # path('cart/', include('cart.urls', namespace='cart')),
    # path('store/', include('store.urls', namespace='store')),
    # path('checkout/', include('checkout.urls', namespace='checkout')),
    path('', include('core.urls', namespace='core')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
