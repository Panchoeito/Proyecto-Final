from django.urls import path, include
from aplicacion.views import index, blogpost, bloglist, PosteoList, PosteoCreacion, editarPerfil, EditarComentario, CrearComentario, EditarPerfil, VerPerfil, EditarDetalle, about, editarDetalle, crearDetalle, DetalleCreacion, DetalleList

urlpatterns = [
    path("", index, name="inicio"),
    path("pages", PosteoList.as_view(), name="lista de blog"),
    path(r"pages/<pk>", blogpost.as_view(), name="posteo de blog"),
    path("about", DetalleList.as_view(), name="acerca de mi"),
    path('blog-form', PosteoCreacion.as_view(), name='New'),
    path('editar-perfil', editarPerfil, name='EditarPerfil'),
    #path('comentario', EditarComentario.as_view(), name='Comentario'),
    path('comentario-form', EditarComentario.as_view(), name='Crear Comentario'),
    #path("editar-perfil", EditarPerfil.as_view(), name='EditarPerfil'),
    path("editar-detalles", editarDetalle, name='Editar Detalle'),
    path("crear-detalles", DetalleCreacion.as_view(), name='Crear Detalle'),
    
]