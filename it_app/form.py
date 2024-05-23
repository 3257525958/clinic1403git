from django import forms
from it_app.models import homeimgmodel
class homeimgform(forms.ModelForm):
    class Meta:
        model = homeimgmodel
        fields = ('name','image',)
        labels = {'name':'نام',
                  'image':'آپلود عکس'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col s12','name':'name'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 loadlabel','hidden':"hidden", 'name':'img'}),
                   }
