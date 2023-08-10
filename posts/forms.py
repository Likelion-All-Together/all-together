from django import forms
from .models import Post, Comment

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        
class PostCreateForm(PostBaseForm):
    CATEGORY_CHOICES = [
            ('알바','알바'),
            ('과외','과외'),
            ('취준','취준'),
            ('경력단절','경력단절'),
    ]
    category = forms.ChoiceField(label='카테고리',choices= CATEGORY_CHOICES)
    class Meta(PostBaseForm.Meta):
        fields = ['title', 'content', 'category']  
    
    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['category'] = self.cleaned_data['category']
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']