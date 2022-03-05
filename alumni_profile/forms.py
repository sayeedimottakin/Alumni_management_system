from django import forms
from .models import Alumni_Profile

class ProfileForm(forms.Form):
    discipline_list = ['Architecture','CSE','ECE','Math','URP','Physics','Chemistry','Stat','Pharmacy','BGE','FWT','FMRT','Agrotechnology','ES','SWE','BAD','HRM','DP','PM','DS','History','English','Bangla','IER','Sculpture','Econ','Sociology','MCJ','Law']

    Discipline_Choices = []
    for x in discipline_list:
        Discipline_Choices.append((x,x))
    Id_Choices = []
    for x in range(1,51):
        Id_Choices.append((x,x))
    
    Batch_Choices = []
    for x in range(1991,2019):
        Batch_Choices.append((x,x))
    
    job_list=['Agriculture','Architecture and Construction','Business Management and Administration','Education','Finance','Food','Government and Public Administration','Health Science','Human Services','Law, Public Safety, Corrections and Security','Manufacturing','Marketing, Sales and Service','Natural Resources','Science, Technology and Engineering','Other']
    Job_Choices = []
    for x in job_list:
        Job_Choices.append((x,x))
    country_list = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
    Country_Choices = []
    for x in country_list:
        Country_Choices.append((x,x))


    #form feilds
    full_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Name"
        })
    )
    profile_pic = forms.FileField()
    certificate = forms.FileField()
    discipline = forms.ChoiceField(choices=Discipline_Choices,widget=forms.Select(
        attrs={
           "class":"edit_profile_select",
        }
    ))
    student_id = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Student ID"
        })
    )
    batch = forms.ChoiceField(choices=Batch_Choices,widget=forms.Select(
        attrs={
            "class":"edit_profile_select",
        }
    ))
    job_type = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Job Type "
        })
       
    )
    job_posi = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Position "
        })
    )
    company_name = forms.CharField(
        required=False,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Company Name"
        })
    )
    
    higher_study = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Higher Study Information"
        })
    )
    present_address = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Present Address"
        })
    )
    present_country = forms.ChoiceField(choices=Country_Choices,widget=forms.Select(
        attrs={
            "class":"edit_profile_select",
        }
    ))
    parmanent_address = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Parmanent Address"
        })
    )
    mobile = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Mobile Number"
        })
    )
    facebook = forms.URLField(
        max_length=60,
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Facebook ID Link"
        })
    )
    linkdin = forms.URLField(
        max_length=60,
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Linkdin Profile Link"
        })
    )
    # social_media_links = forms.URLField(
    #     widget=forms.URLInput(attrs={
    #         "class": "form-control",
    #         "label": "Enter Your Social Media Links"
    #     })
    # )
    about_me = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write About You",
            "rows":2,
        })
    )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Alumni_Profile
        fields = [
            "full_name",
            "image",
            "certificate",
            "discipline",
            "student_id",
            "batch",
            "job_type",
            "job_position",
            "company_name",
            "higher_study",
            "present_address",
            "present_country",
            "prmanent_address",
            "mobile",
            "facebook",
            "linkdin",
            "about_me",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "image" or field == "certificate":
                continue
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })