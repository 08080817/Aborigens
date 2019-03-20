from django.shortcuts import render
from contact.forms import CriarContatoForm

# Create your views here.
def contact(request):

    # formulario = CriarContatoForm(request.POST or None)

    # if formulario.is_valid():
    #     formulario.save()
    #     formulario = CriarContatoForm()

    # context = {
    #     'form': formulario
    # }

    return render(request, 'contact.html')