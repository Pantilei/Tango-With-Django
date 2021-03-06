from django.conf.urls import url, include
from django.contrib import admin
from rango import views
from django.conf import settings
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^rango/', include('rango.urls')),
# above maps any URLs starting
# with rango/ to be handled by
# the rango application
url(r'^admin/', admin.site.urls),
url(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
url(r'^accounts/', include('registration.backends.simple.urls')),
]
