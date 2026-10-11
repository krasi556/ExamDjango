from django import forms


class TotallyLegitForm(forms.Form):
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Let us know how you feel...',
        }),
        error_messages={'required': 'Tokens are becoming expensive..'}
    )
    email_address = forms.EmailField(required=True,
                                     label='Leave your email here',
                                     error_messages={'required': 'Don"t try being sneaky here!',
                                                     'invalid': 'Nono, do try a valid one'})
