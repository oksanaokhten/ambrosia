from django import forms
from products.widgets import CustomClearableFileInput
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
