# Requerimientos Funcionales - Plataforma de Gestión de Gimnasio

## 1. Información General
- RF-1.1 La plataforma debe permitir gestionar las membresías y control de asistencia de los clientes del gimnasio.
- RF-1.2 El panel administrativo debe permitir configurar el branding (logo, imágenes y cinco colores) utilizado tanto en la app móvil como en el panel web.
- RF-1.3 El sistema debe soportar múltiples idiomas, iniciando con español e inglés, con diccionarios administrables desde el panel.

## 2. Gestión de Clientes
- RF-2.1 El sistema debe registrar para cada cliente: nombre, apellidos, teléfono, correo electrónico, dirección, fecha de nacimiento e información de contacto de emergencia.
- RF-2.2 La plataforma debe permitir almacenar una fotografía de perfil del cliente en un bucket S3.
- RF-2.3 El administrador debe poder crear, editar, visualizar y eliminar (lógico) registros de clientes desde el panel administrativo.
- RF-2.4 Los clientes deben poder registrarse y actualizar sus datos personales desde la aplicación móvil.
- RF-2.5 El sistema debe restringir los permisos administrativos a los roles definidos (Administrador y Recepcionista), otorgando control total al administrador.

## 3. Membresías y Pagos
- RF-3.1 La plataforma debe permitir crear membresías especificando tipo de plan y duración (diario, semanal, quincenal, mensual, bimestral, semestral y anual).
- RF-3.2 El panel debe permitir marcar manualmente los pagos en efectivo o transferencia como pagados.
- RF-3.3 La app móvil debe permitir realizar pagos con tarjeta mediante la integración con Stripe y actualizar automáticamente el estatus de la membresía.
- RF-3.4 El sistema debe enviar recordatorios de vencimiento mediante notificaciones push y correo electrónico, con anticipación configurable por tipo de membresía.
- RF-3.5 El administrador debe poder consultar el historial de pagos y membresías activas/inactivas.

## 4. Registro de Asistencia
- RF-4.1 El backend debe generar un código único diario para todos los clientes a las 00:00 horas.
- RF-4.2 La aplicación móvil debe generar un código QR que combine el código diario con el ID del cliente para validar asistencias.
- RF-4.3 El panel administrativo debe permitir escanear el QR y consultar al backend para validar y registrar la asistencia.
- RF-4.4 El sistema debe registrar la hora de entrada del cliente cuando se valida la asistencia.
- RF-4.5 El administrador debe poder registrar asistencias manualmente desde el panel en caso de contingencias.
- RF-4.6 El panel debe ofrecer un botón para regenerar el código diario cuando sea necesario.

## 5. Backend y Base de Datos
- RF-5.1 El backend debe exponer APIs para la gestión de clientes, membresías, pagos, asistencia, recordatorios y configuración de branding.
- RF-5.2 El sistema debe almacenar auditorías registrando fecha, hora y usuario responsable de cada alta, modificación o eliminación, y conservar los registros mediante borrado lógico.

## 6. Aplicación Móvil (Clientes)
- RF-6.1 La app móvil debe permitir a los clientes registrarse, iniciar sesión y actualizar sus datos.
- RF-6.2 La app debe mostrar el código diario del cliente en la pantalla principal y mediante notificaciones push.
- RF-6.3 Los clientes deben poder consultar su historial de asistencias desde la app.
- RF-6.4 La app debe permitir pagar membresías con tarjeta a través de Stripe.
- RF-6.5 La app debe ofrecer un checklist diario para que el cliente marque el avance de su rutina.

## 7. Panel Web Administrativo
- RF-7.1 El panel debe permitir visualizar métricas de asistencia e ingresos con filtros por hora, día y mes.
- RF-7.2 El panel debe mostrar la cantidad de usuarios con membresías activas e inactivas.
- RF-7.3 El sistema debe permitir exportar datos filtrados a archivos CSV.
- RF-7.4 El panel debe permitir la gestión de roles de Administrador y Recepcionista.
- RF-7.5 El panel debe generar reportes de asistencia y pagos basados en rangos de fechas seleccionados.

## 8. Notificaciones y Recordatorios
- RF-8.1 El sistema debe permitir configurar el contenido de los recordatorios según tipo de membresía o cliente.
- RF-8.2 El sistema debe enviar recordatorios mediante correo electrónico y notificaciones push sin requerir confirmación de lectura.

## 9. Cronograma y Entregas
- RF-9.1 El backend debe completarse en un plazo máximo de dos meses.
- RF-9.2 El proyecto debe contemplar entregas incrementales del frontend conforme las funcionalidades del backend estén disponibles.

## 10. Alcances y Exclusiones
- RF-10.1 En esta fase no se requiere facturación, comprobantes de pago ni integración con sistemas externos adicionales.
- RF-10.2 No se implementarán políticas de prórroga o reactivación automática de membresías vencidas.
