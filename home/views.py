from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book

# Create your views here.
def index(request):
    data={
        "obj":Book.objects.all()
    }
    return render(request,'index.html',data)
def generic(request):
    return render(request,'generic.html')
def lists(request):
    books = Book.objects.all()
    return render(request, 'lists.html', {'books': books})


def add(request):
    if request.method == "POST":
        # Retrieve form data
        head = request.POST.get('head')
        para = request.POST.get('para')
        coverphoto = request.FILES.get('image')

        # Validate form data
        if not head or not para:
            messages.error(request, "Please provide both a head and a para.")
            return redirect("add")

        # Check if a file is uploaded
        if coverphoto:
            # Save book details with cover photo
            query = Book(head=head, para=para, coverphoto=coverphoto)
        else:
            # Save book details without cover photo
            query = Book(head=head, para=para)

        query.save()
       
        

    return render(request, 'add.html')


def delete(request,id):
    dlt=Book.objects.get(id=id)
    dlt.delete()
    return redirect("/")



from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def edit(request, id):
    if request.method == "POST":
        head = request.POST.get('head')
        para = request.POST.get('para')
        coverphoto = request.FILES.get('image')

        # Retrieve the book object to edit or return 404 if not found
        edit_book = get_object_or_404(Book, id=id)

        # Update book attributes
        edit_book.head = head
        edit_book.para = para
        edit_book.coverphoto = request.FILES.get('image')

        
    

        # Check if a new cover photo is uploaded
        if coverphoto:
            edit_book.coverphoto = coverphoto

        # Save the changes
        edit_book.save()

        # Redirect to the homepage or any other appropriate page
        return redirect("/")
    else:
        # Render the edit form with the book data or return 404 if not found
        book = get_object_or_404(Book, id=id)
        data = {"obj": book}
        return render(request, 'edit.html', data)



def detailed(request,id):
    data={
        "objs":Book.objects.get(id=id)
        
    }
    return render(request,'details.html',data)