from django.urls import path, include
from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', views.api_root),

	#path('snippets/', views.snippet_list_second),
	#path('snippets/<int:pk>/', views.snippet_detail_second),
	path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
	path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="snippet-highlight"),

	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

#print("Before: ", urlpatterns)
urlpatterns = format_suffix_patterns(urlpatterns) #! Allow a clean way to referring to a specific format. (json/xml/..)
#print("After: ", urlpatterns)



from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = []
urlpatterns = [
	path('',include(router.urls)),
]