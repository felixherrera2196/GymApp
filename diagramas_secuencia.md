# Diagramas de Secuencia - Plataforma de Gestión de Gimnasio

A continuación se describen los principales diagramas de secuencia del sistema en formato **Mermaid**, alineados con los casos de uso definidos para la plataforma.

## UC-01 Gestionar registro de cliente
```mermaid
sequenceDiagram
    actor Administrador
    participant Panel as Panel administrativo
    participant Backend
    participant DB as Base de datos
    participant S3 as Almacenamiento S3

    Administrador->>Panel: Abrir módulo de clientes
    Panel->>Administrador: Solicitar datos obligatorios
    Administrador->>Panel: Capturar datos y adjuntar fotografía
    Panel->>Backend: Enviar solicitud de registro
    Backend->>DB: Guardar datos del cliente
    Backend->>S3: Almacenar fotografía de perfil
    alt Carga de fotografía exitosa
        S3-->>Backend: Confirmación de carga
        Backend->>DB: Registrar auditoría del alta
        DB-->>Backend: Confirmación de guardado
        Backend-->>Panel: Cliente creado correctamente
        Panel-->>Administrador: Mostrar cliente en listado
    else Error al cargar fotografía
        S3-->>Backend: Notificación de error
        Backend-->>Panel: Informar falla y permitir reintento
    end
    opt Información obligatoria incompleta
        Panel-->>Administrador: Solicitar completar campos faltantes
    end
```

## UC-02 Actualizar perfil desde la aplicación móvil
```mermaid
sequenceDiagram
    actor Cliente
    participant App as App móvil
    participant Backend
    participant DB as Base de datos

    Cliente->>App: Abrir "Mi perfil"
    App-->>Cliente: Mostrar datos actuales
    Cliente->>App: Modificar información y guardar cambios
    App->>Backend: Enviar actualización del perfil
    Backend->>DB: Actualizar datos del cliente
    Backend->>DB: Registrar auditoría de modificación
    DB-->>Backend: Confirmaciones de guardado
    Backend-->>App: Confirmar actualización exitosa
    App-->>Cliente: Mostrar mensaje de éxito
    opt Pérdida de conexión
        App-->>Cliente: Mostrar error y ofrecer reintento
    end
    opt Campo restringido
        App-->>Cliente: Indicar que contacte al administrador
    end
```

## UC-03 Gestionar membresías y pagos manuales
```mermaid
sequenceDiagram
    actor Administrador
    participant Panel as Panel administrativo
    participant Backend
    participant DB as Base de datos

    Administrador->>Panel: Abrir módulo de membresías
    Panel-->>Administrador: Listar membresías y estatus
    Administrador->>Panel: Crear o editar membresía
    Panel->>Backend: Enviar configuración del plan
    Backend->>DB: Guardar o actualizar membresía
    Administrador->>Panel: Indicar forma de pago y marcar completado
    Panel->>Backend: Registrar pago manual
    Backend->>DB: Actualizar estatus de pago y auditoría
    DB-->>Backend: Confirmación de actualización
    Backend-->>Panel: Notificar membresía actualizada
    Panel-->>Administrador: Mostrar confirmación
    opt Fechas superpuestas
        Panel-->>Administrador: Alertar y solicitar ajustar vigencia
    end
    opt Pago no marcado como completado
        Panel-->>Administrador: Recordatorio de estatus pendiente
    end
```

## UC-04 Pagar membresía con tarjeta desde la app
```mermaid
sequenceDiagram
    actor Cliente
    participant App as App móvil
    participant Backend
    participant Stripe
    participant DB as Base de datos

    Cliente->>App: Seleccionar plan de membresía
    App-->>Cliente: Mostrar detalle y monto
    Cliente->>App: Elegir "Pagar con tarjeta"
    App->>Stripe: Iniciar flujo de pago seguro
    Stripe->>Cliente: Solicitar datos de tarjeta
    Cliente->>Stripe: Proporcionar información de pago
    Stripe->>Backend: Enviar resultado del procesamiento
    alt Pago aprobado
        Backend->>DB: Actualizar estatus de membresía
        Backend->>DB: Registrar auditoría del pago
        DB-->>Backend: Confirmaciones de guardado
        Backend-->>App: Notificar pago aprobado
        App-->>Cliente: Mostrar confirmación y enviar comprobante
    else Pago rechazado
        Backend-->>App: Informar rechazo y motivo
        App-->>Cliente: Mostrar mensaje y permitir reintento
    end
    opt Cliente cancela el flujo
        App-->>Cliente: Regresar a la selección de planes
    end
```

## UC-05 Registrar asistencia mediante código QR
```mermaid
sequenceDiagram
    actor Recepcionista
    participant Panel as Panel administrativo
    participant Backend
    participant DB as Base de datos

    Recepcionista->>Panel: Abrir módulo de asistencia
    Panel-->>Recepcionista: Habilitar escáner QR
    Recepcionista->>Panel: Escanear código del cliente
    Panel->>Backend: Enviar código para validación
    Backend->>DB: Verificar código, cliente y membresía
    DB-->>Backend: Respuesta de validación
    alt Código válido y membresía activa
        Backend->>DB: Registrar asistencia con fecha/hora
        DB-->>Backend: Confirmación de registro
        Backend-->>Panel: Confirmar asistencia exitosa
        Panel-->>Recepcionista: Mostrar confirmación
    else Código inválido o membresía inactiva
        Backend-->>Panel: Notificar error correspondiente
        Panel-->>Recepcionista: Informar situación y acciones
    end
    opt Cámara inhabilitada
        Recepcionista->>Panel: Solicitar registro manual
        Panel->>Backend: Registrar asistencia manual
    end
```

## UC-06 Configurar branding y diccionarios
```mermaid
sequenceDiagram
    actor Administrador
    participant Panel as Panel administrativo
    participant Backend
    participant S3 as Almacenamiento S3
    participant DB as Base de datos

    Administrador->>Panel: Abrir configuración general
    Panel-->>Administrador: Mostrar branding y diccionarios
    Administrador->>Panel: Cargar logos, imágenes y colores
    Panel->>S3: Subir recursos visuales
    S3-->>Panel: Confirmación de carga
    Administrador->>Panel: Editar textos multilingües
    Panel->>Backend: Enviar configuraciones y diccionarios
    Backend->>DB: Guardar ajustes y traducciones
    DB-->>Backend: Confirmación de guardado
    Backend-->>Panel: Confirmar actualización global
    Panel-->>Administrador: Mostrar mensaje de éxito
    opt Recurso supera tamaño permitido
        S3-->>Panel: Notificar error de carga
        Panel-->>Administrador: Solicitar nuevo recurso
    end
    opt Traducción faltante
        Panel-->>Administrador: Impedir guardado hasta completar
    end
```

## UC-07 Consultar métricas y exportar reportes
```mermaid
sequenceDiagram
    actor Administrador
    participant Panel as Panel administrativo
    participant Backend
    participant DB as Base de datos
    participant CSV as Servicio de exportación CSV

    Administrador->>Panel: Acceder a panel de métricas
    Panel->>Backend: Solicitar métricas disponibles
    Backend->>DB: Obtener datos de asistencia, ingresos y membresías
    DB-->>Backend: Entregar datos agregados
    Backend-->>Panel: Enviar gráficos y tablas
    Panel-->>Administrador: Mostrar métricas
    Administrador->>Panel: Aplicar filtros de hora/día/mes
    Panel->>Backend: Solicitar datos filtrados
    Backend->>DB: Consultar información con filtros
    DB-->>Backend: Resultados filtrados
    Backend-->>Panel: Actualizar visualizaciones
    Administrador->>Panel: Solicitar exportar CSV
    Panel->>CSV: Generar archivo con datos filtrados
    CSV-->>Panel: Entregar archivo CSV
    Panel-->>Administrador: Descargar reporte
    opt Sin datos o error en exportación
        Backend-->>Panel: Notificar ausencia de resultados o fallo
        Panel-->>Administrador: Mostrar mensaje y permitir reintento
    end
```
