from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Veiculo

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
        modelos = request.POST.getlist('modelo')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf,
            contato=contato
        )
        cliente.save()

        for tipo, modelo, placa, ano in zip(tipos, modelos, placas, anos):
            veic = Veiculo(tipo =tipo, modelo=modelo, placa=placa, ano=ano, cliente=cliente)
            veic.save()
        
        #Renderizar template
        return HttpResponse('teste')

