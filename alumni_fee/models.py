from django.db import models

# Create your models here.
class Fee_Info(models.Model):
    registration_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    yearly_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    life_time_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)


class Alumni_Fee(models.Model):
    registration_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    yearly_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    life_time_fee = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    alumni = models.OneToOneField('alumni_profile.Alumni_Profile',on_delete=models.CASCADE)
    fee_info = models.ForeignKey('Fee_Info',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    # yearly_fee_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.alumni.full_name


class Alumni_Yearly_Fee(models.Model):
    alumni_fee = models.ForeignKey('Alumni_Fee',on_delete=models.CASCADE)
    year = models.CharField(max_length=6)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    is_paid = models.BooleanField()

    def __str__(self):
        return self.alumni_fee.alumni.full_name +"  "+self.year
    



