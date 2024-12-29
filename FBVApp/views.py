from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from forms import PlayerForm
from FBVApp.models import PlayerModel

def create_view(request):
    context = {}

    form = PlayerForm(request.POST or None)

    if form.is_valid(): 
        form.save() # Data stored 
    
    context['form'] = form 

    return render(request,'create_view.html',context) 

def list_view(request): 
    context = {}

    context['dataset'] = PlayerModel.objects.all() 

    return render(request,'list_view.html',context)

def detail_view(request,id): 
    context = {}

    context['Player'] = PlayerModel.objects.get(id = id)

    return render(request,'detail_view.html',context)

def update_view(request,id): 
    context = {}

    obj = get_object_or_404(PlayerModel,id = id)

    form = PlayerForm(request.POST or None, instance= obj) 

    if form.is_valid(): 
        form.save()
        return HttpResponseRedirect("/") 

    context['form'] = form 

    return render(request, 'update_view.html',context) 

def delete_view(request,id): 
    context = {}
    obj = get_object_or_404(PlayerModel,id = id)

    if request.method == 'POST': 
        obj.delete() 
        return HttpResponseRedirect("PlayersList/")

    return render(request, 'delete_view.html',context)