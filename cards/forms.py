# cards/forms.py

from django import forms
from cards.models import LanguageSet


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)


class LanguageSetForm(forms.ModelForm):
    class Meta:
        model = LanguageSet
        fields = ['language_pair', 'title', 'name', 'description']  # Customize fields as per your model