from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at is None:
            current_time = timezone.now()
            return current_time - self.entered_at
        else:
            return self.leaved_at - self.entered_at

    def format_duration(self):
        duration = self.get_duration()
        total_seconds = duration.total_seconds()
        hours_of_visit = int(total_seconds // 3600)
        minutes_of_visit = int((total_seconds % 3600) // 60)
        return f"{hours_of_visit} ч {minutes_of_visit} мин"

    def is_visit_long(self, minutes_of_visit=60):
        duration = self.get_duration()
        return duration.total_seconds() / 60 >= minutes_of_visit
