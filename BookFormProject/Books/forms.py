from django import forms
from Books.models import Book
from django.forms import ModelForm
#class BookCreateForm(ModelForm):

  #  book_name = forms.CharField(max_length=120)
  #  author = forms.CharField(max_length=120)
   # price = forms.IntegerField()
   # pages = forms.IntegerField()
class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data=super().clean()
        book_name=cleaned_data.get('book_name')
        price=cleaned_data.get('price')
        pages=cleaned_data.get('pages')
        book=Book.objects.filter(book_name=book_name)
        if book:
            msg="Book with same name already exist"
            self.add_error('book_name',msg)

        if price<100:
            msg = "Book with this price does  not exist"
            self.add_error('price', msg)

        if pages<=50:
            msg = "Page Number Should greater"
            self.add_error('book_name', msg)


class BookUpdate(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"




