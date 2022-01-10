from django.db import models

# Create your models here.
class CategoriesModel(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255, unique=True) # Sirve para hacer la navegacion 
    published = models.BooleanField(default=False) # Podemos tener categorias publicadas y no publicadas

    def __str__(self):
        return self.title
