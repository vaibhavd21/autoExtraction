from django.shortcuts import render
from rest_framework import viewsets
from .models import data
from .serializers import dataSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import MyModelForm

# Create your views here.
class dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = data.objects.all()
    serializer_class = dataSerializer

def my_form(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyModelForm()
    return render(request, 'mainForm.html', {'form': form})