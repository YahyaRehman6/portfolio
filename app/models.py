from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    message = models.TextField()

class Profile_Picture(models.Model):
    image = models.ImageField(upload_to='MEDIA/Images')
    # created_at = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     get_latest_by = 'date'
