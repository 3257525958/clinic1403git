from django import forms
from file_app.models import fpeseshktestmodel
class peseshkform(forms.ModelForm):
    class Meta:
        model = fpeseshktestmodel
        fields = ('apghablimage',)
        labels = {'apghablimage':'آپلود عکس',
                  }
        widgets = {
            'apghablimage':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
                   }
