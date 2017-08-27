from django.shortcuts import render

# Create your views here.
def ebook(request):
    return render(request,'blog/ebook.html',{})
