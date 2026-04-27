# DBIST

Proyecto Django para gestion de inventario, proveedores, productos, categorias, usuarios y facturas.

## Estructura

- `api_dbist/`: proyecto principal Django
- `api_dbist/inventario/`: aplicacion de inventario
- `api_dbist/mysite/`: configuracion global del proyecto

## Requisitos

- Python 3.10+
- Pip

## Instalacion

1. Crear y activar entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install django
```

## Ejecutar el proyecto

Desde la carpeta `api_dbist`:

```powershell
python manage.py migrate
python manage.py runserver
```

Abrir en navegador:

- http://127.0.0.1:8000/

## Comandos utiles

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

## Notas

- La base de datos local `db.sqlite3` esta ignorada en git.
- Si compartes el proyecto, crea un archivo `requirements.txt` con:

```powershell
pip freeze > requirements.txt
```
