from django.db import models
from utilisateurs.models import Utilisateur

class DossierMedical(models.Model):
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='dossiers_patient')
    medecin = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, related_name='dossiers_medecin')
    date_creation = models.DateTimeField(auto_now_add=True)
    diagnostic = models.TextField()
    traitement = models.TextField()

    def __str__(self):
        return f"Dossier de {self.patient.username} - {self.date_creation.date()}"
