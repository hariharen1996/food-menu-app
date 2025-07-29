from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_desc = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='images/',default='images/default.png')
    
    def __str__(self):
        return self.item_name