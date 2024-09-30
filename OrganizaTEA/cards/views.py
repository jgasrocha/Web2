from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required


def card_list(request):
    cards = list(Card.objects.all())  
    total_slots = 50  
    placeholder_range = range(total_slots)  
    
    cards += [None] * (total_slots - len(cards))
    
    is_guest = not request.user.is_authenticated
    
    return render(request, 'cards/card_list.html', {
        'cards': cards,
        'is_guest': is_guest,
    })

@login_required
def card_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        professor_image = request.FILES['professor_image']
        location_image = request.FILES['location_image']
        description = request.POST['description']
        
        card = Card.objects.create(
            title=title,
            professor_image=professor_image,
            location_image=location_image,
            description=description,
            user=request.user 
        )
        return redirect('card_list')
    
    return render(request, 'cards/card_form.html')

@login_required
def card_management(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_management.html', {'cards': cards})

@login_required
def card_edit(request, pk):
    card = get_object_or_404(Card, pk=pk)
    
    if request.method == 'POST':
        card.title = request.POST['title']
        if request.FILES.get('professor_image'):
            card.professor_image = request.FILES['professor_image']
        if request.FILES.get('location_image'):
            card.location_image = request.FILES['location_image']
        card.description = request.POST['description']
        card.save()
        return redirect('card_list')
    
    return render(request, 'cards/card_form.html', {'card': card})


@login_required
def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('card_list')


