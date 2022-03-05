from django.db import models
from alumni_profile.models import Alumni_Profile
# Create your models here.
class News(models.Model):
    default_user = 1
    headline = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='uploads/',blank=True)
    is_approved = models.BooleanField(default=False)
    news_letter = models.ForeignKey('News_Letter',on_delete=models.SET_NULL,blank=True,null=True,related_name='news')
    author = models.ForeignKey('alumni_profile.Alumni_Profile',default=default_user,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class News_Letter(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    

