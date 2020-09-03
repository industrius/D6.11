from django import forms
from .models import Author, Book, Publisher, Friend
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, label="Имя автора")
    class Meta:
        model = Author
        fields = "__all__"

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Название")
    ISBN = forms.IntegerField(label="Книжный номер")
    copy_count = forms.IntegerField(label="Количество")
    class Meta:
        model = Book
        fields = "__all__"

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = "__all__"