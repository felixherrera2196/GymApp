# Preguntas para Levantamiento de Requerimientos - Gestión de Gimnasio

## Información General del Proyecto
1. ¿Cuál es el objetivo principal que el gimnasio quiere lograr con esta aplicación?
2. ¿Qué plataformas móviles se deben soportar para la aplicación (Android, iOS, ambos)?
3. ¿Habrá algún requisito de branding o lineamientos de diseño que deban aplicarse en las interfaces?
4. ¿Qué idiomas debe soportar la aplicación (solo español, multilingüe)?
5. ¿Se requiere integración con algún sistema existente del gimnasio?

## Gestión de Clientes
1. ¿Qué datos específicos se deben registrar de cada cliente (nombre, contacto, datos médicos, etc.)?
2. ¿Se necesita almacenar documentos o fotografías del cliente?
3. ¿Quiénes podrán crear, editar o eliminar registros de clientes?
4. ¿Se debe permitir que los clientes actualicen su información desde la aplicación móvil?
5. ¿Qué niveles de permisos se requieren para el personal administrativo?

## Membresías y Pagos
1. ¿Qué detalles deben registrarse al crear una membresía (tipo de plan, fecha de inicio, descuentos, etc.)?
2. ¿Cómo se registrará el pago de la membresía (efectivo, tarjeta, transferencia, otros)?
3. ¿Debe la aplicación manejar facturación o comprobantes de pago?
4. ¿Se requiere integración con pasarelas de pago en línea?
5. ¿Cómo se manejarán los recordatorios para vencimientos (notificaciones push, email, SMS)?
6. ¿Existe alguna política de prórroga o reactivación automática de membresías vencidas?

## Registro de Asistencia
1. ¿Cómo se verificará la identidad del cliente al presentar el código diario (solo código, documento adicional)?
2. ¿Por cuánto tiempo es válido el código único generado cada día?
3. ¿Qué sucede si un cliente no asiste en un día pero tiene una membresía activa?
4. ¿Se debe registrar el horario exacto de entrada y salida del cliente o solo la asistencia?
5. ¿Se requiere registrar asistencia manualmente en caso de contingencias?

## Funcionalidades del Backend (FastAPI) y Base de Datos (PostgreSQL)
1. ¿En qué horario se debe generar el código único diario y existe alguna lógica para regenerarlo si se filtra?
2. ¿Se necesita exponer APIs adicionales para integraciones con terceros?
3. ¿Qué políticas de seguridad y autenticación se requieren (JWT, OAuth, 2FA)?
4. ¿Qué volumen de usuarios y asistencias se estima para dimensionar la infraestructura?
5. ¿Hay requerimientos específicos de auditoría o registro de eventos?

## Frontend Móvil para Clientes
1. ¿Qué funcionalidades adicionales desea el cliente en la app móvil (ver historial de asistencias, renovar membresía, etc.)?
2. ¿Cómo se comunicará el código diario al cliente (push notification, pantalla de inicio, ambos)?
3. ¿Debe la app móvil funcionar sin conexión y sincronizar después?
4. ¿Se requieren métricas personales para el cliente (rutinas, progresos, etc.)?

## Frontend Web Administrativo
1. ¿Qué métricas y estadísticas son prioritarias para el administrador (asistencias diarias, ingresos, retención)?
2. ¿Se requiere un panel para filtrar y exportar datos (CSV, PDF)?
3. ¿Cuántos tipos de roles administrativos habrá (recepción, gerente, coach)?
4. ¿Qué tan detallados deben ser los reportes de asistencia y pagos?

## Notificaciones y Recordatorios
1. ¿Con cuánta anticipación se enviarán los recordatorios de vencimiento según cada tipo de membresía?
2. ¿Qué canales de comunicación se usarán para los recordatorios (correo, SMS, WhatsApp, push)?
3. ¿Se debe personalizar el contenido de los recordatorios por tipo de membresía o cliente?
4. ¿Se requiere registrar la confirmación de que un cliente recibió o leyó el recordatorio?

## Seguridad y Cumplimiento
1. ¿Existen políticas de protección de datos personales que deban cumplirse (ej. GDPR, leyes locales)?
2. ¿Se necesitan respaldos automáticos y con qué frecuencia?
3. ¿Qué nivel de disponibilidad y recuperación ante desastres se espera?

## Mantenimiento y Soporte
1. ¿Quién será responsable del soporte técnico y mantenimiento de la plataforma?
2. ¿Se requiere un sistema de tickets o canal de soporte integrado para reportar incidencias?
3. ¿Cuáles son los acuerdos de nivel de servicio (SLA) esperados?

## Cronograma y Presupuesto
1. ¿Cuál es la fecha objetivo para el lanzamiento de la plataforma?
2. ¿Hay un presupuesto definido para el desarrollo y mantenimiento?
3. ¿Se planean fases o entregas parciales del proyecto?

## Otros
1. ¿Hay requisitos legales específicos para la operación del gimnasio que deban reflejarse en la plataforma?
2. ¿Se requiere integración con dispositivos externos (torniquetes, lectores biométricos, etc.)?
3. ¿Existe algún requerimiento adicional que no se haya cubierto en las preguntas anteriores?
