from django.urls import path 
from .views import * 
from django.contrib.auth.views import LogoutView


urlpatterns=[ 
    path("", index, name="Index"), 
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("sign_in", sign_in, name="sign_in"), 
    path("post", Post.as_view(), name="posts" ), 
    path("add_post", AddPost.as_view(), name="add_post"), 
    path("post_detail/<int:pk>/", ViewPost.as_view(), name="details"), 
    path("edit/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete_post"), 
    path("login", Login.as_view(), name="login"), 

    path("sign_up", Registration.as_view(), name="register")
]
