from django.shortcuts import render

def toppage(request):
    return render(request, 'toppage.html', {})

def main(request):
    return render(request, 'mainpage.html', {})
