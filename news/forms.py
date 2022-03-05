from django import forms
from .models import News,News_Letter
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        labels = {
        "image": "Image(Optional):"
        }
        fields = [
            "headline",
            "description",
            "image",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "description":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':3,
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})

class NewsFormAdmin(forms.ModelForm):
    class Meta:
        model = News
        labels = {
        "image": "Image(Optional):"
        }
        fields = [
            "headline",
            "description",
            "image",
            "author",
            "news_letter",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "description":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':3,
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})
                
class DateInput(forms.DateInput):
    input_type = 'date'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = News_Letter
        labels = {
        "description": "Description(Optional):"
        }
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date':DateInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "description":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':2,
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})