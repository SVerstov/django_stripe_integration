from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from src.stripe.views import get_stripe_session_id, ViewItem, redirect_to_first_item, success, fail

urlpatterns = [
    path('', redirect_to_first_item,  name='home'),
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', get_stripe_session_id),
    path('item/<int:pk>/', ViewItem.as_view()),
    path('success/<int:item_id>/', success),
    path('fail/<int:item_id>/', fail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
