from django import forms
from .models import ResumeModel

GENDER_CHOICES =[
    ('Male', 'Male'),
    ('Female', 'Female')
]

CITY_CHOICES = [
    ('Ahmedabad', 'Ahmedabad'),
    ('Vadodara', 'Vadodara'),
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Delhi', 'Delhi')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations',choices=CITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ResumeModel
        fields = ('name', 'dob', 'gender', 'locality', 'city', 'Pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file', )
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'Pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'profile_image':'Profile Image', 'my_file':'Document'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'Pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
         
        }
