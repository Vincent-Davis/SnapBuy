from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags
class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["nama", "price", "description", "produk_terjual", "rating"]

        def clean_nama(self):
            nama = self.cleaned_data["nama"]
            return strip_tags(nama)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        