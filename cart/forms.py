from django import forms

PRODUTO_QUANTIDADE_CHOICES=[(i, str(i)) for i in range (1,10)]

class CartAddQuantityForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        choices=PRODUTO_QUANTIDADE_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )