from django import forms
# from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    
# class ContactModelForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#         # fields = ['name', 'email', 'message']
#         # exclude = ['created_at']
    