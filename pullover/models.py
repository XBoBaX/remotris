from django.db import models

class pullover(models.Model):
    tittle = models.CharField(null=True, blank=True, max_length=100, verbose_name="Название")
    adress = models.CharField(null=True, blank=True, max_length=200, verbose_name="Ссылка")
    price = models.IntegerField(default=0, verbose_name="Цена")
    photo = models.ImageField(upload_to='image/', verbose_name="Изображение")
    top = models.BooleanField(default=False, verbose_name="В топ?")

    def __str__(self):
        return "{0}_{1}".format(self.tittle, self.price)

    class Meta:
        verbose_name = u"Свитшоты"
        verbose_name_plural = u"Свитшоты"
