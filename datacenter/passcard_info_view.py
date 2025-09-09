from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .models import Visit


def passcard_info_view(request, passcode):
    # passcard = Passcard.objects.all()[0]
    # Программируем здесь
    # passcard = Visit.objects.filter(passcard__owner_name)
    # this_passcard_visits = [
    #     {
    #         'entered_at': '11-04-2018',
    #         'duration': '25:03',
    #         'is_strange': False
    #     },
    # ]
    # context = {
    #     'passcard': passcard,
    #     'this_passcard_visits': this_passcard_visits
    # }
    # return render(request, 'passcard_info.html', context)
    passcard = get_object_or_404(Passcard, passcode=passcode)

    # Извлекаем все визиты данного владельца пропуска
    visits = Visit.objects.filter(passcard=passcard)

    # Формируем представление визитов с необходимой информацией
    this_passcard_visits = []
    for visit in visits:
        # Форматируем начало визита
        entered_at = visit.entered_at.strftime('%Y-%m-%d %H:%M:%S')  # Год-Месяц-День Часы:Минуты:Секунды

        # Рассчитываем продолжительность визита
        duration = visit.get_duration()
        duration_in_minutes = int(duration.total_seconds() / 60)

        # Определяем, является ли визит странным/сомнительным
        is_strange = visit.is_visit_long()

        # Заполняем словарь для передачи в шаблон
        this_passcard_visits.append({
            'entered_at': entered_at,
            'duration': f'{duration_in_minutes} минут',
            'is_strange': is_strange
        })

    # Готовим контекст для шаблона
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)