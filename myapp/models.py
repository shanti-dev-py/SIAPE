from django.db import models
from django.db.models import SET_NULL
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
# Model for the table 'usuarios'
class UserSchema(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=[('Estudiante', 'Estudiante'), ('Docente', 'Docente'), ('Admin', 'Administrador')])
    is_active = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'usuarios'  # 👈 Mapea al nombre exacto de la tabla existente
        managed = False        # 👈 Indica que Django **no debe crear ni modificar** esta tabla
# Model for the table 'areas'
class AreaSchema(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100)
    id_plandearea = models.ForeignKey('PlanAreaSchema', on_delete=models.DO_NOTHING, db_column='id_plandearea') # 👈 Mapea la columna correcta (lo hacemos explicito)

    class Meta:
        db_table = 'areas'
        managed = False
# Model for the table 'plandearea'
class PlanAreaSchema(models.Model):
    id_plandearea = models.AutoField(primary_key=True)
    dba = models.TextField()
    ebc = models.TextField()
    competencias = models.TextField()
    malla_curricular = models.TextField()
    matriz_refe = models.TextField()
    
    
    class Meta:
        db_table = 'plandearea'
        managed = False
# Model for the table 'grados' 
class GradoSchema(models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre_grado = models.TextField()
    id_area = models.ForeignKey('PlanAreaSchema', on_delete=models.DO_NOTHING, db_column='id_area') #Deve ser una relacion de uno a muchos

    class Meta:
        db_table = 'grados'
        managed = False