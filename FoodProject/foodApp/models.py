from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://media.istockphoto.com/id/1137255480/vector/coming-soon-sign.jpg?s=1024x1024&w=is&k=20&c=6ey80gBK_vWoOHJSNzeNL1KXVCGHevn1bXTsafUF0U4=")

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("foodApp:detail", kwargs={'pk':self.pk})
    
    