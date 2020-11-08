from django.shortcuts import render, redirect
from Books.models import Book
from Books.forms import BookCreateForm,BookUpdate

# Create your views here.

def bookCreate(request):
    template_name="bookCreate.html"
    form=BookCreateForm()
    context= {}
    books=Book.objects.all()
    context["books"]=books
    context["form"] = form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():

        #   book_name=form.cleaned_data.get("book_name")
         #   author=form.cleaned_data.get("author")
         #   price=form.cleaned_data.get("price")
         #   pages=form.cleaned_data.get("pages")

         #   obj=Book(book_name=book_name,author=author,price=price,pages=pages)
         #   obj.save()
          #  qs=Book.objects.all()
          #  context["books"]=qs
          #  return render(request, template_name, context)

            form.save()
            return redirect("create")

        else:
            context["form"]=form
            return render(request,template_name,context)
    return render(request, template_name, context)

def listBook(request):
    template_name="list.html"
    qs=Book.objects.all()
    context={}
    context["books"]=qs
    return render(request,template_name,context)

def viewBook(request,bb):
    template_name="book.html"
    qs=Book.objects.get(id=bb)
    context={}
    context["book"]=qs
    return render(request,template_name,context)

def deleteBook(request,bb):
    qs = Book.objects.get(id=bb).delete()
    return redirect("create")

def updateBook(request,bb):
    book=Book.objects.get(id=bb)
    form = BookUpdate(instance=book)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BookUpdate(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("create")

    return render(request,"bookupdate.html",context)


