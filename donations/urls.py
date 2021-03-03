from django.conf.urls.static import static
from django.conf.urls import url
from donations import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name='index'),

    url(r'^donations$', views.donations, name='donations'),

    url(r'^api/appeals/$', views.AppealList.as_view()),
    url(r'^api/appeals/(?P<pk>[0-9]+)$', views.appeal_detail),
    url(r'^api/appeals/published$', views.appeal_list_published),
    url(r'^api/donations$', views.DonationList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)