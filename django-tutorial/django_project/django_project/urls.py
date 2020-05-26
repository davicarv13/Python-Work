from django.contrib import admin
from django.urls import path, include

#Uso do alias 'as' para não ocorrer conflito entre essa views e as views de user
from django.contrib.auth import views as auth_views 

#Importação direta da view, para que não seja necessário 
#passar pelo arquivo urls.py da aplicação users
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    #Class based views. Essas classes tratarão a parte de login e logout,
    #mas não tratarão a parte de templates

    #template_name define uma origem diferente da padrão do django,
    #que seria registration/arquivo.html
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]

#Apenas quando modo DEBUG for true
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
















