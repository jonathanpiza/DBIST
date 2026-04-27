from django import forms

from .models import Categoria, Factura, Inventario, Producto, Proveedor, Usuario

_ctrl = {"class": "form-control"}
_sel = {"class": "form-select"}
_ta = {"class": "form-control", "rows": 3}


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["codigo_cat", "nombre", "descripcion"]
        widgets = {
            "codigo_cat": forms.TextInput(attrs=_ctrl),
            "nombre": forms.TextInput(attrs=_ctrl),
            "descripcion": forms.Textarea(attrs=_ta),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["codigo_proveedor", "nombre", "servicio", "telefono", "correo_electronico", "pagina_web"]
        widgets = {
            "codigo_proveedor": forms.TextInput(attrs=_ctrl),
            "nombre": forms.TextInput(attrs=_ctrl),
            "servicio": forms.TextInput(attrs=_ctrl),
            "telefono": forms.TextInput(attrs=_ctrl),
            "correo_electronico": forms.EmailInput(attrs=_ctrl),
            "pagina_web": forms.URLInput(attrs=_ctrl),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["codigo_produ", "nombre", "descripcion", "categoria", "proveedor"]
        widgets = {
            "codigo_produ": forms.TextInput(attrs=_ctrl),
            "nombre": forms.TextInput(attrs=_ctrl),
            "descripcion": forms.Textarea(attrs=_ta),
            "categoria": forms.Select(attrs=_sel),
            "proveedor": forms.Select(attrs=_sel),
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "nombre_propietario",
            "apellido_propietario",
            "correo_electronico",
            "telefono",
            "direccion",
            "contrasena",
        ]
        widgets = {
            "nombre_propietario": forms.TextInput(attrs=_ctrl),
            "apellido_propietario": forms.TextInput(attrs=_ctrl),
            "correo_electronico": forms.EmailInput(attrs=_ctrl),
            "telefono": forms.TextInput(attrs=_ctrl),
            "direccion": forms.TextInput(attrs=_ctrl),
            "contrasena": forms.PasswordInput(attrs=_ctrl),
        }


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ["fecha", "usuario"]
        widgets = {
            "fecha": forms.DateInput(attrs={**_ctrl, "type": "date"}),
            "usuario": forms.Select(attrs=_sel),
        }


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ["producto", "cantidad_stock"]
        widgets = {
            "producto": forms.Select(attrs=_sel),
            "cantidad_stock": forms.NumberInput(attrs=_ctrl),
        }
