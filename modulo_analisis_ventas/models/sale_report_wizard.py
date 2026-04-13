from odoo import api, fields, models

class SaleReportWizard(models.TransientModel):
    _name = 'sale.report.wizard'
    _description = 'Asistente de informe de ventas'

    # campos para filtrar el informe fecha incio, fecha fin, cliente
    date_from = fields.Date(string='Fecha desde', required=True)
    date_to = fields.Date(string='Fecha hasta', required=True)

    partner_id = fields.Many2one('res.partner', string='Cliente')

    # Método para obtener el dominio de búsqueda de las ventas
    def _get_domain(self):
        # filtro base para obtener solo las ventas confirmadas o realizadas
        domain = [('state', 'in', ['sale', 'done'])]
        
        
        # agregar filtro de fecha
        if self.date_from:
            domain.append(('date_order', '>=', self.date_from))

        if self.date_to:
            domain.append(('date_order', '<=', self.date_to))
        
        # agregar filtro de cliente
        if self.partner_id:
            domain.append(('partner_id', '=', self.partner_id.id))
        
        # devolvemos el dominio completo para la búsqueda de las ventas
        return domain
    
    # Método para generar el informe de ventas
    def action_print_report(self):
        # aquí localizamos la accion del informe definida en XML
        # modulo_analisis_ventas.action_sale_report_pdf
        
        return self.env.ref('modulo_analisis_ventas.action_sale_report_pdf').report_action(self, data={
        'date_from': str(self.date_from) if self.date_from else False,
        'date_to': str(self.date_to) if self.date_to else False,
        'partner_name': self.partner_id.name if self.partner_id else False,
        'lines': self.get_report_lines(),
        'total': self.get_total_general(),
    })
    
    # metodo para obtener los datos de las ventas según el dominio
    def get_report_lines(self):
        # obtenemos el dominio de búsqueda
        domain = self._get_domain()
        
        # buscamos en el modelo sale.order las ventas que cumplen con el dominio
        sales = self.env['sale.order'].search(domain, order='date_order desc')

        # crear una lista de diccionarios con los datos que queremos mostrar en el informe
        lines = []

        for sale in sales:
            # dentro de cada pedido de venta, recorremos las líneas para obtener los detalles de cada producto vendido
            for line in sale.order_line:
                lines.append({
                    'pedido': sale.name,
                    'fecha': str(sale.date_order),
                    'cliente': sale.partner_id.name,
                    'producto': line.product_id.name,
                    'cantidad': line.product_uom_qty,
                    'precio_unitario': line.price_unit,
                    'subtotal': line.price_subtotal,
            })
        
        # Devolvemos la lista completa
        return lines
                
    # Método para obtener el total de ventas
    def get_total_general(self):
        total = 0.0

        # recorremos las líneas del informe para sumar el subtotal de cada línea
        lines = self.get_report_lines()
        total = sum(line['subtotal'] for line in lines)
        
        # devolvemos el total general de ventas
        return total
    

