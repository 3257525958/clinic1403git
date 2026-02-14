from django import forms
from .models import MessageTemplate

class SendSMSForm(forms.Form):
    message_name = forms.CharField(max_length=100, required=False, label="نام پیام (برای ذخیره‌سازی)")
    message_text = forms.CharField(widget=forms.Textarea, required=True, label="متن پیام")
    contacts = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="مخاطبان")  # dynamically filled

    def __init__(self, *args, **kwargs):
        contact_choices = kwargs.pop('contact_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['contacts'].choices = contact_choices