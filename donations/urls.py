from django.conf.urls.static import static
from django.conf.urls import url
from donations import views
from django.conf import settings
from django.urls import path

from .views import SignUpView


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^appeals$', views.appeals, name='appeals'),
    url(r'^donations$', views.donations, name='donations'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^register$', views.register, name='register'),
    url(r'^works$', views.works, name='works'),
    url(r'^add$', views.add, name='add'),
    url(r'^donate$', views.donate, name='donate'),

    path('signup/', SignUpView.as_view(), name='signup'),



    url(r'^api/appeals/$', views.AppealList.as_view()),
    url(r'^api/appeals/(?P<pk>[0-9]+)$', views.appeal_detail),
    url(r'^api/appeals/published$', views.appeal_list_published),
    url(r'^api/donations$', views.DonationList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)