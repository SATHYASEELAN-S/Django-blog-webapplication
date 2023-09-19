from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('postview/<str:pk>',views.postview,name="postview"),
    path('createblog/',views.createblog,name="createblog"),
    path('authorpost/<str:pk>',views.authorpost,name="authorpost"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('delete/<str:pk>/',views.deletepost,name="delete"),
    path('editpost/<str:pk>/',views.editpost,name="editpost")
]
  
urlpatterns+=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)