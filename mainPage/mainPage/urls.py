from django.urls import path, include
from django.contrib import admin
from site_mainPage import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name='mainPage/mainPage.html')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("kanban_desk/", views.kanban_desk),
    path("order_card/",views.order_card),
    path("account_list", views.account_list),
]