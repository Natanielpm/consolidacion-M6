from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    """
    Clase que define el Modelo de datos para vehiculo.
    """
    # Selectores de Marca
    Marca = (
        ('FIAT', 'FIAT'),
        ('CHEVROLET', 'CHEVROLET'),
        ('FORD', 'FORD'),
        ('TOYOTA', 'TOYOTA'),
    )
 
    # Selectores de categoría
    Categoria = (
        ('PARTICULAR', 'PARTICULAR'),
        ('TRANSPORTE', 'TRANSPORTE'),
        ('DE CARGA', 'DE CARGA'),
    )
 
    # Campos
    marca = models.CharField(max_length=20, choices=Marca, default='FORD', verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serial_carroceria = models.CharField(max_length=50, verbose_name='Serial Carroceria')
    serial_motor = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=Categoria, default='PARTICULAR', verbose_name='Categoria')
    precio = models.IntegerField(verbose_name='Precio')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha Registro')
    fecha_modificado = models.DateTimeField(auto_now = True, verbose_name='Última modificación')
 
    # Permisos
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['marca']
        permissions = [
            ("visualizar_catalogo", "Puede visualizar Catálogo de Vehículos"),
            ("modificar_catalogo", "Puede modificar Catálogo de Vehículos"),
        ]
   
    # Método de representación
    def __str__(self):
        return f'Vehiculo marca {self.marca}, modelo {self.modelo}, categoría {self.categoria}. PRECIO: {self.precio}'
    


    def precio_categoria(self):
        """Determina la categoría del precio del vehículo"""
        if self.precio < 10000:
            return 'Bajo'
        elif 10000 <= self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'
