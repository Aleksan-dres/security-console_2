from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit


def storage_information_view(request):
    inside_the_storage = Visit.objects.filter(leaved_at__isnull=True)
    inside = []
    for visit in inside_the_storage:
        went_inside = visit.entered_at

        formatted_elapsed_time = visit.format_duration()

        inside.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': went_inside,
            'duration': formatted_elapsed_time
        })

    context = {
        'non_closed_visits': inside,
    }
    return render(request, 'storage_information.html', context)

