from odoo.tests.common import TransactionCase

class TestTareas(TransactionCase):

    def setUp(self):
        super(TestTareas, self).setUp()
        # Crea un registro de ejemplo en el modelo tareas.tarea
        self.tarea = self.env['tareas.tarea'].create({
            'name': 'Prueba de tarea',
            'description': 'Descripción de prueba',
            'due_date': '2024-12-31',
            'is_done': False,
        })

    def test_creacion_tarea(self):
        """Test para verificar la creación de tareas"""
        self.assertEqual(self.tarea.name, 'Prueba de tarea', "El nombre de la tarea no coincide.")
        self.assertFalse(self.tarea.is_done, "La tarea debería estar marcada como no completada.")

    def test_actualizacion_tarea(self):
        """Test para verificar la actualización de tareas"""
        self.tarea.write({'is_done': True})
        self.assertTrue(self.tarea.is_done, "La tarea debería estar marcada como completada.")

