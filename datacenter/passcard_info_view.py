from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .models import Visit


SECONDS_IN_MINUTE = 60


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        entered_at = visit.entered_at.strftime('%Y-%m-%d %H:%M:%S')
        duration = visit.get_duration()
        duration_in_minutes = int(duration.total_seconds() / SECONDS_IN_MINUTE)
        is_strange = visit.is_visit_long()
        this_passcard_visits.append({
            'entered_at': entered_at,
            'duration': f'{duration_in_minutes} минут',
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
