from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name = 'managment'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('Home', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('slider', views.slider, name='slider'),
    path('ecom', views.ecom, name='ecom'),
    path('update<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)