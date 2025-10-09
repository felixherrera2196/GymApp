# Historias de Usuario - Plataforma de Gestión de Gimnasio

## HU-01 Registrar clientes desde el panel administrativo
- **Como** administrador del gimnasio
- **Quiero** capturar la información completa de un nuevo cliente y su contacto de emergencia
- **Para** mantener un registro actualizado que permita gestionar membresías y asistencia
- **Criterios de aceptación:**
  - Dado que accedo al módulo de clientes, cuando completo los datos obligatorios del cliente y guardo, entonces el sistema debe almacenar la información y mostrar al cliente en el listado general. (RF-2.1, RF-2.3)
  - Dado que adjunto una fotografía válida, cuando confirmo el registro, entonces el sistema debe almacenarla en el repositorio definido y asociarla al cliente. (RF-2.2)
  - Dado que omito un campo obligatorio, cuando intento guardar, entonces el sistema debe indicar los campos faltantes y evitar el registro hasta completarlos. (RF-2.3)

## HU-02 Actualizar perfil personal desde la app móvil
- **Como** cliente del gimnasio
- **Quiero** modificar mis datos personales y de contacto desde la aplicación móvil
- **Para** asegurar que la información del gimnasio esté siempre vigente
- **Criterios de aceptación:**
  - Dado que inicio sesión en la app, cuando abro la sección "Mi perfil", entonces debo visualizar mis datos actuales para editarlos. (RF-6.1)
  - Dado que actualizo mis datos y guardo los cambios, cuando la operación sea exitosa, entonces debo recibir una confirmación y la información debe quedar sincronizada en el backend. (RF-2.4, RF-6.1)
  - Dado que pierdo conexión durante la actualización, cuando el sistema no pueda guardar los cambios, entonces debe informarme del error y permitirme reintentar. (UC-02)

## HU-03 Gestionar membresías y pagos manuales
- **Como** administrador del gimnasio
- **Quiero** asignar planes de membresía y registrar pagos en efectivo o transferencia
- **Para** mantener actualizado el estatus de pago de cada cliente
- **Criterios de aceptación:**
  - Dado que selecciono un cliente, cuando elijo un tipo de plan y duración, entonces el sistema debe crear o actualizar la membresía con esas condiciones. (RF-3.1)
  - Dado que recibo un pago en efectivo o transferencia, cuando lo marco como completado, entonces el estatus de la membresía debe reflejarse como pagado. (RF-3.2)
  - Dado que existe un solapamiento de fechas, cuando intento guardar, entonces el sistema debe alertarme y solicitar ajustes antes de confirmar. (UC-03)

## HU-04 Pagar membresía con tarjeta desde la app
- **Como** cliente del gimnasio
- **Quiero** completar el pago de mi membresía mediante tarjeta dentro de la aplicación móvil
- **Para** renovar mi acceso sin depender de pagos presenciales
- **Criterios de aceptación:**
  - Dado que tengo una membresía pendiente por pagar, cuando elijo la opción de pagar con tarjeta, entonces debo ser dirigido al flujo seguro de Stripe. (RF-3.3, RF-6.4)
  - Dado que Stripe confirma el pago, cuando se procese correctamente, entonces el sistema debe actualizar el estatus de mi membresía y enviar la confirmación correspondiente. (RF-3.3)
  - Dado que el pago es rechazado, cuando Stripe devuelva un error, entonces la app debe notificarme el motivo y permitir reintentar o elegir otro método. (UC-04)

## HU-05 Registrar asistencia escaneando código QR
- **Como** recepcionista del gimnasio
- **Quiero** escanear el código QR de los clientes para registrar su asistencia diaria
- **Para** llevar un control rápido y preciso de los ingresos al gimnasio
- **Criterios de aceptación:**
  - Dado que el cliente presenta su QR vigente, cuando lo escaneo desde el panel, entonces el sistema debe validar el código diario y registrar la hora de entrada. (RF-4.1, RF-4.2, RF-4.3, RF-4.4)
  - Dado que el cliente no tiene membresía activa o el código es inválido, cuando intento registrar la asistencia, entonces el sistema debe mostrar un mensaje de error específico. (RF-4.3, UC-05)
  - Dado que el lector falla, cuando no sea posible escanear el QR, entonces debo contar con la opción de registrar la asistencia manualmente. (RF-4.5)

## HU-06 Regenerar código diario de asistencia
- **Como** administrador del gimnasio
- **Quiero** regenerar el código único diario en caso de contingencia
- **Para** garantizar que los clientes puedan seguir registrando su asistencia
- **Criterios de aceptación:**
  - Dado que detecto un problema con el código diario, cuando utilizo la opción de regenerarlo desde el panel, entonces el backend debe crear un nuevo código válido para todos los clientes. (RF-4.6)
  - Dado que se genera un nuevo código, cuando los clientes refresquen su app, entonces deben obtener el nuevo QR actualizado. (RF-4.2)

## HU-07 Configurar branding y diccionarios multilingües
- **Como** administrador del gimnasio
- **Quiero** personalizar el branding y actualizar los textos en múltiples idiomas
- **Para** mantener la identidad visual y comunicativa del gimnasio en todos los canales
- **Criterios de aceptación:**
  - Dado que accedo a la configuración general, cuando actualizo logo, imágenes y colores permitidos, entonces el sistema debe aplicar los cambios a la app y al panel. (RF-1.2)
  - Dado que edito los diccionarios de español e inglés, cuando guardo la configuración, entonces los textos deben quedar disponibles para ambos idiomas. (RF-1.3)
  - Dado que falta una traducción obligatoria, cuando intento guardar, entonces el sistema debe impedir la operación y solicitar completar la información. (UC-06)

## HU-08 Configurar recordatorios de vencimiento
- **Como** administrador del gimnasio
- **Quiero** definir el contenido y la anticipación de los recordatorios de membresía
- **Para** mantener informados a los clientes sobre sus vencimientos
- **Criterios de aceptación:**
  - Dado que selecciono un tipo de membresía, cuando configuro la anticipación del recordatorio, entonces el sistema debe guardar la programación para enviar notificaciones y correos. (RF-3.4)
  - Dado que edito el contenido de un recordatorio, cuando guardo los cambios, entonces debe actualizarse tanto para correo como para notificación push. (RF-8.1, RF-8.2)

## HU-09 Consultar métricas y exportar reportes
- **Como** administrador del gimnasio
- **Quiero** revisar estadísticas de asistencia e ingresos y exportarlas a CSV
- **Para** analizar el desempeño del gimnasio y compartir información
- **Criterios de aceptación:**
  - Dado que accedo al panel de métricas, cuando aplico filtros por hora, día o mes, entonces el sistema debe actualizar las visualizaciones correspondientes. (RF-7.1)
  - Dado que necesito revisar membresías activas o inactivas, cuando consulto las métricas, entonces debo ver los totales actualizados. (RF-7.2)
  - Dado que deseo respaldar la información, cuando solicito la exportación, entonces el sistema debe generar un archivo CSV con los datos filtrados. (RF-7.3)

## HU-10 Llevar control de rutina diaria
- **Como** cliente del gimnasio
- **Quiero** marcar mi avance en un checklist diario de ejercicios desde la app
- **Para** dar seguimiento a mi rutina personal
- **Criterios de aceptación:**
  - Dado que accedo a la sección de rutina, cuando visualizo el checklist del día, entonces debo poder marcar cada elemento completado. (RF-6.5)
  - Dado que finalizo el checklist, cuando marco todos los elementos, entonces el sistema debe guardar mi progreso y mostrar una confirmación. (RF-6.5)
  - Dado que regreso posteriormente, cuando consulto mi rutina, entonces debo ver el estado actualizado de mis marcas. (RF-6.5)
