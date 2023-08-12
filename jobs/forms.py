from django import forms
from .models import Class

class ClassBaseForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        

class ClassCreateForm(ClassBaseForm):
    class Meta(ClassBaseForm.Meta):
        fields = '__all__'