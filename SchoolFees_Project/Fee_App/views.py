from rest_framework import generics
from .models import Fee
from .serializers import FeeSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeeForm

class FeeListCreateView(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

def fee_list(request):
    fees = Fee.objects.all()
    return render(request, 'Fee_app/fee_list.html', {'fees': fees})

def add_fee(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeeForm()
    return render(request, 'Fee_app/fee_form.html', {'form': form})

def edit_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeeForm(instance=fee)
    return render(request, 'Fee_app/fee_form.html', {'form': form})

def delete_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        fee.delete()
        return redirect('fee_list')
    return render(request, 'Fee_app/fee_confirm_delete.html', {'fee': fee})