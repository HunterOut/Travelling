from django import forms
from cities.models import City

class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control',}))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control',}))
    across_sities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(),
                                                    required=False,
                                                    widget=forms.Select(attrs={'class': 'form-control',}))
    traveling_time = forms.IntegerField(label='Время в пути',
                                     widget=forms.NumberInput(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'Введите время в пути'}))