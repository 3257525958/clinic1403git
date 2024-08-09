from django import forms
from file_app.models import fpeseshktestmodel
class peseshkform(forms.ModelForm):
    class Meta:
        model = fpeseshktestmodel
        fields = ('vahedeobject',
                  )
        labels = {'apghablimage':'آپلود عکس',
                  'vahedeobject':'مقدار واحد :',
                  }
        widgets = {
            'apghablimage':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
            'vahedeobject': forms.FileInput(attrs={'class': 'validate', 'name': 'vahedeobject'}),
        }
class testform(forms.Form):
    img = forms.ImageField()