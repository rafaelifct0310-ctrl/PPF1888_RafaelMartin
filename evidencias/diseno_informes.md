# Diseño de informes

## 1. Objetivo del informe
Presentar información comercial sobre ventas confirmadas del sistema ERP.

## 2. Fuentes de información
- sale_order
- sale_order_line
- res_partner
- product_product
- product_template

## 3. Tipo de informe
Se ha diseñado un informe pdf accesible desde un asistente en Odoo.

## 4. Filtros del informe
- Fecha desde
- Fecha hasta
- Cliente

## 5. Campos mostrados
- Pedido
- Fecha
- Cliente
- Producto
- Cantidad
- Precio unitario
- Subtotal
- Total general

## 6. Formato de presentación
El informe se presenta en formato de tabla, ordenado por fecha de pedido en orden descendente.

## 7. Prueba funcional realizada
- Se abrió el asistente desde el menú de ventas
- Se introdujeron filtros
- Se generó el PDF correctamente
- Se comprobó que lo datos mostrados cinciden con los pedidos del sistema

## 8. Conclusión
El informe permite explorar información empresarial de forma clara.