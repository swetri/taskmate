
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from todolist import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist.urls')),
    path('account/', include('users.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
]

