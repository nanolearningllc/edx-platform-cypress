"""
Course Block API URLs
"""
from django.conf import settings
from django.conf.urls import patterns, url
from .views import BlocksView


urlpatterns = patterns(
    '',
    url(
        r"^{}".format(settings.USAGE_KEY_PATTERN),
        BlocksView.as_view(),
        name="course_blocks"
    ),
)
