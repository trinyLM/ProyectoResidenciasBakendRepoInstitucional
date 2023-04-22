from django.db import models


class Carrera(models.Model):
    """modelo de la carrera de la que egreso el estudiamte"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.nombre


class Campus(models.Model):
    """modelo de campus donde se anotara el nombre de la extension de la universidad"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"
        ordering = ["nombre"]


class Autor(models.Model):
    """modelo de autor, informacion necesaria de los autores """
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(
        "Nombres", max_length=255, null=False, blank=False)
    apellido_paterno = models.CharField(
        "Apellido paterno", max_length=255, null=False, blank=False)
    apellido_materno = models.CharField(
        "Apellido materno", max_length=255, null=True, blank=False)
    matricula = models.CharField(
        "Matricula", max_length=255, null=False, blank=False, unique=True)
    asesor_interno = models.CharField(
        "Asesor interno", max_length=255, null=False, blank=False)
    asesor_externo = models.CharField(
        "Asesor externo", max_length=255, null=False, blank=False)
    carrera = models.ForeignKey(
        Carrera, null=False, blank=False, on_delete=models.CASCADE)
    campus = models.ForeignKey(
        Campus, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.apellido_paterno+" "+self.apellido_materno+" "+self.nombres)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nombres"]


class TipoDePublicacion(models.Model):
    """Modelo para los diferentes tipos de archivos, ya sean tesis, reporte de residencias etc."""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        "Nombre", max_length=255, null=False, blank=False)
    descripcion = models.TextField(
        "Descripción", blank=True, null=True, default="")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Publicacion"
        verbose_name_plural = "Tipos de Publicacion"
        ordering = ["nombre"]


class Archivo(models.Model):
    """Modelo de archivo, se registran todos los datos de las publicaciones. """
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        "Titulo", max_length=255,help_text="nombre de la publicacion", null=False, blank=False)
    imagen = models.ImageField(
        "Imagen", upload_to='imgs/', null=False, blank=False)
    materia = models.CharField("Materia", max_length=255)
    fecha_publicacion = models.DateField("Fecha de publicacion",)
    tipo_de_publicacion = models.ForeignKey(
        TipoDePublicacion, on_delete=models.CASCADE)
    pdf = models.FileField("pdf", upload_to='pdfs/',
                           storage=None, default="")
    resumen = models.TextField("Resumen", null=False, blank=True, default="")
    autor = models.ManyToManyField(Autor,related_name="archivos",)

    def Autor(self):
        return ",".join([str(p) for p in self.autor.all()])

    def __str__(self) -> str:
        return self.titulo
