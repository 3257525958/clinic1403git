from django import forms
from it_app.models import homeimgmodel,homemenosarimodel,homemobilemodel
class homeimgform(forms.ModelForm):
    class Meta:
        model = homeimgmodel
        fields = ('name','image',)
        labels = {'name':'نام:',
                  'image':'آپلود عکس'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col s12','name':'name'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
                   }


class homemenosariform(forms.ModelForm):
    class Meta:
        model = homemenosarimodel
        fields = ('name','image',)
        labels = {'name':'نام:',
                  'image':'آپلود عکس'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col s12','name':'name'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
                   }
class homemobileform(forms.ModelForm):
    class Meta:
        model = homemobilemodel
        fields = ('name','image',)
        labels = {'name':'نام:',
                  'image':'آپلود عکس'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col s12','name':'name'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
        }
