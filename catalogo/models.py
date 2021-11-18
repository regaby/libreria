from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, get_available_image_extensions
from django.urls import reverse
from django.utils.text import slugify

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=8)
    ciudad = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return f"{self.calle}, {self.cod_postal}, {self.ciudad}"

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # print ('self', self)
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Autores"

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=60)
    puntaje = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(10)])
    # autor = models.CharField(max_length=100, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, related_name="libros")
    es_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False, blank=True)
    paises_publicado = models.ManyToManyField(Pais)

    def __str__(self):
        # print ('self', self)
        return f"{self.titulo} - puntaje: {self.puntaje}"

    def get_url(self):
        return reverse('libro', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

