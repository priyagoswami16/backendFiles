from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name = 'pooko'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('Detail/<int:id>',views.Detail,name='Detail'),
    path('ecomproduct',views.ecomproduct,name='ecomproduct'),
    path('categry',views.categry,name='categry'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
