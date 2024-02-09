
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login_page,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_page,name="register"),
    path('home/',views.home,name="home"),
    path("create_todo/",views.create_todo),
    path("delete-todo/<id>",views.delete_todo),
    path("edit-todo/<id>/<status>/",views.edit_todo),
]
