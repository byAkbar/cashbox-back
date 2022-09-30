from ensurepip import version
from django.db import models
from cashbox.models import Product, Product_history
from users.models import CustomUser



class Order(models.Model):
    cash = models.IntegerField(help_text="указывать сумму в сумах", verbose_name='Наличка')
    card = models.IntegerField(help_text="указывать сумму в сумах", verbose_name='Онлайн')
    returned = models.IntegerField(help_text="указывать сумму в сумах", verbose_name='Возвращено', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Продовец")

    

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    # version = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='versions')
    version = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    returned_quantity = models.PositiveSmallIntegerField(default=0)



    def __str__(self):
        return f"{self.product} {self.version}"


  
    class Meta:
        verbose_name = 'Деталь заказов'
        verbose_name_plural = 'Детали заказов'
 
    def __str__(self):
        return 'Order {}'.format(self.id)









