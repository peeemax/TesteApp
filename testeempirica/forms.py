from django import forms


class UploadFileForm(forms.Form):
    csv_upload  = forms.FileField()