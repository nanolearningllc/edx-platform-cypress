"""
Course API URLs
"""
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',
    url(r'^v1/blocks/', include('course_api.blocks.urls'))
)
