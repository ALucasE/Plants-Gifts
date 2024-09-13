from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Codigo")
    valid_from = models.DateTimeField(verbose_name="validado desde")
    valid_to = models.DateTimeField(verbose_name="validado hasta")
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Valor porcentual (0 a 100)",
        verbose_name="Descuento",
    )
    active = models.BooleanField()

    class Meta:
        verbose_name = 'cupón'
        verbose_name_plural = 'cupones'

    def __str__(self):
        return self.code