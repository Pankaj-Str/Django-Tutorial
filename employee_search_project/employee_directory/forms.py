from django import forms

class EmployeeSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Employee')
