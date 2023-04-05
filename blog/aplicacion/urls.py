from django.urls import path
from aplicacion.views import index, about, blogpost, bloglist, PosteoList, PosteoCreacion

urlpatterns = [
    path("", index, name="inicio"),
    path("pages/", bloglist, name="lista de blog"),
    path("blog-post/", blogpost, name="posteo de blog"),
    path("about/", about, name="acerca de mi"),
    path('posteo/list/', PosteoList.as_view(), name='List'),
    path('blog-form/', PosteoCreacion.as_view(), name='New'),
]