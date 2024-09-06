from django import forms
from accountancy_app.models import esmekalamodel
class esmekalaiform(forms.ModelForm):
    class Meta:
        model = esmekalamodel
        fields = ('jobid',
                  'esmekala',
                  'berand',
                  'unit',
                  'value',
                  'image')
        labels = {
                  'jobid':'نام خدمت:',
                  'esmekala':'نام کالا:',
                  'berand': 'برند:',
                  'unit': 'نوع واحد:',
                  'value': 'حجم:',
                  'image':'آپلود عکس',
                  }
        widgets = {
            'jobid': forms.TextInput(attrs={'class':'form-control col s12','name':'jobid'}),
            'esmekala': forms.TextInput(attrs={'class':'form-control col s12','name':'esmekala'}),
            'berand': forms.TextInput(attrs={'class':'form-control col s12','name':'berand'}),
            'unit': forms.TextInput(attrs={'class':'form-control col s12','name':'unit'}),
            'value': forms.TextInput(attrs={'class':'form-control col s12','name':'value'}),
            'image':forms.FileInput(attrs={'class':'w-100 btn waves-effect col s6 mt-5', 'name':'img'}),
                   }
