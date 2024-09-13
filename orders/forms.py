import re
from django import forms

from .models import Order



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']

        # Validación con expresiones regulares
        regex = r'^\d{4}$|^[A-HJ-NP-Za-hj-np-z]\d{4}\D{3}$'
        if not re.match(regex, postal_code):
            raise forms.ValidationError("Formato de código postal inválido.")

        # Validación de longitud
        if len(postal_code) not in (4, 8):
            raise forms.ValidationError("La longitud del código postal debe ser de 4 u 8 caracteres.")

        # Formateado del código postal (si es necesario)
        if len(postal_code) == 8:
            return '%s%s%s' % (postal_code[0].upper(), postal_code[1:5], postal_code[5:].upper())

        return postal_code

