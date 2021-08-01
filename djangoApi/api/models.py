from django.db import models
from ckeditor.fields import RichTextField

class stock (models.Model):
    stockName =  models.CharField(max_length=100)
    stockPrice = models.CharField(max_length=10)
    stockSl = models.CharField(max_length=10)
    stockTarget = models.CharField(max_length=10)
    stockAdvice = models.CharField(max_length=10)
    timeStamp = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.stockName
    
    class meta:
        ordering = ['timeStamp']


class articles (models.Model):
    title = models.CharField(max_length=300)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    description         = RichTextField(null=True, blank=True)
    description2 =  models.TextField(default='hello')


    def __str__(self):
        return self.title


    def get_image_url(self, obj):
        return obj.header_image.url