from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
                  widget=forms.TextInput(
                      attrs= {
                          "placeholder": "Your title"
                      }
                  )
    )
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs= {
                                "placeholder": "Your description",
                                "rows": 15
                            }
                        )
                  )
    price = forms.DecimalField()


    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(required=False)
    price = forms.DecimalField()
