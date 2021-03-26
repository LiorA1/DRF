
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter() # generate all the paths automatically
router.register('languages', views.LanguageViewSet)
router.register('paradigms', views.ParadigmViewSet)
router.register('programmers', views.ProgrammerViewSet)

urlpatterns = [
    
    path('', include(router.urls)),

]

#print(router.urls)
