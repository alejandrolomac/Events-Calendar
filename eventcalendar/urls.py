from django.contrib import admin
from django.urls import path, include
from .views import signup, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('', include('calendarapp.urls')),
]
