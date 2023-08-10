
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from orders.views import stripe_webhook_view
from products.views import IndexView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    # глобальное имя для адресов приложения orders
    path('orders/', include('orders.urls', namespace='orders')),
    # url для вебхук страйп
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
    # информация о проекте и авторе
    path('about', AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
