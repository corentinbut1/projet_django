from django.shortcuts import render, get_object_or_404
from computerApp.models import Machine
from computerApp.models import Personnel
from computerApp.forms import AddMachineForm
from computerApp.forms import AddPersonnelForm
from computerApp.forms import DeleteMachineForm
from computerApp.forms import DeletePersonnelForm
from computerApp.forms import UpdateMachineForm
from  django.shortcuts import redirect

# Create your views here
def index(request) :
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines': machines,
        'personnels': personnels,

    }

    return render(request, 'index.html', context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'],
                                type=form.cleaned_data['type'],
                                ip=form.cleaned_data['ip'],
                                etat=form.cleaned_data['etat'],
                                date_maintenance=form.cleaned_data['date_maintenance'])
            new_machine.save()   
            return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/machine_add.html', context)

def machine_list_view(request) :
    machines = Machine.objects.order_by('-mise_a_jour')
    context={'machines': machines}
    return render(request, 'computerApp/machine_list.html', context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    form = UpdateMachineForm(request.POST)
    if request.method == 'POST':
        form = UpdateMachineForm(request.POST)
        if form.is_valid():
            machine.etat = form.cleaned_data['etat']
            machine.save()
            return redirect('machine-detail', pk=machine.id)
    else:
        form = UpdateMachineForm(initial={'etat': machine.etat})
    context = {'machine': machine, 'form': form}
    return render(request, 'computerApp/machine_detail.html', context)

def delete_machine(request):
    if request.method == 'POST':
        form = DeleteMachineForm(request.POST)
        if form.is_valid():
            form.delete_machine()
            return redirect('machines')
    else:
        form = DeleteMachineForm()
        context = {'form': form}
    return render(request, 'computerApp/machine_delete.html', context)

def personnel_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personnel = Personnel(nom=form.cleaned_data['nom'],
                                type=form.cleaned_data['type'])
            new_personnel.save()   
            return redirect('personnels')
    else:
        form = AddPersonnelForm()
        context = {'form': form}
        return render(request, 'computerApp/personnel_add.html', context)

def personnel_detail_view(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    context={'personnel': personnel}
    return render(request, 'computerApp/personnel_detail.html', context)

def personnel_list_view(request):
    personnels = Personnel.objects.all()
    context={'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)

def delete_personnel(request):
    if request.method == 'POST':
        form = DeletePersonnelForm(request.POST)
        if form.is_valid():
            form.delete_personnel() 
            return redirect('personnels')
    else:
        form = DeletePersonnelForm()
        context = {'form': form}
    return render(request, 'computerApp/personnel_delete.html', context)


        