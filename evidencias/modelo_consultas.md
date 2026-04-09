# Modelo de consultas
## 1. Objetivo
Diseñar un sistema de análisis de ventas ...

## 2. Modelo de datos relacional
Odoo utiliza un modelo de datos relacional soportado por PostgreSQL

## 3. Objetos principales del diccionario de datos
- Tablas
- Campos
- Registros
- Vistas
- Índices
- Relaciones entre modelos

## 4. Tablas idientificadas para el pedido de venta
### sale_order
Contiene la cabecera de los pedidos
Campos relevantes:
- id
- name
- date_order
- partner_id
- state
- amount_total
- amount_untaxed

### sale_order_line
Contiene las líneas de cada pedido
Campos relevantes:
- id
- order_id
- product_id
- product_uom_qty
- price_unit
- price_subtotal

### res_partner
Contiene la información de clientes
Campos relevantes:
- id
- name

### product_product
Contiene la variante del producto
Campos relevantes:
- id
- product_tmpl_id

### product_template
Contiene la información general del producto
Campos relevantes:
- id
- name

## 5. Relaciones entre tablas
- sale_order.partner_id -> res_partner.id
- sale_order_line.order_id -> sale_order.id
- sale_order_line.product_id -> product_product.id
- product_product.product_tmpl_id -> product_template.id

## 6. Integridad de datos
La clave primaria identifica cada registro de manera única.
La clave ajena permite relacionar tablas.
La integridad referencial garantiza que no existan registros huérfanos o relaciones inválidas.

## 7. Herramientas y lenguajes utilizados
- PostgreSQL: permite consultar directamente la base de datos mediante SQL
- pgAdmin4: Interfaz gráfica que permite la gestión de la base de datos.
- ORM de Odoo: Nos permite acceder a la información desde Python sin usar SQL
- Interfaz de Odoo: permite visualizar registros, exportar datos y probar los resultados.

## 8. Conclusión 
Las fuentes elegidas permiten explorar la información comercial del ERP y construir informes de ventas por cliente, producto y fecha.
  

