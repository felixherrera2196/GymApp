# Levantamiento de Requerimientos - Gestión de Gimnasio

## Información General del Proyecto

**¿Cuál es el objetivo principal que el gimnasio quiere lograr con esta aplicación?**

El objetivo principal es gestionar las membresías de los clientes y llevar control de su asistencia.

**¿Qué plataformas móviles se deben soportar para la aplicación (Android, iOS, ambos)?**

La aplicación móvil se desarrollará en Flutter para ser compatible con Android e iOS. Además, se contempla una versión web móvil en el futuro.

**¿Habrá algún requisito de branding o lineamientos de diseño que deban aplicarse en las interfaces?**

El branding será configurable desde el panel de administración, permitiendo gestionar logos, imágenes y cinco colores tanto para el panel como para la app móvil. Inicialmente se utilizará el logo principal y esos cinco colores personalizables.

**¿Qué idiomas debe soportar la aplicación (solo español, multilingüe)?**

La aplicación será multilingüe con diccionarios administrables desde el panel; por ahora se manejarán español e inglés.

**¿Se requiere integración con algún sistema existente del gimnasio?**

Actualmente no se requiere integración con sistemas externos del gimnasio.

## Gestión de Clientes

**¿Qué datos específicos se deben registrar de cada cliente (nombre, contacto, datos médicos, etc.)?**

Se registrarán: nombre, apellido paterno, apellido materno, teléfono, correo electrónico, dirección, fecha de nacimiento, datos del contacto de emergencia (nombre, apellido paterno, apellido materno, teléfono) e imagen de perfil.

**¿Se necesita almacenar documentos o fotografías del cliente?**

Solo se almacenará la foto de perfil, prevista en un bucket S3 de AWS.

**¿Quiénes podrán crear, editar o eliminar registros de clientes?**

Únicamente el administrador podrá agregar, editar, ver y eliminar registros desde el panel administrativo. Los clientes pueden registrarse, pero el administrador controla el estatus de sus membresías.

**¿Se debe permitir que los clientes actualicen su información desde la aplicación móvil?**

Sí, los clientes podrán actualizar los datos de su registro.

**¿Qué niveles de permisos se requieren para el personal administrativo?**

El rol de administrador tendrá permisos totales.

## Membresías y Pagos

**¿Qué detalles deben registrarse al crear una membresía (tipo de plan, fecha de inicio, descuentos, etc.)?**

Se registrará el tipo de plan y la duración solicitada, ya que el precio varía según la cantidad de días. Los planes contemplados son: diario, semanal, quincenal, mensual, bimestral, semestral y anual. Por ahora no se manejan descuentos.

**¿Cómo se registrará el pago de la membresía (efectivo, tarjeta, transferencia, otros)?**

Se admitirán pagos en efectivo o transferencia, marcados manualmente como pagados desde el panel, y pagos con tarjeta desde la app que actualizarán automáticamente el estatus de la membresía.

**¿Debe la aplicación manejar facturación o comprobantes de pago?**

Por el momento no es necesario manejar facturación ni comprobantes.

**¿Se requiere integración con pasarelas de pago en línea?**

Sí, se integrará con Stripe para pagos con tarjeta; el flujo en efectivo no requiere integración.

**¿Cómo se manejarán los recordatorios para vencimientos (notificaciones push, email, SMS)?**

Se enviarán recordatorios mediante notificaciones push y correo electrónico.

**¿Existe alguna política de prórroga o reactivación automática de membresías vencidas?**

No hay políticas de prórroga o reactivación automática actualmente.

## Registro de Asistencia

**¿Cómo se verificará la identidad del cliente al presentar el código diario (solo código, documento adicional)?**

El backend generará un código diario cada 24 horas. La app móvil generará un QR combinando ese código y el ID del cliente; el panel administrativo leerá el QR y consultará al backend para validar el código y registrar la asistencia.

**¿Por cuánto tiempo es válido el código único generado cada día?**

El código es válido por 24 horas y se renueva a las 00:00 horas.

**¿Qué sucede si un cliente no asiste en un día pero tiene una membresía activa?**

No ocurre nada adicional; en el historial se reflejará la ausencia. Se planea implementar un sistema de rachas configurable similar a Duolingo para motivar la asistencia.

**¿Se debe registrar el horario exacto de entrada y salida del cliente o solo la asistencia?**

Se registrará únicamente la hora de entrada.

**¿Se requiere registrar asistencia manualmente en caso de contingencias?**

Sí, el administrador podrá registrar asistencias manualmente desde el panel.

## Funcionalidades del Backend (FastAPI) y Base de Datos (PostgreSQL)

**¿En qué horario se debe generar el código único diario y existe alguna lógica para regenerarlo si se filtra?**

El código se genera a las 00:00 horas y el panel debe ofrecer un botón para solicitar al backend regenerarlo cuando sea necesario.

**¿Se necesita exponer APIs adicionales para integraciones con terceros?**

No se han definido integraciones adicionales por ahora.

**¿Qué políticas de seguridad y autenticación se requieren (JWT, OAuth, 2FA)?**

Se utilizará autenticación basada en JWT.

**¿Qué volumen de usuarios y asistencias se estima para dimensionar la infraestructura?**

Se estima un máximo de 200 usuarios por día y hasta 20 usuarios concurrentes.

## Frontend Móvil para Clientes

**¿Qué funcionalidades adicionales desea el cliente en la app móvil (ver historial de asistencias, renovar membresía, etc.)?**

Los clientes podrán registrarse, iniciar sesión, editar sus datos, consultar su historial de asistencias y pagar su membresía.

**¿Cómo se comunicará el código diario al cliente (push notification, pantalla de inicio, ambos)?**

Se mostrará tanto mediante notificaciones push como en la pantalla principal.

**¿Debe la app móvil funcionar sin conexión y sincronizar después?**

No, la app requerirá conexión permanente.

**¿Se requieren métricas personales para el cliente (rutinas, progresos, etc.)?**

Se plantea un checklist diario para que el cliente marque el avance de su rutina.

## Frontend Web Administrativo

**¿Qué métricas y estadísticas son prioritarias para el administrador (asistencias diarias, ingresos, retención)?**

Se priorizarán métricas de asistencias e ingresos con filtros por hora, día y mes, además de usuarios con membresías activas o inactivas y la cantidad de asistentes con membresías activas.

**¿Se requiere un panel para filtrar y exportar datos (CSV, PDF)?**

Sí, con opción de exportar a CSV.

**¿Cuántos tipos de roles administrativos habrá (recepción, gerente, coach)?**

Habrá roles de Administrador y Recepcionista.

**¿Qué tan detallados deben ser los reportes de asistencia y pagos?**

Serán reportes sencillos basados en los filtros de rango de fechas seleccionados.

## Notificaciones y Recordatorios

**¿Con cuánta anticipación se enviarán los recordatorios de vencimiento según cada tipo de membresía?**

La anticipación será configurable según la membresía activa, ajustable desde el panel administrativo.

**¿Qué canales de comunicación se usarán para los recordatorios (correo, SMS, WhatsApp, push)?**

Se emplearán correos electrónicos y notificaciones push.

**¿Se debe personalizar el contenido de los recordatorios por tipo de membresía o cliente?**

Sí, el contenido será personalizable.

**¿Se requiere registrar la confirmación de que un cliente recibió o leyó el recordatorio?**

No es necesario registrar confirmaciones de lectura.

## Seguridad y Cumplimiento

**¿Existen políticas de protección de datos personales que deban cumplirse (ej. GDPR, leyes locales)?**

Por ahora no se han definido políticas específicas.

**¿Se necesitan respaldos automáticos y con qué frecuencia?**

No se han requerido respaldos automáticos.

**¿Qué nivel de disponibilidad y recuperación ante desastres se espera?**

No hay expectativas especiales de disponibilidad ni de recuperación ante desastres en esta fase.

## Mantenimiento y Soporte

**¿Quién será responsable del soporte técnico y mantenimiento de la plataforma?**

No se ha asignado un responsable de soporte o mantenimiento.

**¿Se requiere un sistema de tickets o canal de soporte integrado para reportar incidencias?**

No se necesita por ahora, aunque podría considerarse en una segunda versión.

**¿Cuáles son los acuerdos de nivel de servicio (SLA) esperados?**

No se han definido SLA en este momento.

## Cronograma y Presupuesto

**¿Cuál es la fecha objetivo para el lanzamiento de la plataforma?**

El backend debe completarse en dos meses; el frontend se entregará progresivamente conforme el backend esté listo.

**¿Hay un presupuesto definido para el desarrollo y mantenimiento?**

Sí, el presupuesto ya fue negociado.

**¿Se planean fases o entregas parciales del proyecto?**

Sí, se realizarán entregas incrementales hasta completar todos los requerimientos.
