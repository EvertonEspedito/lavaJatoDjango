from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def clientes (request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        #pegar dados do cliente
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        contato = request.POST.get('contato')
        #pegar dados do(s) veiculos do cliente
        tipos = request.POST.getlist('tipo')
        modelo = request.POST.getlist('modelo')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')
