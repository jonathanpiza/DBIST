from datetime import date
from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import (
    CategoriaForm,
    FacturaForm,
    InventarioForm,
    ProductoForm,
    ProveedorForm,
    UsuarioForm,
)
from .models import Categoria, Factura, FacturaDetalle, Inventario, Producto, Proveedor, Usuario


# ── Dashboard ─────────────────────────────────────────────────────────────────
class IndexView(TemplateView):
    template_name = "inventario/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "total_categorias": Categoria.objects.count(),
                "total_proveedores": Proveedor.objects.count(),
                "total_productos": Producto.objects.count(),
                "total_usuarios": Usuario.objects.count(),
                "total_facturas": Factura.objects.count(),
                "total_inventario": Inventario.objects.count(),
            }
        )
        return ctx


# ── Categoria ─────────────────────────────────────────────────────────────────
class CategoriaListView(ListView):
    model = Categoria
    template_name = "inventario/categoria_list.html"
    context_object_name = "categorias"
    ordering = ["codigo_cat"]


class CategoriaCreateView(SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("categorias")
    success_message = "Categoría creada correctamente."
    extra_context = {"titulo": "Nueva Categoría", "back_url": reverse_lazy("categorias")}


class CategoriaUpdateView(SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("categorias")
    success_message = "Categoría actualizada correctamente."
    extra_context = {"titulo": "Editar Categoría", "back_url": reverse_lazy("categorias")}


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("categorias")
    extra_context = {"titulo": "Eliminar Categoría", "back_url": reverse_lazy("categorias")}


# ── Proveedor ─────────────────────────────────────────────────────────────────
class ProveedorListView(ListView):
    model = Proveedor
    template_name = "inventario/proveedor_list.html"
    context_object_name = "proveedores"
    ordering = ["codigo_proveedor"]


class ProveedorCreateView(SuccessMessageMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("proveedores")
    success_message = "Proveedor creado correctamente."
    extra_context = {"titulo": "Nuevo Proveedor", "back_url": reverse_lazy("proveedores")}


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("proveedores")
    success_message = "Proveedor actualizado correctamente."
    extra_context = {"titulo": "Editar Proveedor", "back_url": reverse_lazy("proveedores")}


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("proveedores")
    extra_context = {"titulo": "Eliminar Proveedor", "back_url": reverse_lazy("proveedores")}


# ── Producto ──────────────────────────────────────────────────────────────────
class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"
    context_object_name = "productos"
    ordering = ["codigo_produ"]


class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("productos")
    success_message = "Producto creado correctamente."
    extra_context = {"titulo": "Nuevo Producto", "back_url": reverse_lazy("productos")}


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("productos")
    success_message = "Producto actualizado correctamente."
    extra_context = {"titulo": "Editar Producto", "back_url": reverse_lazy("productos")}


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("productos")
    extra_context = {"titulo": "Eliminar Producto", "back_url": reverse_lazy("productos")}


# ── Usuario ───────────────────────────────────────────────────────────────────
class UsuarioListView(ListView):
    model = Usuario
    template_name = "inventario/usuario_list.html"
    context_object_name = "usuarios"
    ordering = ["apellido_propietario"]


class UsuarioCreateView(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("usuarios")
    success_message = "Usuario creado correctamente."
    extra_context = {"titulo": "Nuevo Usuario", "back_url": reverse_lazy("usuarios")}


class UsuarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("usuarios")
    success_message = "Usuario actualizado correctamente."
    extra_context = {"titulo": "Editar Usuario", "back_url": reverse_lazy("usuarios")}


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("usuarios")
    extra_context = {"titulo": "Eliminar Usuario", "back_url": reverse_lazy("usuarios")}


# ── Factura ───────────────────────────────────────────────────────────────────
class FacturaListView(ListView):
    model = Factura
    template_name = "inventario/factura_list.html"
    context_object_name = "facturas"
    ordering = ["-fecha"]


class FacturaVentaCreateView(TemplateView):
    template_name = "inventario/factura_tienda_form.html"

    def _context(self, form_data=None):
        return {
            "titulo": "Nueva Venta",
            "back_url": reverse_lazy("facturas"),
            "usuarios": Usuario.objects.order_by("apellido_propietario", "nombre_propietario"),
            "stocks": (
                Inventario.objects.select_related("producto")
                .filter(cantidad_stock__gt=0)
                .order_by("producto__nombre")
            ),
            "hoy": date.today().isoformat(),
            "form_data": form_data or {},
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self._context())

    def post(self, request, *args, **kwargs):
        form_data = {
            "fecha": request.POST.get("fecha", ""),
            "usuario_id": request.POST.get("usuario_id", ""),
        }

        usuario_id = request.POST.get("usuario_id")
        fecha = request.POST.get("fecha")
        productos = request.POST.getlist("producto_id[]")
        cantidades = request.POST.getlist("cantidad[]")
        valores = request.POST.getlist("valor_unitario[]")

        if not usuario_id or not fecha:
            messages.error(request, "Debes seleccionar cliente y fecha.")
            return render(request, self.template_name, self._context(form_data))

        lineas = []
        for idx, producto_id in enumerate(productos):
            if not producto_id:
                continue

            cant_txt = cantidades[idx] if idx < len(cantidades) else "0"
            val_txt = valores[idx] if idx < len(valores) else "0"
            try:
                cantidad = int(cant_txt)
                valor = Decimal(val_txt)
            except (ValueError, InvalidOperation):
                messages.error(request, "Cantidad o valor unitario invalido en una linea.")
                return render(request, self.template_name, self._context(form_data))

            if cantidad <= 0 or valor <= 0:
                messages.error(request, "Cantidad y valor unitario deben ser mayores a 0.")
                return render(request, self.template_name, self._context(form_data))

            lineas.append({"producto_id": int(producto_id), "cantidad": cantidad, "valor_unitario": valor})

        if not lineas:
            messages.error(request, "Debes agregar al menos un producto.")
            return render(request, self.template_name, self._context(form_data))

        # Evita duplicados por producto para respetar unique_together en FacturaDetalle.
        consolidado = {}
        for linea in lineas:
            p_id = linea["producto_id"]
            if p_id not in consolidado:
                consolidado[p_id] = {"cantidad": 0, "valor_unitario": linea["valor_unitario"]}
            consolidado[p_id]["cantidad"] += linea["cantidad"]

        try:
            with transaction.atomic():
                factura = Factura.objects.create(fecha=fecha, usuario_id=usuario_id)

                for producto_id, data in consolidado.items():
                    stock = (
                        Inventario.objects.select_for_update()
                        .select_related("producto")
                        .filter(producto_id=producto_id)
                        .first()
                    )
                    if not stock:
                        raise ValueError("Uno de los productos no tiene registro de inventario.")

                    if stock.cantidad_stock < data["cantidad"]:
                        raise ValueError(
                            f"Stock insuficiente para {stock.producto.nombre}. Disponible: {stock.cantidad_stock}."
                        )

                    FacturaDetalle.objects.create(
                        factura=factura,
                        producto_id=producto_id,
                        cantidad=data["cantidad"],
                        valor_unitario=data["valor_unitario"],
                    )
                    stock.cantidad_stock -= data["cantidad"]
                    stock.save(update_fields=["cantidad_stock"])
        except ValueError as exc:
            messages.error(request, str(exc))
            return render(request, self.template_name, self._context(form_data))

        messages.success(request, f"Venta registrada en factura FAC-{factura.codigo_fact}.")
        return redirect("facturas")


class FacturaCreateView(SuccessMessageMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("facturas")
    success_message = "Factura creada correctamente."
    extra_context = {"titulo": "Nueva Factura", "back_url": reverse_lazy("facturas")}


class FacturaUpdateView(SuccessMessageMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("facturas")
    success_message = "Factura actualizada correctamente."
    extra_context = {"titulo": "Editar Factura", "back_url": reverse_lazy("facturas")}


class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("facturas")
    extra_context = {"titulo": "Eliminar Factura", "back_url": reverse_lazy("facturas")}


# ── Inventario ────────────────────────────────────────────────────────────────
class InventarioListView(ListView):
    model = Inventario
    template_name = "inventario/inventario_list.html"
    context_object_name = "inventarios"
    ordering = ["producto"]


class InventarioCreateView(SuccessMessageMixin, CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("inventarios")
    success_message = "Registro de inventario creado correctamente."
    extra_context = {"titulo": "Nuevo Registro de Inventario", "back_url": reverse_lazy("inventarios")}


class InventarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = "inventario/form.html"
    success_url = reverse_lazy("inventarios")
    success_message = "Inventario actualizado correctamente."
    extra_context = {"titulo": "Editar Inventario", "back_url": reverse_lazy("inventarios")}


class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = "inventario/confirm_delete.html"
    success_url = reverse_lazy("inventarios")
    extra_context = {"titulo": "Eliminar Inventario", "back_url": reverse_lazy("inventarios")}
