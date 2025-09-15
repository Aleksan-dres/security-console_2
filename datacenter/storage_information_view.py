from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at__isnull=True)
    current_visitors = []
    for visit in current_visits:
        went_inside = visit.entered_at

        formatted_elapsed_time = visit.format_duration()

        current_visitors.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': went_inside,
            'duration': formatted_elapsed_time
        })

    context = {
        'non_closed_visits': current_visitors,
    }
    return render(request, 'storage_information.html', context)

