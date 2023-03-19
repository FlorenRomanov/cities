from django import forms
from .models import City
class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Введите город'}))
    img = forms.ImageField(label="Загрузите фотографию")

    class Meta:
        model = City
        fields = ('name', 'content','img')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
