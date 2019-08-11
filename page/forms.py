from django import forms
from .models import Carousel, Page


class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = [
            'title',
            'cover_image',
            'status'
        ]  # don't use this


class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        # fields = '__all__'
        # exclude = ['title'] title hariç hepsini getir. don't use
        fields = [
            'title',
            'cover_image',
            'content',
            'status',
        ]
