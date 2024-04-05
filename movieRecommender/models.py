from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieReviewModel(models.Model):
    Reviewid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    Rating = models.IntegerField(max_length=3)
    movietitle = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id-'+str(self.Reviewid)
    
    