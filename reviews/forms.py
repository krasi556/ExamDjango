from django import forms

from reviews.models import Review


class ReviewForms(forms.ModelForm):
    author = forms.CharField(max_length=100,
                             required=False,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'As Anonymous'
                             }))
    text = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={
            'placeholder': 'Feedback about our AI agents'
        }),
    )


    class Meta:
        model = Review
        fields = ['author', 'rating', 'text']



    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author or not author.strip():
            return 'Anonymous'
        return author
