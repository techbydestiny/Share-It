from django import render, redirect

def index_page(request):
    render("index.html")