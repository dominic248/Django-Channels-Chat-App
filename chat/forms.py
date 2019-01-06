from django import forms


class ComposeForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type a message...'}))

    def __init__(self, *args, **kwargs):
        super(ComposeForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = False