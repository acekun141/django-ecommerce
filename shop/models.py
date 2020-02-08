from django.db import models
from django.dispatch import receiver
import os


class Product(models.Model):
    name = models.CharField(max_length=100)
    ver = models.CharField(max_length=100, blank=True, default='')
    price = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return "{0}-{1}".format(self.name, self.ver)


class ImageProduct(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_product')

    def __str__(self):
        return self.image.name

@receiver(models.signals.post_delete, sender=ImageProduct)
def delete_image_when_model_deleted(sender, instance, **kwargs):
    if os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
    else:
        return False
    
@receiver(models.signals.pre_save, sender=ImageProduct)
def delete_image_when_model_edited(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_image = ImageProduct.objects.get(pk=instance.pk)
    except Exception:
        return False
    if old_image.image.path != instance.image.path:
        if os.path.isfile(old_image.image.path):
            os.remove(old_image.image.path)
        else:
            return False
    else:
        return False