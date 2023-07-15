from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField()
    recipient_email = forms.EmailField()
