from django import forms
from .models import Post,Comment
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("auther","title","text")
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postscontant'})
        }
class commentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("auther","text")
        widgets = {
                    'auther':forms.TextInput(attrs={'class':'textinputclass'}),
                    'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
                }
