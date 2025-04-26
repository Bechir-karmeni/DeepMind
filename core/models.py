from django.db import models
from django.utils import timezone

class AnonymousSubmission(models.Model):
    submission_id = models.CharField(max_length=100, unique=True)
    phq9_score = models.IntegerField()
    gad7_score = models.IntegerField()
    mbi_score = models.IntegerField()
    combined_report = models.TextField()
    sector = models.CharField(max_length=100, default='Général')  # 🆕 champ ajouté
    submitted_at = models.DateTimeField(default=timezone.now)
    has_quit = models.BooleanField(default=False)

    def __str__(self):
        return f'Submission {self.submission_id}'
