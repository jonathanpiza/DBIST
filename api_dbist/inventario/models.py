from django.db import models


class Categoria(models.Model):
	codigo_cat = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=120)
	descripcion = models.TextField(blank=True)

	def __str__(self):
		return f"{self.codigo_cat} - {self.nombre}"


class Proveedor(models.Model):
	codigo_proveedor = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=120)
	servicio = models.CharField(max_length=120, blank=True)
	telefono = models.CharField(max_length=30, blank=True)
	correo_electronico = models.EmailField(blank=True)
	pagina_web = models.URLField(blank=True)

	def __str__(self):
		return f"{self.codigo_proveedor} - {self.nombre}"


class Producto(models.Model):
	codigo_produ = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=120)
	descripcion = models.TextField(blank=True)
	categoria = models.ForeignKey(
		Categoria,
		on_delete=models.PROTECT,
		related_name="productos",
	)
	proveedor = models.ForeignKey(
		Proveedor,
		on_delete=models.PROTECT,
		related_name="productos",
	)

	def __str__(self):
		return f"{self.codigo_produ} - {self.nombre}"


class Usuario(models.Model):
	nombre_propietario = models.CharField(max_length=120)
	apellido_propietario = models.CharField(max_length=120)
	correo_electronico = models.EmailField(unique=True)
	telefono = models.CharField(max_length=30, blank=True)
	direccion = models.CharField(max_length=255, blank=True)
	contrasena = models.CharField(max_length=128)

	def __str__(self):
		return f"{self.nombre_propietario} {self.apellido_propietario}"


class Factura(models.Model):
	codigo_fact = models.AutoField(primary_key=True)
	fecha = models.DateField()
	usuario = models.ForeignKey(
		Usuario,
		on_delete=models.PROTECT,
		related_name="facturas",
	)

	def __str__(self):
		return f"FAC-{self.codigo_fact} ({self.fecha})"


class FacturaDetalle(models.Model):
	factura = models.ForeignKey(
		Factura,
		on_delete=models.CASCADE,
		related_name="detalles",
	)
	producto = models.ForeignKey(
		Producto,
		on_delete=models.PROTECT,
		related_name="detalles_factura",
	)
	cantidad = models.PositiveIntegerField()
	valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		unique_together = ("factura", "producto")

	def __str__(self):
		return f"FAC-{self.factura_id} / {self.producto.codigo_produ}"


class Inventario(models.Model):
	cod_inv = models.AutoField(primary_key=True)
	producto = models.OneToOneField(
		Producto,
		on_delete=models.CASCADE,
		related_name="inventario",
	)
	cantidad_stock = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"INV-{self.cod_inv} / {self.producto.codigo_produ}"
