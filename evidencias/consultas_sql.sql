-- ===============================================
-- PPF1888 - Consultas SQL
-- Autor: Rafael Martin
-- ===============================================

-- ===============================================
-- Consulta 1: Ventas por cliente
-- ===============================================
SELECT 
    rp.name AS Cliente,
    COUNT(so.id) AS Numero_pedidos,
    SUM(so.amount_total) AS Total_ventas
FROM 
    sale_order so
JOIN 
    res_partner rp ON so.partner_id = rp.id
GROUP BY 
    rp.name
ORDER BY 
    Total_ventas DESC;

-- ===============================================
-- Consulta 2: Ventas por productos
-- ===============================================
SELECT
    pt.name AS Producto,
    SUM(sol.product_uom_qty) AS Cantidad_vendida,
    SUM(sol.price_total) AS Total_ventas
FROM
    sale_order_line sol
JOIN
    sale_order so ON sol.order_id = so.id
JOIN
    product_product pp ON sol.product_id = pp.id
JOIN
    product_template pt ON pp.product_tmpl_id = pt.id
WHERE so.state IN ('sale', 'done')
GROUP BY
    pt.name
ORDER BY
    Total_ventas DESC;

-- ===============================================
-- Consulta 3: Detalle de ventas
-- ===============================================
SELECT
    so.name AS Numero_pedido,
    rp.name AS Cliente,
    pt.name AS Producto,
    so.date_order AS Fecha_pedido,
    sol.product_uom_qty AS Cantidad,
    sol.price_unit AS Precio_unitario,
    sol.price_subtotal AS Subtotal
FROM
    sale_order_line sol
JOIN
    sale_order so ON sol.order_id = so.id
JOIN
    res_partner rp ON so.partner_id = rp.id
JOIN
    product_product pp ON sol.product_id = pp.id
JOIN
    product_template pt ON pp.product_tmpl_id = pt.id
WHERE so.state IN ('sale', 'done')
ORDER BY
    so.date_order DESC;

