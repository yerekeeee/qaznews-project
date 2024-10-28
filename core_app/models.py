from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Tag(models.Model):
    name = models.CharField("Название тега", max_length=100)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField("Название поста", max_length=150)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Тег")
    description = models.TextField("Описание поста")
    image = models.ImageField("Фото", upload_to="news/images/")
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title