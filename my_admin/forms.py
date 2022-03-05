from .models import My_Admin_Panel
from alumni_fee.models import Fee_Info
from django import forms
class MyAdminForm(forms.Form):
    user_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your User Name"
        })
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Password"
        })
    )


class AdminFeeForm(forms.ModelForm):
    class Meta:
        model = Fee_Info
        fields = [
            "registration_fee",
            "yearly_fee",
            "life_time_fee"  
        ]
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control'})