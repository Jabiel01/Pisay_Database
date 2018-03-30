from django import forms

from canteen.models import Consumable, Purchase


class ConsumableForm(forms.ModelForm):

	class Meta:
		model = Consumable
		fields = ('__all__')

class PurchaseForm(forms.ModelForm):

	class Meta:
		model = Purchase
		fields = ('__all__')

"""class PurchaseForms(forms.Form):

    consumable = forms.
    anchor = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Link Name / Anchor Text',
                    }),
                    required=False)
    url = forms.URLField(
                    widget=forms.URLInput(attrs={
                        'placeholder': 'URL',
                    }),
                    required=False)
"""