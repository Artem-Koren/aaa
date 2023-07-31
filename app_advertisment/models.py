from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("загаловок", max_length=128)
    text = models.TextField("описание")
    author = models.CharField("автор", max_length=64)
    data = models.DateField("дата", auto_now_add = True )

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"


migrations.RenameModel (old_name="app_advertisements_advertisement)", new_name="advertisement",)