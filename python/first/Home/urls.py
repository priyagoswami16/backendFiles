
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Home'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path( '' , views.home , name='home'),
    path( 'photo' , views.photo , name='photo'),
    path( 'about' , views.about , name='about'),
    path( 'call' , views.call , name='call'),
    path( 'home2' , views.home2 , name='home2'),
    path( 'home3' , views.home3 , name='home3'),
    path( 'home4' , views.home4 , name='home4'),
    path( 'login' , views.login , name='login'),
    path( 'rgister' , views.rgister , name='rgister'),
    path( 'contacts' , views.contacts , name='contacts'),
    path( 'ecom' , views.ecom , name='ecom'),
    path( 'update<int:id>' , views.update , name='update'),
    path( 'sender' , views.sender , name='sender'),
    # path( 'search' , views.search , name='search'),
    path( 'details/<int:id>' , views.details , name='details'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
