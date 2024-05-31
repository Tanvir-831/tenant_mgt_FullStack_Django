from django import forms
from .models import Building, Flat
from django.forms import ModelForm


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'Location', 'District', 'post_code', 'total_flat', 'building_image']

        labels = {
            'name': 'Building Name',
            'Location': 'Location',
            'District': 'District',
            'post_code': 'Post Code',
            'total_flat': 'Total Flat',
            'building_image': 'Building Image'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Location': forms.TextInput(attrs={'class': 'form-control'}),
            'District': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
            'total_flat': forms.NumberInput(attrs={'class': 'form-control'}),
            'building_image': forms.FileInput(attrs={'class': 'form-control'})
        }


class FlatForm(ModelForm):
    class Meta:
        model = Flat
        fields = ['number', 'building', 'bedroom', 'washroom', 'kitchen', 'balcony', 'flat_area', 'rent']

        labels = {
            'number': 'Flat Number',
            'building': 'Building',
            'bedroom': 'Bedroom',
            'washroom': 'Washroom',
            'kitchen': 'Kitchen',
            'balcony': 'Balcony',
            'flat_area': 'Flat Area',
            'rent': 'Rent'
        }

        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'building': forms.Select(attrs={'class': 'form-control'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'washroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'kitchen': forms.NumberInput(attrs={'class': 'form-control'}),
            'balcony': forms.NumberInput(attrs={'class': 'form-control'}),
            'flat_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'})
        }


class FlatUpdateForm(ModelForm):
    class Meta:
        model = Flat
        fields = ['number', 'building', 'bedroom', 'washroom', 'kitchen', 'balcony', 'flat_area', 'rent', 'tenant']

        labels = {
            'number': 'Flat Number',
            'building': 'Building',
            'bedroom': 'Bedroom',
            'washroom': 'Washroom',
            'kitchen': 'Kitchen',
            'balcony': 'Balcony',
            'flat_area': 'Flat Area',
            'rent': 'Rent',
            'tenant': 'Tenant'
        }

        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'building': forms.Select(attrs={'class': 'form-control'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'washroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'kitchen': forms.NumberInput(attrs={'class': 'form-control'}),
            'balcony': forms.NumberInput(attrs={'class': 'form-control'}),
            'flat_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'tenant': forms.Select(attrs={'class': 'form-control'})
        }