from django import forms
from cantact_app.models import accuntmodel

class accuntform(forms.ModelForm):
    class Meta:
        model = accuntmodel
        exclude = ('firstname','lastname','melicode','phonnumber','berthday'),
        # labels = {
        #     "imageuser" : ('عکسی برای پروفایل خودتان انتخاب کنید'),
        # }
        # widgets = {
        #     "imageuser" : forms.Textarea(attrs = { "class":"box",}),
        # }
