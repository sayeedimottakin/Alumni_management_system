from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User
# Create your models here.
class Alumni_Profile(models.Model):

    discipline_list = ['Architecture','CSE','ECE','Math','URP','Physics','Chemistry','Stat','Pharmacy','BGE','FWT','FMRT','Agrotechnology','ES','SWE','BAD','HRM','DP','PM','DS','History','English','Bangla','IER','Sculpture','Econ','Sociology','MCJ','Law']

    Discipline_Choices = []
    for x in discipline_list:
        Discipline_Choices.append((x,x))

    Id_Choices = []
    for x in range(1,51):
        Id_Choices.append((str(x),str(x)))
    
    Batch_Choices = []
    for x in range(1991,2019):
        Batch_Choices.append((str(x),str(x)))

    job_list=['Agriculture','Architecture and Construction','Business Management and Administration','Education','Finance','Food','Government and Public Administration','Health Science','Human Services','Law, Public Safety, Corrections and Security','Manufacturing','Marketing, Sales and Service','Natural Resources','Science, Technology and Engineering','Other']
    Job_Choices = []
    for x in job_list:
        Job_Choices.append((x,x))
    country_list = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
    Country_Choices = []
    for x in country_list:
        Country_Choices.append((x,x))

    #Table Feilds
    full_name = models.CharField(max_length=255)
    image = models.FileField(upload_to='uploads/')
    certificate = models.FileField(upload_to='uploads/')
    discipline = models.CharField(max_length=255,choices=Discipline_Choices)
    student_id = models.CharField(max_length=10)
    batch = models.CharField(max_length=50,choices=Batch_Choices)
    job_type = models.CharField(max_length=50)
    job_position = models.CharField(max_length=60)
    company_name = models.CharField(max_length=60,blank=True)
    higher_study = models.CharField(max_length=60)
    present_address = models.CharField(max_length=60)
    present_country = models.CharField(max_length=60,choices=Country_Choices)
    prmanent_address = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    facebook = models.URLField(max_length=60,blank=True)
    linkdin = models.URLField(max_length=60,blank=True)
    # social_media_links = models.URLField(max_length=200, blank=True)
    about_me = models.TextField()
    is_verified = models.BooleanField(default=False)
    ask_for_update_certificate = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="alumni")

    def __str__(self):
        return self.user.username