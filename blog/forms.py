from django import forms
from .models import visiteur

class MoveForm(forms.ModelForm):
    
    class Meta:
        model = visiteur
        fields = ('attraction',)
        labels = {
            'attraction': "Nouvelle Attraction",
        }
        widgets = {
            'attraction': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
    def save(self, commit=True):
        visiteur = super().save(commit=False)
        visiteur.transition_etat()
        if commit:
            visiteur.save()
        return visiteur