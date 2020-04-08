from django import forms


# adds new todo list
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200) # optional args
    check = forms.BooleanField(required=False)