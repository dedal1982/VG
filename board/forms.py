from django import forms

from board.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        labels  = {"message": "Заявка"}
        fields  = ["message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 3, })}