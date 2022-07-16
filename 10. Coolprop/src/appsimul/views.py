from django.shortcuts import render, redirect, HttpResponseRedirect
from api.calcul import Calcul_thermo

FLUID = ('R134a', 'R404a', 'R22', 'R12')


# Create your views here.
def index(request):
    return render(request, "simul/index.html", {"fluids": FLUID})


def cacul(request):
    try:
        fluid = str(request.POST.get('fluid'))
        t_cdr = float(request.POST.get("t_cdr"))
        t_o = float(request.POST.get('t_o'))
    except:
        return render(request, "simul/index.html", {"fluids": FLUID, "msg_err": "Données d'entrées manquantes ou érronés"})

    simul = Calcul_thermo(fluid, t_cdr, t_o, 2, 5)

    return render(request, "simul/index.html",
    {
        "results": simul.get_data(),
        "fluids": FLUID
    }
    )
