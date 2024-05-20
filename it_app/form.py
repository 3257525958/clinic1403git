from django import forms
from it_app.models import homeimgmodel
class homeimgform(forms.ModelForm):
    class Meta:
        model = homeimgmodel
        fields = ('image','name',)

# # class mform(forms.ModelForm):
# #
# #     class Meta:
# #         model = homeimgmodel
# #         exclude = ('image'),
# #         labels = {
# #             "namelabel": (": انتخاب موضوع"),
# #             "imagelabel": ("انتخاب عکس"),
# #         }
# #         widgets = {
# #             "name":forms.Textarea(attrs = {"class":"form-control p-4","style":"text-align: right",}),
# #             # "image": forms.ImageField(),
# #
# #             # "cc":forms.Textarea(attrs = {"class":"form-control p-4","style":"text-align: right",}),
# #             # "pmh":forms.CheckboxSelectMultiple(choices=pmh),
# #             # "consentletter":forms.CheckboxSelectMultiple(choices=con),
# #         }
# #
# class mform(forms.Form):
#     name = forms.CharField(max_length=100, label='اسم فایل مورد نظر را وارد کنید')
#     image = forms.ImageField(label="سلام")
