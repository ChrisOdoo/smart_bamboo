from odoo import models, fields

class Tarea(models.Model):
    _name = 'tareas.tarea'
    _description = 'Gestión de Tareas'

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    due_date = fields.Date(string='Fecha de vencimiento')
    is_done = fields.Boolean(string='Completado', default=False)
