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

    #Enviar email para resetar senha
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
        name='password_reset'
        ),

    #Página para informar que o email foi enviado
    path('password-reset/done', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'
        ),

    #Página de atualização da senha
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'
        ),

    #Pagina de redirecionamento depois que senha for a atualizada
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'
        ),


    path('', include('blog.urls')),

]

#Apenas quando modo DEBUG for true
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
















