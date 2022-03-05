from django import forms
from .models import Post
class PostForm(forms.Form):
    tag_list=['Job Circular','Educational Blog','Higher Study Opportunities','Publications','Achievements']
    Tag_Choices = []
    for x in tag_list:
        Tag_Choices.append((x,x))

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control bg-light",
            "placeholder": "Write Something To Post!",
            "rows":3,
        })
    )
    tag = forms.ChoiceField(choices = Tag_Choices,widget=forms.Select(
        attrs={
            'style':"display:inline;font-weight:500;"
        })
    )
    image = forms.FileField(required=False,widget=forms.FileInput(
        attrs={
            'style':"display:inline;",
        }
    ))
    files = forms.FileField(required=False,widget=forms.FileInput(
        attrs={
            'style':"display:inline;",
        }
    ))

class CommentForm(forms.Form):
    # body = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            "rows":2,
            "id":'comment_reply'
        })
    )



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "body",
            "tag",
            "image",
            "files",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "body":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':2,
                })
                continue
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })

    