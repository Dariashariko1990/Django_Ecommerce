from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    CHOICES = [('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5')
               ]
    name = forms.CharField(widget=forms.Textarea, label='Имя')
    content = forms.CharField(widget=forms.Textarea, label='Содержание')
    mark = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta(object):
        model = Review
        exclude = ('id', 'product')