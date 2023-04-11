from django.urls import path, include
from aplicacion.views import index, about, blogpost, bloglist, PosteoList, PosteoCreacion, editarPerfil, EditarComentario, CrearComentario

urlpatterns = [
    path("", index, name="inicio"),
    path("pages", PosteoList.as_view(), name="lista de blog"),
    path(r"pages/<pk>", blogpost.as_view(), name="posteo de blog"),
    path("about", about, name="acerca de mi"),
    path('posteo/list', PosteoList.as_view(), name='List'),
    path('blog-form', PosteoCreacion.as_view(), name='New'),
    path('editar-perfil', editarPerfil, name='EditarPerfil'),
    #path('comentario', EditarComentario.as_view(), name='Comentario')
    path(r'^comentario/(?P<pk>\d+)$', CrearComentario.as_view(), name='Crear Comentario')
]