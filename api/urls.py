from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
import debug_toolbar

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('auth/token-auth/', obtain_jwt_token),
    path('auth/', include('authentication.urls')),
    path('ingredients/', include('ingredient.urls')),
    path('cocktails/', include('cocktail.urls')),
    path('user/', include('bar.urls')),
]
