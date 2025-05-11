from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Veiculo
import re
from django.shortcuts import redirect

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

        #Validar Placa
        veiculoPlaca = Veiculo.objects.filter(placa=placa)
        if veiculoPlaca.exists():
            #TODO: Adicionar mensagens
            return render(request, 'clientes.html',{'modelo':modelo, 'tipo':tipo,'ano':ano})

        #Validar CPF e EMAIL
        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            #TODO: Adicionar mensagens
            return render(request, 'clientes.html',{'nome':nome, 'sobrenome':sobrenome,'email':email,'contato':contato})
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            #TODO: Adicionar mensagens
            return render(request, 'clientes.html',{'nome':nome, 'sobrenome':sobrenome,'cpf':cpf,'contato':contato}) 
        

        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf,
            contato=contato
        )
        cliente.save()

        for tipo, modelo, placa, ano in zip(tipos, modelos, placas, anos):
            print("Salvando veículo:", tipo, modelo, placa, ano)  # DEBUG
            
            veic = Veiculo(
                tipo=tipo,
                modelo=modelo,
                placa=placa,
                ano=ano,
                cliente=cliente
            )
            veic.save()
        
        #Renderizar template
        return redirect('/clientes/')

