# Requerimientos No Funcionales - Plataforma de Gestión de Gimnasio

## 1. Usabilidad
- RNF-1.1 Las interfaces del panel administrativo y la app móvil deben seguir el branding configurable del gimnasio.
- RNF-1.2 La plataforma debe ofrecer una experiencia multilingüe, permitiendo cambiar entre español e inglés desde la configuración.
- RNF-1.3 La app móvil debe mostrar el código diario y recordatorios en la pantalla principal de manera clara y accesible.

## 2. Rendimiento y Escalabilidad
- RNF-2.1 La infraestructura debe dimensionarse para soportar hasta 200 usuarios diarios y 20 usuarios concurrentes sin degradar el rendimiento.
- RNF-2.2 El sistema debe generar y distribuir el código diario para todos los clientes a las 00:00 horas sin interrupciones del servicio.

## 3. Seguridad
- RNF-3.1 El backend debe implementar autenticación basada en JWT para el acceso a las APIs.
- RNF-3.2 Los roles de Administrador y Recepcionista deben tener permisos diferenciados, asegurando que solo el administrador posea privilegios totales.
- RNF-3.3 El sistema debe conservar auditorías de operaciones (fecha, hora y usuario) y aplicar borrado lógico para preservar la trazabilidad.
- RNF-3.4 Los datos sensibles, incluidas las fotografías de perfil almacenadas en S3 y la información de pago procesada por Stripe, deben transmitirse mediante canales seguros (HTTPS).

## 4. Disponibilidad y Recuperación
- RNF-4.1 El sistema no requiere niveles especiales de disponibilidad en esta fase, pero debe garantizar la continuidad básica del servicio durante el horario operativo del gimnasio.
- RNF-4.2 El panel debe permitir regenerar manualmente el código diario en caso de contingencia para mantener el control de accesos.

## 5. Integraciones
- RNF-5.1 La integración con Stripe debe cumplir las buenas prácticas de seguridad de la pasarela y mantener actualizado el estatus de pago de las membresías.
- RNF-5.2 El almacenamiento de fotografías en S3 debe gestionar correctamente los permisos de acceso para evitar exposiciones no autorizadas.

## 6. Mantenibilidad
- RNF-6.1 El backend desarrollado en FastAPI y la base de datos PostgreSQL deben seguir una arquitectura modular que facilite entregas incrementales.
- RNF-6.2 El código debe permitir la incorporación futura de nuevas integraciones, como sistemas externos o módulos de soporte, sin reescrituras significativas.

## 7. Operación y Soporte
- RNF-7.1 Aunque no se ha definido un equipo de soporte, la plataforma debe registrar eventos relevantes para facilitar el mantenimiento futuro.
- RNF-7.2 El sistema debe permitir la expansión futura para incorporar un módulo de tickets o soporte si se requiere en versiones posteriores.

## 8. Entregas y Ciclo de Vida
- RNF-8.1 El desarrollo debe organizarse en entregas incrementales, alineadas con la disponibilidad de funcionalidades del backend y la aplicación móvil.
- RNF-8.2 El despliegue de nuevas funcionalidades debe minimizar la interrupción de los servicios existentes para los usuarios finales.
