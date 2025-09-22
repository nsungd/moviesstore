from django import forms
from .models import SecuritySetting 
from .models import SecurityQuestion

class SecuritySettingForm(forms.ModelForm):
    class Meta:
        model = SecuritySetting
        fields = ['security_question', 'security_answer']
        widgets = {
            'security_answer': forms.PasswordInput(attrs={'placeholder': 'Enter your answer'}),
        }

class SecurityCheckForm(forms.Form):
    username = forms.CharField(max_length=150)
    answer = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)

class SecurityQuestionForm(forms.ModelForm):
    class Meta:
        model = SecurityQuestion
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your security question'}),
            'answer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your answer'}),
        }
