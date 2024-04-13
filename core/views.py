from django.shortcuts import render, redirect
from.models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()[:10]
    return render(request,"index.html", {"pessoas":pessoas})

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"home.html", {"pessoas":pessoas})

def criar(request):
    vnome = request.POST.get("nome")
    vdataNasc = request.POST.get("dataNasc")
    vemail = request.POST.get("email")
    vpaisDesejado = request.POST.get("paisDesejado")
    Pessoa.objects.create(nome=vnome, dataNasc = vdataNasc, email=vemail, paisDesejado=vpaisDesejado)
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def atualizar(request, id):
     vnome = request.POST.get("nome")
     vdataNasc = request.POST.get("dataNasc")
     vemail = request.POST.get("email")
     vpaisDesejado = request.POST.get("paisDesejado")
     pessoa = Pessoa.objects.get(id=id)
     pessoa.nome = vnome
     pessoa.dataNasc = vdataNasc
     pessoa.email = vemail
     pessoa.paisDesejado = vpaisDesejado
     pessoa.save()
     return redirect(home)

def deletar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def pesquisar(request):
    vnome = request.GET.get("nomePesquisa")
    pessoas = Pessoa.objects.filter(nome=vnome)
    return render(request, "index.html", {"pessoas": pessoas})

def mostrarTodes(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html", {"pessoas":pessoas})