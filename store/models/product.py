from django.db import models
from .category import Category
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) #jb category delete karenege hm to uss model se category se related saare kapde delete krne hai
    descripton = models.CharField(max_length=200,default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category_id)
        else:
            return Product.get_all_products()
    