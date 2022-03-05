from django import forms
from .models import Event
class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "headline",
            "description",
            "discipline",
            "visible_to",
            "target_amount",
            "present_amount",
            "is_present",
        ]
        labels = {
            "discipline": "Discipline (not required)",
            "visible_to": "Visbible To (not required)",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "is_present":
                self.fields[field].widget.attrs.update({
                'style': "margin:7px;"})
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})