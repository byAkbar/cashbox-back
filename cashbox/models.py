from django.db import models







class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=200, unique=True, verbose_name = "Имя")
    status = models.BooleanField(default=True, verbose_name="Статус")

    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


 




class Product(models.Model):
    """Продукты"""
    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name = "Имя", null=False)
    status = models.BooleanField(default=True, verbose_name = "Статус")
    version = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "category")

    
    
    
    def __str__(self):
        return f'{[ self.name, self.version ]}'


 
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"






class Product_history(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_history')
    version = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return f"{[self.product, self.version]}"


    class Meta:
        verbose_name = 'История продуктов'
        verbose_name_plural = 'История продуктов'


