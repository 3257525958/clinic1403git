from django import forms
from it_app.models import homeimgmodel
class homeimgform(forms.ModelForm):
    class Meta:
        model = homeimgmodel
        fields = ('name','image',)
        labels = {'name':'نام',
                  'image':'آپلود'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','name':'name'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 m-100','hidden':"hidden", 'name':'img'}),
                   }
