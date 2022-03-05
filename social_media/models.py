from django.db import models
# Create your models here.

class Post(models.Model):
    tag_list=['Job Circular','Educational Blog','Higher Study Opportunities','Publications','Achievements']
    Tag_Choices = []
    for x in tag_list:
        Tag_Choices.append((x,x))

    author = models.ForeignKey('alumni_profile.Alumni_Profile',on_delete=models.CASCADE)
    body = models.TextField()
    image = models.FileField(upload_to='uploads/',blank=True)
    files = models.FileField(upload_to='uploads/',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=30,choices=Tag_Choices)
    
    def __str__(self):
        return self.author.full_name

class Comment(models.Model):
    author = models.ForeignKey('alumni_profile.Alumni_Profile',on_delete=models.CASCADE)
    body = models.TextField()
    image = models.FileField(upload_to='uploads/',blank=True)
    files = models.FileField(upload_to='uploads/',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

# class Like(models.Model):
#     author = models.ForeignKey('alumni_profile.Alumni_Profile',on_delete=models.CASCADE,related_name="alumni_like")
#     post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name="like")
