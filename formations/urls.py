from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from .views import Surveillant 
from .views import FormationViewSet, GameViewSet, CourseViewSet, FileUploadView


urlpatterns = [
    path('upload', FileUploadView.as_view()),
    path("formation" , FormationViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('formation/<str:pk>', FormationViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("game" , GameViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('game/<str:pk>', GameViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
     path("course" , CourseViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('course/<str:pk>', CourseViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)