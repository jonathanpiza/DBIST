from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    path("categorias/", views.CategoriaListView.as_view(), name="categorias"),
    path("categorias/nueva/", views.CategoriaCreateView.as_view(), name="categoria_crear"),
    path("categorias/<int:pk>/editar/", views.CategoriaUpdateView.as_view(), name="categoria_editar"),
    path("categorias/<int:pk>/eliminar/", views.CategoriaDeleteView.as_view(), name="categoria_eliminar"),

    path("proveedores/", views.ProveedorListView.as_view(), name="proveedores"),
    path("proveedores/nuevo/", views.ProveedorCreateView.as_view(), name="proveedor_crear"),
    path("proveedores/<int:pk>/editar/", views.ProveedorUpdateView.as_view(), name="proveedor_editar"),
    path("proveedores/<int:pk>/eliminar/", views.ProveedorDeleteView.as_view(), name="proveedor_eliminar"),

    path("productos/", views.ProductoListView.as_view(), name="productos"),
    path("productos/nuevo/", views.ProductoCreateView.as_view(), name="producto_crear"),
    path("productos/<int:pk>/editar/", views.ProductoUpdateView.as_view(), name="producto_editar"),
    path("productos/<int:pk>/eliminar/", views.ProductoDeleteView.as_view(), name="producto_eliminar"),

    path("usuarios/", views.UsuarioListView.as_view(), name="usuarios"),
    path("usuarios/nuevo/", views.UsuarioCreateView.as_view(), name="usuario_crear"),
    path("usuarios/<int:pk>/editar/", views.UsuarioUpdateView.as_view(), name="usuario_editar"),
    path("usuarios/<int:pk>/eliminar/", views.UsuarioDeleteView.as_view(), name="usuario_eliminar"),

    path("facturas/", views.FacturaListView.as_view(), name="facturas"),
    path("facturas/nueva/", views.FacturaVentaCreateView.as_view(), name="factura_crear"),
    path("facturas/<int:pk>/editar/", views.FacturaUpdateView.as_view(), name="factura_editar"),
    path("facturas/<int:pk>/eliminar/", views.FacturaDeleteView.as_view(), name="factura_eliminar"),

    path("inventarios/", views.InventarioListView.as_view(), name="inventarios"),
    path("inventarios/nuevo/", views.InventarioCreateView.as_view(), name="inventario_crear"),
    path("inventarios/<int:pk>/editar/", views.InventarioUpdateView.as_view(), name="inventario_editar"),
    path("inventarios/<int:pk>/eliminar/", views.InventarioDeleteView.as_view(), name="inventario_eliminar"),
]
