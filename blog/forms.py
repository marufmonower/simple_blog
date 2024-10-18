from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <= 3:  # BUG: Incorrect condition for title validation
            raise forms.ValidationError('The title is too short.')
        return title
