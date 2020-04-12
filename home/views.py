from django.shortcuts import render ,redirect
from .models import Detail
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url="/")
def home(request):
        data = Detail.objects.filter(Uid = request.user.id)
        return render(request, 'home.html',{'data':data})

@login_required(login_url="/")
def add(request):
        if request.method == 'POST':
                Uid = request.user.id
                Title = request.POST['title']
                Author = request.POST['author']
                Url = request.POST['url']
                Genre = request.POST['genre']
                data = Detail(Uid=Uid, Title=Title, Author=Author, Url=Url, Genre=Genre)
                data.save()
                messages.info(request, 'Book Added to you Fav list :)')
                return redirect('home')
        else:
                return render(request, 'add.html')


@login_required(login_url="/")
def update(request,id):
        book = Detail.objects.get(id=id)
        if request.method == "POST":

            book.Title = request.POST['title']
            book.Author = request.POST['author']
            book.Genre = request.POST['genre']
            book.Url = request.POST['url']
            book.save()
            messages.info(request, 'Successfully Updated..')
            return redirect('home')
        else:
                return render(request, 'update.html', {'book': book})

@login_required(login_url="/")
def delete(request, id):
        book = Detail.objects.get(id=id)
        book.delete()
        return redirect('home')


