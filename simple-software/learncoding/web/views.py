from django.shortcuts import render

def index(requet):
    return render(requet, 'index.html', {})