from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit 


    

def storage_information_view(request):
    
    at_the_entrance = Visit.objects.filter( leaved_at__isnull=True)

    results = []
    for visit in at_the_entrance: 
        entered_original = visit.entered_at 
        elapsed_time = visit.get_duration()  
        
        formatted_elapsed_time = visit.format_duration()
        
        results.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_original , 
            'duration': formatted_elapsed_time 
        })
         
    
    
    
    context = {
        'non_closed_visits': results,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


