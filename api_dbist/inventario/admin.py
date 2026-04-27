from django.contrib import admin

from .models import Categoria, Factura, FacturaDetalle, Inventario, Producto, Proveedor, Usuario

admin.site.site_header = "DBIST - Sistema de Inventario"
admin.site.site_title = "DBIST Admin"
admin.site.index_title = "Panel de Administración"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo_cat", "nombre", "descripcion")
    search_fields = ("codigo_cat", "nombre")
    ordering = ("codigo_cat",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "codigo_proveedor",
        "nombre",
        "servicio",
        "telefono",
        "correo_electronico",
        "pagina_web",
    )
    search_fields = ("codigo_proveedor", "nombre", "correo_electronico")
    ordering = ("codigo_proveedor",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo_produ", "nombre", "categoria", "proveedor")
    list_filter = ("categoria", "proveedor")
    search_fields = ("codigo_produ", "nombre")
    ordering = ("codigo_produ",)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre_propietario",
        "apellido_propietario",
        "correo_electronico",
        "telefono",
        "direccion",
    )
    search_fields = ("nombre_propietario", "apellido_propietario", "correo_electronico")
    ordering = ("apellido_propietario", "nombre_propietario")


class FacturaDetalleInline(admin.TabularInline):
    model = FacturaDetalle
    extra = 1
    fields = ("producto", "cantidad", "valor_unitario")


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("codigo_fact", "fecha", "usuario")
    list_filter = ("fecha", "usuario")
    search_fields = ("codigo_fact", "usuario__nombre_propietario", "usuario__apellido_propietario")
    ordering = ("-fecha",)
    inlines = [FacturaDetalleInline]


@admin.register(FacturaDetalle)
class FacturaDetalleAdmin(admin.ModelAdmin):
    list_display = ("id", "factura", "producto", "cantidad", "valor_unitario")
    list_filter = ("factura", "producto")
    search_fields = ("factura__codigo_fact", "producto__nombre")
    ordering = ("factura",)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ("cod_inv", "producto", "cantidad_stock")
    search_fields = ("producto__codigo_produ", "producto__nombre")
    ordering = ("producto",)