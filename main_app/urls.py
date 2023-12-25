from django.urls import path

from main_app import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('profile/', views.profile_page, name="profile"),
    path('profile_view', views.profile_view, name="profile_view"),
    path('', views.post_list, name="postlist"),
    path('create_post', views.create_post, name="create_post"),
    path('postdetails/<int:id>/', views.post_details,name="postdetails"),
    path('delete/<int:id>/', views.delete_post,name="delete"),
    path('update/<int:id>/', views.update_post,name="update"),
    path('update_blogger_profile', views.update_blogger_profile,name="update_blogger_profile"),
    path('update_viewer_profile', views.update_viewer_profile,name="update_viewer_profile"),
    path('viewer_profile_view', views.viewer_profile_view,name="viewer_profile_view"),
]
