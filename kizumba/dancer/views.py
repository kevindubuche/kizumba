from django.shortcuts import render
from .models import Dancer

# Create your views here.
def index(request):
    context = {
        "dancers": Dancer.objects.all()
    }
    return render(request, "dancers/index.html", context)
