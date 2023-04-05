from django.urls import path
from aplicacion.views import index, about, blogpost, bloglist

urlpatterns = [
    path("", index, name="inicio"),
    path("blog-list/", bloglist, name="lista de blog"),
    path("blog-post/", blogpost, name="posteo de blog"),
    path("about/", about, name="acerca de mi"),
]