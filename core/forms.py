import datetime
from django import forms
from .models import Expence, Income


class ExpenceForm(forms.Form):
    title = forms.CharField(max_length=100)
    amount = forms.IntegerField()
    date = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))

    def __init__(self, *args, **kwargs):
        super(ExpenceForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'value': datetime.date.today().strftime("%Y-%m-%d")})
    

    def save(self):
        data = self.cleaned_data
        obj = Expence(title=data['title'], amount=data['amount'], date=data['date'])
        obj.save()
        return obj



class IncomeForm(forms.Form):
    title = forms.CharField(max_length=100)
    amount = forms.IntegerField()
    date = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'value': datetime.date.today().strftime("%Y-%m-%d")})
    

    def save(self):
        data = self.cleaned_data
        obj = Income(title=data['title'], amount=data['amount'], date=data['date'])
        obj.save()
        return obj
    