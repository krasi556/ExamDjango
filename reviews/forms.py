from django import forms

from reviews.models import Review


class ReviewForms(forms.ModelForm):
    author = forms.CharField(max_length=100)

    class Meta:
        model = Review
        fields = ['author', 'rating', 'text']

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author or not author.strip():
            return 'Anonymous'
        return author
