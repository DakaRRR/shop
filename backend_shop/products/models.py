from PIL import Image
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from io import BytesIO

REQUIRED_FORMATS = ['jpg', 'png']

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Product(models.Model):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

        ordering = ['title']

    class Status(models.TextChoices):
        in_stock = "1", "В наличии"
        on_order = "2", "Под заказ"
        pending = "3", "Ожидается поступление"
        out_of_stock = "4", "Нет в наличии"
        not_available = "5", "Не производится"

    title = models.CharField(_('title'), max_length=255)
    sku = models.CharField(_('sku'), max_length=255, unique=True)
    price = models.IntegerField(_('price'))
    status = models.CharField(_('status'), max_length=1,
                              choices=Status.choices,
                              default=Status.in_stock)
    image = models.ImageField(_('image'), upload_to=upload_to, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image and self.image.name.rpartition('.')[-1] in REQUIRED_FORMATS:
            filename = "%s.webp" % self.image.name.split('.')[0] # будущее название файла
            image_pil = Image.open(self.image)
            image = image_pil.convert('RGB')
            image_io = BytesIO()
            image.save(image_io, format='webp')

            # изменить значение поля изображения на новое измененное значение изображения
            self.image.save(filename, ContentFile(image_io.getvalue()), save=False)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
