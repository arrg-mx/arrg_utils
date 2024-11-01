# ARRG Utils Library (arrg_utils).

`arrg_utils` es un paquete de Python que proporciona utilidades para recopilar y gestionar diversa información del sistema. Permite obtener detalles sobre el uso de la CPU, el estado de la memoria, el uso del disco, las interfaces de red y la configuración del entorno. Este paquete es particularmente útil para monitorear el estado del sistema, generar instantáneas y obtener configuraciones del entorno ROS (Sistema Operativo para Robots), si corresponde.

## Características

- **Información del Sistema**: Recupera información del host, incluyendo el nombre y la dirección IP.
- **Monitoreo de Recursos**: Accede a detalles sobre el uso del disco, el estado de la RAM y el uso de la CPU.
- **Interfaces de Red**: Lista las interfaces de red disponibles con filtrado opcional.
- **Detección de Entorno ROS**: Identifica la versión, distribución y otras configuraciones de ROS.
- **Instantáneas del Sistema**: Genera instantáneas del estado actual del sistema para registro o monitoreo.

## Contenido

- [Instalación](#instalación)
- [Uso](#uso)
- [Módulos y Funciones](#módulos-y-funciones)
- [Ejemplos](#ejemplos)
- [Licencia](#licencia)

## Instalación

Clona el repositorio y navega a la carpeta `arrg_utils`:

```bash
git clone https://github.com/tu-usuario/arrg_utils.git
cd arrg_utils
```

Luego, instala el paquete utilizando `pip`:

```bash
pip install .
```

## Uso

Una vez instalado, puedes importar la clase `SysInfo` desde el paquete `arrg_utils` y usarla para recopilar información del sistema.

### Ejemplo Básico de Uso

```python
from arrg_utils import SysInfo

sys_info = SysInfo()
print(sys_info.get_system_report())
print(sys_info.get_system_snapshot())
```

Esto imprimirá un informe completo y una instantánea del estado actual del sistema.

## Módulos y Funciones

### Clase `SysInfo`

La clase `SysInfo` contiene métodos para obtener y gestionar información del sistema. A continuación, se describe cada método público:

- **`get_host_info()`**: Obtiene el nombre del host y la dirección IP del sistema.
- **`get_free_disk()`**: Devuelve detalles sobre el uso del disco en el directorio raíz, incluyendo espacio total, usado y disponible en GB.
- **`get_free_ram()`**: Recupera información de la RAM, como memoria total, usada, libre y disponible.
- **`get_system_date()`**: Proporciona la fecha y hora actuales del sistema.

- **`get_cpu_usage(compute_value_only=False)`**: Obtiene estadísticas de uso de la CPU, ya sea un informe completo (para cada núcleo de la CPU) o un porcentaje resumido.
- **`parse_network_interfaces(filtered=True, target_ip="")`**: Lista las interfaces de red disponibles. Soporta filtrado y objetivos por IP.
- **`get_ros_info()`**: Recupera detalles del entorno ROS (versión, distribución, ID de dominio y si es solo localhost). Devuelve `None` si ROS no está configurado.

- **`get_system_report()`**: Genera un informe completo que incluye información sobre el host, la CPU, la RAM, el disco, las interfaces de red y la configuración de ROS.

- **`get_system_snapshot()`**: Proporciona una instantánea con un resumen de CPU, RAM, uso de disco y detalles de la dirección IP, ideal para monitoreo periódico.

### Detalles de Implementación

Cada método utiliza internamente la función `_execute_command()` para ejecutar comandos de shell, asegurando un manejo de errores y procesamiento de salida consistente. Esto ayuda a gestionar las llamadas a comandos externos, como la obtención de uso de la CPU, estado de la RAM y otros datos del sistema, y hace que el paquete sea más resistente ante fallos en los comandos.

### Dependencias

El paquete depende de:

- Python 3.6 o superior
- Solo bibliotecas estándar (sin dependencias externas)

## Ejemplos

### Obtener Información del Host

```python
host_info = sys_info.get_host_info()
print("Nombre del host:", host_info["name"])
print("Dirección IP:", host_info["ip"])
```

### Obtener Información de Disco y RAM

```python
disk_info = sys_info.get_free_disk()
print("Tamaño total del disco:", disk_info["size"])
print("Espacio usado del disco:", disk_info["used"])
print("Espacio disponible del disco:", disk_info["available"])

ram_info = sys_info.get_free_ram()
print("RAM total:", ram_info["total"])
print("RAM usada:", ram_info["used"])
print("RAM libre:", ram_info["free"])
```

### Generar un Informe del Sistema

```python
report = sys_info.get_system_report()
print("Informe del sistema:", report)
```

### Analizar Interfaces de Red

```python
network_interfaces = sys_info.parse_network_interfaces()
for interface in network_interfaces:
    print(interface)
```

### Obtener Información de ROS

```python
ros_info = sys_info.get_ros_info()
if ros_info:
    print("Versión de ROS:", ros_info["version"])
else:
    print("Entorno ROS no configurado.")
```

## Licencia

Este proyecto está bajo la licencia MIT.

---

### Notas Adicionales

Siéntase libre de personalizar `arrg_utils` aún más para necesidades especializadas, como monitoreo extendido o agregar soporte para sistemas que no sean Linux, si es necesario.
