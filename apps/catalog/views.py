from django.shortcuts import render

def books_list_placeholder(request):
    return render(request, "catalog/books_list_placeholder.html")
