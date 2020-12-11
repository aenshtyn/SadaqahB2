from django.conf.urls.static import static
from django.conf.urls import url
from donations import views
from django.conf import settings


urlpatterns = [
    # url(r'^$', views.home),
    # url(r'^api/appeals$', views.appeal_list),
    url(r'^$', views.appeal_list),
    url(r'^donations$', views.DonationList.as_view()),
    # url(r'^api/appeals/(?P<pk>[0-9]+)$', views.appeal_detail),
    # url(r'^api/appeals/published$', views.appeal_list_published),
    #  url(r'^api/donations$', views.donation_list),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)