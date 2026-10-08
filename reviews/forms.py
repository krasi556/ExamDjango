from django import forms
from django.core.exceptions import ValidationError

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
            'placeholder': 'Feedback about our AI agents',
            'rows': 2
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

    def clean_text(self):
        text = self.cleaned_data.get('text').strip()
        if text.isupper():
            raise ValidationError("Our AI agents are trying to sleep, don't yell")
        return text


class CreateReview(ReviewForms):
    pass


class DeleteReview(ReviewForms):
    pass


class EditReview(ReviewForms):
    pass
