from django.urls import path, include
from rest_framework.routers import SimpleRouter

from match.views import MatchViewSet

app_name = 'match'

router = SimpleRouter()
router.register('', MatchViewSet, '')

urlpatterns = [
    path('', include((router.urls, 'match'))),
]
