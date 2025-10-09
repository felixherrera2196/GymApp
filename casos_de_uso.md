# Casos de Uso - Plataforma de Gestión de Gimnasio

## UC-01 Gestionar registro de cliente
- **Actor principal:** Administrador del gimnasio.
- **Interesados y objetivos:** El administrador desea dar de alta a nuevos clientes conservando la información de contacto y emergencia para gestionar sus membresías y asistencia.
- **Precondiciones:** El administrador ha iniciado sesión en el panel con permisos completos. El cliente ha proporcionado sus datos personales y de emergencia.
- **Postcondiciones:** El cliente queda registrado con un perfil activo y disponible para asignarle una membresía.
- **Flujo principal:**
  1. El administrador accede al módulo de clientes desde el panel administrativo.
  2. El sistema solicita los datos obligatorios del cliente (nombre, apellidos, teléfono, correo electrónico, dirección, fecha de nacimiento y contacto de emergencia).
  3. El administrador adjunta la fotografía de perfil del cliente.
  4. El administrador confirma el registro.
  5. El sistema almacena la información en la base de datos, registra la auditoría y asocia la imagen en el bucket S3.
  6. El sistema muestra el nuevo cliente en el listado general.
- **Flujos alternos/excepciones:**
  - 5a. Si la fotografía no puede almacenarse en S3, el sistema muestra un mensaje de error y permite reintentar la carga.
  - 2a. Si falta información obligatoria, el sistema solicita completar los campos antes de guardar.

## UC-02 Actualizar perfil desde la aplicación móvil
- **Actor principal:** Cliente del gimnasio.
- **Interesados y objetivos:** El cliente desea mantener actualizada su información personal para recibir notificaciones y mantener vigente su membresía.
- **Precondiciones:** El cliente cuenta con una membresía válida, ha iniciado sesión en la app móvil y dispone de conexión a internet.
- **Postcondiciones:** Los datos del cliente quedan actualizados y el sistema registra la auditoría correspondiente.
- **Flujo principal:**
  1. El cliente abre la aplicación móvil e ingresa al apartado "Mi perfil".
  2. El sistema muestra los datos actuales del cliente.
  3. El cliente modifica la información deseada (datos personales, contacto de emergencia o fotografía).
  4. El cliente guarda los cambios.
  5. El sistema envía la actualización al backend, almacena los datos y registra la auditoría.
  6. El sistema confirma la actualización exitosa en la app.
- **Flujos alternos/excepciones:**
  - 5a. Si se pierde la conexión durante la actualización, la app muestra un error y permite reintentar.
  - 3a. Si el cliente intenta modificar campos restringidos por permisos, la app informa que debe contactar al administrador.

## UC-03 Gestionar membresías y pagos manuales
- **Actor principal:** Administrador del gimnasio.
- **Interesados y objetivos:** El administrador desea asignar membresías y registrar los pagos realizados en efectivo o transferencia.
- **Precondiciones:** El cliente se encuentra registrado y el administrador ha iniciado sesión con permisos completos.
- **Postcondiciones:** El cliente queda asociado a una membresía con estatus de pago actualizado.
- **Flujo principal:**
  1. El administrador ingresa al módulo de membresías del panel.
  2. El sistema muestra las membresías existentes y el estado de cada cliente.
  3. El administrador crea una nueva membresía o edita una existente seleccionando el tipo de plan y duración.
  4. El administrador indica la forma de pago (efectivo o transferencia) y marca el pago como completado.
  5. El sistema actualiza el estatus de la membresía, registra la auditoría y muestra la confirmación.
- **Flujos alternos/excepciones:**
  - 4a. Si el administrador no marca el pago como completado, el sistema mantiene el estatus pendiente y genera un recordatorio.
  - 3a. Si se selecciona un plan con fechas superpuestas, el sistema alerta y solicita ajustar la vigencia.

## UC-04 Pagar membresía con tarjeta desde la app
- **Actor principal:** Cliente del gimnasio.
- **Interesados y objetivos:** El cliente desea renovar o activar su membresía pagando con tarjeta de forma segura.
- **Precondiciones:** El cliente tiene una cuenta activa en la app y dispone de un método de pago compatible con Stripe.
- **Postcondiciones:** El pago queda procesado en Stripe, el estatus de la membresía se actualiza y el cliente recibe confirmación.
- **Flujo principal:**
  1. El cliente accede a la sección de membresías en la app y selecciona el plan deseado.
  2. El sistema muestra el detalle del plan y el monto a pagar.
  3. El cliente elige la opción "Pagar con tarjeta".
  4. El sistema redirige al flujo de pago con Stripe y solicita los datos de la tarjeta.
  5. Stripe procesa el pago y devuelve la confirmación al backend.
  6. El backend actualiza el estatus de la membresía a pagada y registra la auditoría.
  7. La app muestra un mensaje de confirmación y envía un comprobante por correo electrónico.
- **Flujos alternos/excepciones:**
  - 5a. Si Stripe rechaza el pago, la app informa el motivo y permite reintentar con otro método.
  - 4a. Si el cliente cancela el flujo de pago, el sistema vuelve a la pantalla de selección sin cambios.

## UC-05 Registrar asistencia mediante código QR
- **Actor principal:** Recepcionista o administrador.
- **Interesados y objetivos:** El personal del gimnasio desea registrar la asistencia diaria de los clientes de forma rápida y confiable.
- **Precondiciones:** El backend generó el código único diario y los clientes cuentan con un QR vigente en la app. El recepcionista ha iniciado sesión en el panel con permisos adecuados.
- **Postcondiciones:** La asistencia del cliente se registra con la hora de entrada, quedando disponible para reportes.
- **Flujo principal:**
  1. El recepcionista abre el módulo de control de asistencia en el panel.
  2. El sistema activa la cámara o lector para escanear el QR del cliente.
  3. El recepcionista escanea el QR desde la app del cliente.
  4. El panel envía el código al backend para validarlo.
  5. El backend verifica el código diario, el ID del cliente y el estatus de la membresía.
  6. Si todo es válido, el backend registra la asistencia con fecha y hora.
  7. El panel muestra la confirmación de asistencia exitosa.
- **Flujos alternos/excepciones:**
  - 5a. Si el código es inválido o expiró, el panel muestra un mensaje de error y solicita regenerarlo.
  - 6a. Si el cliente no tiene membresía activa, el sistema deniega el registro e informa la situación.
  - 2a. Si la cámara no funciona, el administrador puede ingresar manualmente la asistencia desde el panel.

## UC-06 Configurar branding y diccionarios
- **Actor principal:** Administrador del gimnasio.
- **Interesados y objetivos:** El administrador busca personalizar el aspecto del panel y la app, así como mantener actualizados los idiomas disponibles.
- **Precondiciones:** El administrador ha iniciado sesión en el panel con permisos completos.
- **Postcondiciones:** La configuración de branding y los diccionarios de idiomas quedan actualizados para todos los canales.
- **Flujo principal:**
  1. El administrador accede al módulo de configuración general.
  2. El sistema muestra las opciones de branding (logo, imágenes y paleta de cinco colores) y los diccionarios disponibles.
  3. El administrador carga los nuevos recursos visuales y ajusta los colores.
  4. El administrador edita los textos multilingües para español e inglés.
  5. El administrador guarda los cambios.
  6. El sistema aplica la configuración, actualiza los diccionarios y confirma la operación.
- **Flujos alternos/excepciones:**
  - 3a. Si algún recurso supera el tamaño permitido, el sistema solicita uno nuevo.
  - 4a. Si falta una traducción obligatoria, el sistema impide guardar hasta completarla.

## UC-07 Consultar métricas y exportar reportes
- **Actor principal:** Administrador del gimnasio.
- **Interesados y objetivos:** El administrador quiere visualizar el desempeño del gimnasio y exportar información para análisis externo.
- **Precondiciones:** El administrador ha iniciado sesión en el panel con permisos completos y existen datos registrados en el sistema.
- **Postcondiciones:** El administrador obtiene métricas visuales y, si lo requiere, un archivo CSV con la información filtrada.
- **Flujo principal:**
  1. El administrador accede al panel de métricas.
  2. El sistema muestra gráficos y tablas de asistencia, ingresos y membresías activas/inactivas.
  3. El administrador aplica filtros por hora, día o mes según lo requerido.
  4. El sistema actualiza las visualizaciones con los filtros seleccionados.
  5. El administrador solicita exportar los datos.
  6. El sistema genera y descarga un archivo CSV con la información filtrada.
- **Flujos alternos/excepciones:**
  - 5a. Si no hay datos para el rango seleccionado, el sistema muestra un mensaje de "sin resultados" y deshabilita la exportación.
  - 6a. Si ocurre un error durante la generación del archivo, el sistema notifica y permite reintentar.
