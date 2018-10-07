from django.db import models

# Create your models here.

class Item(models.Model):
    content = models.CharField(max_length=200)
    done = models.BooleanField()
    def __str__(self):
        return "content:"+self.content+"  done:"+str(self.done)