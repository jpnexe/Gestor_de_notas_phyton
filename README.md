# Gestor de Notas Python 📚

Proyecto de la materia **"Procesos Ágiles de Desarrollo de Software"** para dar solución a una actividad planteada por el profesor.

## 📋 Descripción

Sistema integral de gestión de notas estudiantiles que permite registrar estudiantes, ingresar calificaciones, calcular promedios y generar reportes. El proyecto está diseñado con una arquitectura modular y utiliza herramientas de automatización para simplificar el flujo de trabajo de versioning.

## 📁 Estructura del Proyecto

```
Gestor_de_notas_phyton/
├── main.py                  # Archivo principal del sistema de gestión de notas
├── commit_manager.py        # Script para automatizar commits y push a GitHub
├── README.md               # Documentación del proyecto (este archivo)
└── .git/                   # Repositorio Git local
```

### Descripción de Archivos

#### `main.py`
Contiene la funcionalidad principal del proyecto. En este archivo se centra toda la lógica del sistema con un menú interactivo que permite:
- Registrar estudiantes
- Ingresar notas
- Calcular promedios
- Generar reportes
- Guardar/cargar datos

#### `commit_manager.py`
Script automatizado para facilitar la gestión de commits en Git. Automatiza todo el proceso de versionado incluido push a GitHub.

## 🚀 Características Actuales

### Sistema Principal (`main.py`)
Sistema de gestión de notas completo y funcional con las siguientes características:

#### Menú Interactivo
```
1. Registrar Estudiante
2. Ingresar Notas
3. Calcular Promedio
4. Generar Reporte
5. Guardar y Salir
```

#### Funciones Implementadas

##### 1. **`registrar_estudiante(estudiantes)`**
- Permite registrar un nuevo estudiante
- Solicita: Nombre e ID del estudiante
- Crea estructura de datos con:
  - `nombre`: Nombre del estudiante
  - `id`: Identificador único
  - `notas`: Lista vacía para almacenar calificaciones
  - `promedio`: Promedio inicial en 0.0
  - `estado`: Estado inicial "N/A"
- **Ejemplo:**
  ```
  Nombre: Juan Pérez
  ID: EST001
  ✅ Estudiante Juan Pérez registrado.
  ```

##### 2. **`ingresar_notas(estudiantes)`**
- Permite agregar calificaciones a un estudiante
- Valida rango de notas: 0 a 5
- Manejo de errores:
  - Verifica si el estudiante existe
  - Valida que la entrada sea un número
  - Valida rango válido de notas
- **Ejemplo:**
  ```
  ID del estudiante: EST001
  Ingrese nota (0-5): 4.5
  ⭐ Nota agregada.
  ```

##### 3. **`calcular_promedio(estudiantes)`**
- Calcula automáticamente el promedio de cada estudiante
- Determina el estado académico:
  - **"Aprobado"** si promedio >= 3.0
  - **"Reprobado"** si promedio < 3.0
  - **"Sin notas"** si no tiene calificaciones
- Actualiza información en tiempo real

##### 4. **`generar_reporte(estudiantes)`**
- Muestra tabla formateada con toda la información
- Columnas:
  - ID
  - NOMBRE
  - PROMEDIO
  - ESTADO
- **Ejemplo de salida:**
  ```
  ============================================================
  ID         | NOMBRE               | PROMEDIO   | ESTADO    
  ============================================================
  EST001     | Juan Pérez           | 4.5        | Aprobado   
  EST002     | María García         | 2.8        | Reprobado  
  ============================================================
  ```

##### 5. **`guardar_datos(estudiantes)`**
- Guarda todos los datos en archivo `notas.json`
- Formato JSON con indentación de 4 espacios
- Preserva toda la información de estudiantes
- Se ejecuta al salir del programa

##### 6. **`cargar_datos()`**
- Carga datos del archivo `notas.json` al iniciar
- Retorna lista vacía si el archivo no existe
- Permite persistencia de datos entre sesiones

##### 7. **`main()`**
- Función principal que controla el flujo
- Carga datos al iniciar
- Bucle principal que:
  1. Muestra menú
  2. Solicita opción del usuario
  3. Ejecuta función correspondiente
  4. Repite hasta que el usuario seleccione salir
  5. Guarda datos antes de cerrar

### Gestor de Commits (`commit_manager.py`)
Automatización completa del proceso de versionado Git:

#### Funciones Implementadas

##### 1. **`ejecutar_comando(comando)`**
- Ejecuta comandos de terminal de forma segura
- Captura salida estándar y errores
- Retorna: (stdout, stderr, código_retorno)
- Compatible con Windows y Linux

##### 2. **`verificar_git_config()`**
- Verifica si Git está configurado (nombre y email)
- Si no está configurado:
  - Solicita nombre de usuario
  - Solicita email
  - Configura automáticamente Git
- Muestra confirmación de configuración

##### 3. **`mostrar_menu()`**
- Muestra banner de bienvenida
- Explica el propósito del script

##### 4. **`commit_estado_actual()`**
- Hace commit automático del estado actual
- Genera timestamp automático
- Formato: `[AUTO] Estado actual: YYYY-MM-DD HH:MM:SS`
- Manejo de errores si no hay cambios

##### 5. **`solicitar_mensaje_commit()`**
- Solicita mensaje descriptivo del commit
- Valida que no esté vacío
- Input simple de una línea

##### 6. **`hacer_commit_usuario(mensaje)`**
- Realiza commit con mensaje del usuario
- Valida mensaje no vacío
- Agrega todos los archivos con `git add .`
- Ejecuta commit con mensaje personalizado
- Manejo de errores robusto

##### 7. **`hacer_push()`**
- Ejecuta push automático a GitHub
- Rama destino: `main`
- Comunica éxito o error
- Sugerencia de comando manual si falla

##### 8. **`mostrar_ultimo_commit()`**
- Muestra información del último commit
- Datos mostrados:
  - Hash del commit
  - Autor
  - Email del autor
  - Fecha y hora
  - Mensaje del commit

##### 9. **`main()`**
- Orquesta todo el proceso:
  1. Muestra menú
  2. Verifica configuración Git
  3. Commit automático del estado
  4. Solicita mensaje
  5. Commit con mensaje del usuario
  6. Muestra información del commit
  7. Push automático a GitHub
  8. Confirmación final

## 💻 Cómo Usar

### Ejecutar el Sistema de Gestión de Notas
```bash
python main.py
```
Abre el menú interactivo donde podrás gestionar estudiantes y notas.

### Automatizar Commits y Push a GitHub
```bash
python commit_manager.py
```

**Flujo del script:**
1. Verifica la configuración de Git
2. Realiza commit automático del estado actual
3. Solicita el mensaje del commit
4. Realiza el commit con tu mensaje
5. Ejecuta push automático a GitHub
6. Muestra información del commit realizado

---

## 📊 Flujo de Datos y Lógica

### Estructura de Datos del Estudiante
```python
{
    "nombre": "Juan Pérez",
    "id": "EST001",
    "notas": [4.5, 3.8, 4.2],
    "promedio": 4.17,
    "estado": "Aprobado"
}
```

### Flujo Principal de la Aplicación

```
┌─────────────────────────────────┐
│   INICIA APLICACIÓN MAIN.PY     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  Cargar datos (notas.json)      │
│  Si no existe → lista vacía     │
└────────────┬────────────────────┘
             │
             ▼
       ┌─────────────┐
       │ MOSTRAR MENÚ│
       └────┬────────┘
            │
    ┌───────┼───────────────────────────────────┐
    │       │                                   │
    ▼       ▼       ▼       ▼       ▼         ▼
   [1]    [2]     [3]     [4]     [5]      Otro
    │      │       │       │       │         │
    ▼      ▼       ▼       ▼       ▼         ▼
 Registra Ingresa Calcula Genera Guardar  Error
 Estudiante Notas Promedio Reporte y Salir
    │      │       │       │       │
    └──────┴───────┴───────┴───────┴─► MENÚ
                                       (Repetir)
```

### Lógica de Cálculo de Promedio

```
Para cada estudiante:
  IF estudiante.notas está vacío:
    promedio = 0.0
    estado = "Sin notas"
  ELSE:
    promedio = suma(notas) / cantidad(notas)
    IF promedio >= 3.0:
      estado = "Aprobado"
    ELSE:
      estado = "Reprobado"
```

### Persistencia de Datos

```
INICIAR APP
    ↓
Intenta cargar notas.json
    ↓
    ├─ Si existe → Carga estudiantes
    └─ Si no existe → Lista vacía
    ↓
Usuario realiza operaciones
    ↓
Usuario selecciona "Guardar y Salir"
    ↓
Convierte lista en JSON
    ↓
Guarda en notas.json
    ↓
Cierra aplicación
```

### Flujo del Gestor de Commits

```
python commit_manager.py
        ↓
┌────────────────────────────┐
│ ¿Git configurado?          │
└────┬─────────────┬─────────┘
     │ No          │ Sí
     ▼             ▼
Solicita Configura
datos     automáticamente
     │             │
     └──────┬──────┘
            ▼
   ┌─────────────────────┐
   │ git add .           │
   │ Agregar cambios     │
   └──────────┬──────────┘
              ▼
   ┌─────────────────────────────────────┐
   │ Commit automático con timestamp     │
   │ [AUTO] Estado actual: YYYY-MM-DD... │
   └──────────┬──────────────────────────┘
              ▼
   ┌─────────────────────────┐
   │ Solicitar mensaje de    │
   │ commit al usuario       │
   └──────────┬──────────────┘
              ▼
   ┌──────────────────────────────┐
   │ Commit con mensaje del usuario│
   └──────────┬───────────────────┘
              ▼
   ┌──────────────────────────────┐
   │ git push origin main         │
   │ Enviar a GitHub             │
   └──────────┬───────────────────┘
              ▼
   ┌──────────────────────────────┐
   │ Mostrar info del commit      │
   │ ✓ Completado exitosamente   │
   └──────────────────────────────┘
```

### Validaciones Implementadas

#### En `ingresar_notas()`:
- ✓ Verifica que el estudiante exista
- ✓ Valida que la entrada sea numérica
- ✓ Valida rango 0 a 5
- ✓ Mensaje de error específico para cada caso

#### En `commit_manager.py`:
- ✓ Verifica configuración de Git
- ✓ Valida que el mensaje no esté vacío
- ✓ Detecta si no hay cambios para commitear
- ✓ Captura errores de conexión a GitHub

---

## 🗂️ Estructura de Archivos Generados

```
Gestor_de_notas_phyton/
├── main.py                  # Sistema de gestión
├── commit_manager.py        # Automatización Git
├── notas.json              # Base de datos (generado)
├── README.md               # Documentación
└── .git/                   # Repositorio Git
    ├── objects/
    ├── refs/
    ├── HEAD
    └── config
```

### Formato de `notas.json`
```json
[
    {
        "nombre": "Juan Pérez",
        "id": "EST001",
        "notas": [4.5, 3.8, 4.2],
        "promedio": 4.17,
        "estado": "Aprobado"
    },
    {
        "nombre": "María García",
        "id": "EST002",
        "notas": [2.5, 2.8],
        "promedio": 2.65,
        "estado": "Reprobado"
    }
]
```

## 🔧 Requisitos

- **Python 3.7+**
- **Git** instalado y configurado
- **Acceso a GitHub** con permisos en el repositorio

## 📝 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/jpnexe/Gestor_de_notas_phyton.git
```

2. Navegar al directorio:
```bash
cd Gestor_de_notas_phyton
```

3. Ejecutar el script:
```bash
python main.py
```

---

## 🎯 Sugerencias de Mejoras Futuras

### 📱 Funcionalidades Planeadas

#### 1. **Interfaz Gráfica (GUI)**
   - Implementar con `tkinter` (nativa en Python) o `PyQt5`
   - Hacer la aplicación más intuitiva y amigable
   - Dashboard con visualización en tiempo real
   - Tablas interactivas para edición de datos

#### 2. **Base de Datos Persistente**
   - Integrar **SQLite** para almacenamiento local
   - Opcionalmente PostgreSQL para escalabilidad
   - Migración automática de esquema
   - Consultas avanzadas de histórico

#### 3. **Sistema de Autenticación**
   - Login para profesores/administradores
   - Roles y permisos diferenciados
   - Auditoría y registro de cambios (quién hizo qué y cuándo)
   - Contraseñas encriptadas

#### 4. **Reportes Avanzados**
   - Exportar a **PDF** y **Excel**
   - Gráficas estadísticas (histogramas, distribuciones)
   - Análisis de desempeño estudiantil
   - Comparativas entre cursos/períodos
   - Generación automática de reportes

#### 5. **Validación Robusta**
   - Validación rigurosa de datos de entrada
   - Manejo comprehensivo de excepciones
   - Mensajes de error descriptivos y útiles
   - Restricciones de datos (rangos de notas, etc.)

#### 6. **Testing y Calidad**
   - Pruebas unitarias con `pytest`
   - Pruebas de integración
   - Cobertura de código al 80%+
   - CI/CD con GitHub Actions

#### 7. **API REST**
   - Crear API con `Flask` o `FastAPI`
   - Permitir acceso desde aplicaciones móviles/externas
   - Documentación interactiva con Swagger/OpenAPI
   - Autenticación JWT

#### 8. **Sincronización en la Nube**
   - Integración con servicios cloud (Firebase, AWS S3)
   - Backup automático de datos
   - Acceso desde múltiples dispositivos
   - Sincronización en tiempo real

#### 9. **Optimización de Rendimiento**
   - Caché para consultas frecuentes
   - Indexación de datos
   - Paginación de resultados
   - Optimización de algoritmos

#### 10. **Documentación Mejorada**
   - Docstrings detallados en todas las funciones
   - Ejemplos de uso en la documentación
   - Guía de contribución para desarrolladores
   - Comentarios explicativos en código complejo

### 🛠️ Mejoras Técnicas

- Implementar **logging completo** con módulo `logging`
- Configuración externa con archivos `config.ini` o `.env`
- Arquitectura escalable (estructura de carpetas mejorada)
- Patrón **MVC** o arquitectura limpia
- Manejo de errores con tipos de excepciones personalizadas
- Type hints en todas las funciones
- Validación de entrada con librerías como `pydantic`

### 🔐 Seguridad

- Validación de entrada para prevenir inyecciones
- Encriptación de datos sensibles
- HTTPS para comunicación API
- Protección contra CSRF y XSS

---

## 📈 Hoja de Ruta (Roadmap)

| Fase | Objetivos | Estado |
|------|-----------|--------|
| **Fase 1** | Funcionalidad base completa | ✅ En Progreso |
| **Fase 2** | Base de datos + GUI básica | ⏳ Planeado |
| **Fase 3** | Autenticación + Reportes avanzados | ⏳ Planeado |
| **Fase 4** | API REST + Testing | ⏳ Planeado |
| **Fase 5** | Cloud sync + Optimización | ⏳ Futuro |

---

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 👨‍💻 Autor
**jpnexe** - Desarrollador Principal

## 📅 Última actualización
Mayo 2026

## 📄 Licencia
Proyecto educativo - Libre para uso en propósitos académicos

---

**Nota:** Este proyecto está en desarrollo continuo. Las sugerencias futuras se irán implementando según la evolución del curso y los requisitos del proyecto.
