# Análisis de Ventas (Módulo de Odoo)

Este módulo proporciona un asistente (wizard) interactivo que permite generar informes de ventas detallados en formato PDF, facilitando la toma de decisiones mediante el filtrado de datos por fechas y clientes.

## 📋 Descripción

El módulo `modulo_analisis_ventas` extiende las capacidades nativas de Odoo para extraer información específica de los pedidos de venta. Permite obtener un desglose línea por línea de los productos vendidos, sus cantidades y montos, consolidando la información en un documento profesional.

## 🛠️ Características Técnicas

El módulo implementa los siguientes componentes:

* **Modelo Transient (`sale.report.wizard`):** Gestiona la entrada de datos del usuario sin persistir información innecesaria en la base de datos.
* **Lógica de Negocio:**
    * `_get_domain()`: Filtra dinámicamente órdenes en estado "Venta" (`sale`) o "Hecho" (`done`).
    * `get_report_lines()`: Itera sobre los pedidos y sus líneas para construir una estructura de datos procesable por el motor QWeb.
    * `get_total_general()`: Calcula de forma eficiente el sumatorio total de los subtotales de las ventas filtradas.
* **Reporte QWeb:** Plantilla XML que utiliza `web.external_layout` para un acabado profesional con encabezados y pies de página corporativos.

## 🚀 Requisitos e Instalación

### Requisitos
* Odoo (versión compatible con modelos `TransientModel`).
* Módulo de **Ventas** (`sale`) instalado.

### Instalación
1. Descargue el archivo `modulo_analisis_ventas.zip`.
2. Descomprima el contenido en su carpeta de `addons`.
3. Reinicie el servicio de Odoo.
4. Active el **Modo Desarrollador**.
5. Vaya a **Aplicaciones > Actualizar lista de aplicaciones**.
6. Busque e instale `modulo_analisis_ventas`.

## 📖 Guía de Uso

1.  Diríjase al menú de **Ventas**.
2.  Abra el asistente **Informe de ventas**.
3.  Configure los filtros deseados:
    * **Fecha desde:** (Obligatorio) Inicio del periodo.
    * **Fecha hasta:** (Obligatorio) Fin del periodo.
    * **Cliente:** (Opcional) Filtrar por un socio comercial específico.
4.  Pulse el botón para generar el PDF.

## 📊 Estructura del Informe

El PDF generado presenta la siguiente información organizada en tablas:
* **Encabezado:** Detalles de los filtros aplicados.
* **Cuerpo:** Tabla detallada con Pedido, Fecha, Cliente, Producto, Cantidad, Precio Unitario y Subtotal.
* **Pie de página:** Total general acumulado de las líneas reportadas.

---
**Desarrollado para:** Gestión de análisis de datos en Odoo.