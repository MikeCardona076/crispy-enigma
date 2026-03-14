# Documentación de la API de GeoMike

Esta API proporciona endpoints para gestionar empleados y sus direcciones geográficas.

## Endpoints Disponibles

La API está disponible en la ruta base `/api-mike/`.

### Empleados

- **GET** `/api-mike/empleados/`: Lista todos los empleados
- **POST** `/api-mike/empleados/`: Crea un nuevo empleado
- **GET** `/api-mike/empleados/{id}/`: Obtiene detalles de un empleado específico
- **PUT** `/api-mike/empleados/{id}/`: Actualiza un empleado específico
- **PATCH** `/api-mike/empleados/{id}/`: Actualiza parcialmente un empleado específico
- **DELETE** `/api-mike/empleados/{id}/`: Elimina un empleado específico

### Direcciones

- **GET** `/api-mike/direcciones/`: Lista todas las direcciones
- **POST** `/api-mike/direcciones/`: Crea una nueva dirección
- **GET** `/api-mike/direcciones/{id}/`: Obtiene detalles de una dirección específica
- **PUT** `/api-mike/direcciones/{id}/`: Actualiza una dirección específica
- **PATCH** `/api-mike/direcciones/{id}/`: Actualiza parcialmente una dirección específica
- **DELETE** `/api-mike/direcciones/{id}/`: Elimina una dirección específica

## Modelos de Datos

### Empleado

```json
{
    "nombre_completo": "string",
    "puesto": "string",
    "fecha_registro": "datetime"
}
```

### Dirección

```json
{
    "empleado": "integer (ID del empleado)",
    "latitud": "string",
    "longitud": "string"
}
```

Nota: La dirección completa se genera automáticamente usando las coordenadas de latitud y longitud.

## Ejemplos de Uso

### Crear un Empleado

```bash
POST /api-mike/empleados/
Content-Type: application/json

{
    "nombre_completo": "Juan Pérez",
    "puesto": "Desarrollador"
}
```

### Crear una Dirección

```bash
POST /api-mike/direcciones/
Content-Type: application/json

{
    "empleado": 1,
    "latitud": "19.4326",
    "longitud": "-99.1332"
}
```

### Listar Empleados

```bash
GET /api-mike/empleados/
```

### Listar Direcciones

```bash
GET /api-mike/direcciones/
```

## Autenticación

La API utiliza autenticación de Django REST Framework. Para acceder a los endpoints, es necesario estar autenticado.

## Configuración

Asegúrate de que las aplicaciones `core_api` y `admin_geomike` estén incluidas en `INSTALLED_APPS` en `settings.py`.

Las rutas están configuradas en `core_api/urls.py` y `core_main_geomike/urls.py`.