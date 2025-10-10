# Endpoints por entregable

A continuación se listan los endpoints REST propuestos para el backend de GymApp, organizados en entregables incrementales. Cada grupo describe el objetivo funcional del bloque y los recursos involucrados.

## Entregable 1: Autenticación y gestión básica de usuarios administrativos
Este entregable habilita la infraestructura mínima de seguridad para que administradores y recepcionistas puedan acceder al panel, manteniendo los roles diferenciados.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/login` | Autentica a un usuario administrativo y entrega el JWT de sesión. |
| POST | `/auth/refresh` | Renueva el token JWT antes de su expiración. |
| POST | `/auth/logout` | Invalida el token activo (lista negra o rotación). |
| GET | `/auth/me` | Devuelve la información del usuario autenticado y sus roles. |
| GET | `/admin/users` | Lista usuarios administrativos con filtros por rol y estado. |
| POST | `/admin/users` | Crea un usuario administrativo (solo rol administrador). |
| PATCH | `/admin/users/{user_id}` | Actualiza datos y rol de un usuario administrativo. |
| DELETE | `/admin/users/{user_id}` | Realiza borrado lógico de un usuario administrativo. |

## Entregable 2: Gestión de clientes y perfiles
Establece los recursos para registrar clientes, almacenar su información completa y permitir que cada uno administre su perfil desde la aplicación móvil.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/clients` | Lista clientes con filtros por estatus de membresía y fecha de alta. |
| POST | `/clients` | Registra un nuevo cliente con datos personales y contacto de emergencia. |
| GET | `/clients/{client_id}` | Obtiene el detalle de un cliente específico. |
| PATCH | `/clients/{client_id}` | Actualiza información del cliente (incluida foto de perfil). |
| DELETE | `/clients/{client_id}` | Ejecuta borrado lógico del registro del cliente. |
| GET | `/clients/{client_id}/profile` | Devuelve el perfil para consumo de la app móvil. |
| PUT | `/clients/{client_id}/profile` | Permite al cliente actualizar sus datos personales desde la app. |
| POST | `/clients/{client_id}/avatar` | Sube o reemplaza la fotografía de perfil en S3. |

## Entregable 3: Membresías, planes y pagos
Cubre la administración de planes de membresía, asignaciones a clientes y procesamiento de pagos tanto manuales como por Stripe.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/plans` | Lista los planes disponibles (diario, semanal, etc.) y sus parámetros. |
| POST | `/plans` | Crea o actualiza definiciones de planes personalizados. |
| PATCH | `/plans/{plan_id}` | Modifica atributos de un plan existente. |
| DELETE | `/plans/{plan_id}` | Desactiva un plan para futuras ventas. |
| GET | `/clients/{client_id}/memberships` | Consulta las membresías del cliente y su estatus. |
| POST | `/clients/{client_id}/memberships` | Asigna una nueva membresía al cliente con vigencia. |
| PATCH | `/memberships/{membership_id}` | Actualiza fechas o estado de una membresía existente. |
| GET | `/memberships/{membership_id}/payments` | Lista los pagos asociados a la membresía. |
| POST | `/memberships/{membership_id}/payments/manual` | Registra pago manual (efectivo/transferencia) y marca como liquidado. |
| POST | `/memberships/{membership_id}/payments/stripe-intent` | Crea intent de pago con Stripe para la app móvil. |
| POST | `/payments/stripe/webhook` | Recibe notificaciones de Stripe y actualiza la membresía. |

## Entregable 4: Control de asistencia y códigos diarios
Implementa la lógica de generación y validación de códigos diarios, lectura de QR y registro de asistencia tanto automática como manual.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/attendance/daily-code` | Devuelve el código vigente para su uso en la app móvil. |
| POST | `/attendance/daily-code/regenerate` | Fuerza la regeneración manual del código diario. |
| POST | `/attendance/validate` | Recibe el código QR escaneado y valida membresía/código. |
| POST | `/attendance/manual` | Registra asistencia manual por parte del administrador. |
| GET | `/attendance/logs` | Lista asistencias con filtros por fecha, estatus y cliente. |
| GET | `/clients/{client_id}/attendance` | Permite al cliente consultar su historial de asistencias. |

## Entregable 5: Configuración, notificaciones y métricas
Reúne las capacidades transversales para personalizar la marca, administrar diccionarios multilingües, configurar recordatorios y exponer métricas con exportación.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/settings/branding` | Obtiene la configuración actual de branding y recursos gráficos. |
| PUT | `/settings/branding` | Actualiza logos, paleta de colores e imágenes (carga a S3). |
| GET | `/settings/dictionaries` | Lista los diccionarios disponibles por idioma. |
| PUT | `/settings/dictionaries/{locale}` | Actualiza las traducciones de un idioma. |
| GET | `/notifications/reminders` | Consulta la configuración de recordatorios por tipo de membresía. |
| PUT | `/notifications/reminders` | Ajusta la anticipación y contenido de los recordatorios. |
| POST | `/notifications/test` | Envía un recordatorio de prueba para validar plantillas. |
| GET | `/metrics/overview` | Devuelve métricas agregadas de asistencias, ingresos y membresías. |
| GET | `/metrics/overview/export` | Genera un CSV con los datos filtrados solicitados. |
| GET | `/clients/{client_id}/checklist` | Recupera el checklist diario del cliente. |
| PUT | `/clients/{client_id}/checklist` | Actualiza el progreso diario del checklist. |

