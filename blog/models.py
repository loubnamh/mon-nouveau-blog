from django.db import models


class attraction(models.Model):
    id_attraction = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    etat = models.CharField(
        max_length=20,
        choices=[
            ("ouverte", "Ouverte"),
            ("fermée", "Fermée"),
        ],
    )
    capacitemaximal = models.PositiveIntegerField(default=0)
    nbractuelle = models.PositiveIntegerField(default=0)
    photo = models.CharField(max_length=200)

    def est_disponible(self):
        """Vérifie si l'attraction a encore de la capacité."""
        return self.nbractuelle < self.capacitemaximal

    def ajouter_visiteur(self):
        """Ajoute un visiteur à l'attraction si elle n'est pas pleine."""
        if self.est_disponible() and self.etat == "ouverte":
            self.nbractuelle += 1
            self.save()

    def retirer_visiteur(self):
        """Retire un visiteur de l'attraction."""
        if self.nbractuelle > 0:
            self.nbractuelle -= 1
            self.save()

    def __str__(self):
        return self.nom

    @property
    def liste_visiteurs(self):
        """Retourne les visiteurs actuellement dans l'attraction."""
        return visiteur.objects.filter(attraction=self)


class visiteur(models.Model):
    id_visiteur = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    etat = models.CharField(
        max_length=20,
        choices=[
            ("fatigué", "Fatigué"),
            ("prêt", "Prêt"),
            ("affamé", "Affamé"),
            ("enjoué", "Enjoué"),
        ],
    )
    attraction = models.ForeignKey(attraction, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)

    
    def changer_etat(self, nouvel_etat, nouvelle_attraction):

        if nouvelle_attraction.est_disponible() and nouvelle_attraction.etat == "ouverte":
            self.etat = nouvel_etat
            if self.attraction:
                self.attraction.retirer_visiteur()
                self.attraction = nouvelle_attraction
                nouvelle_attraction.ajouter_visiteur()
                self.save() 

    
    def transition_etat(self, nouvelle_attraction):
    
        transitions = {
            "fatigué": ("affamé", "Zones de Repos"),
            "affamé": ("enjoué", "Zones de Restauration"),
            "enjoué": ("prêt", "Attractions Légères"),
            "prêt": ("fatigué", "Attraction Intense"),
        }
    
    
        if self.etat in transitions:
            nouvel_etat, nom_attraction = transitions[self.etat]

            try:
            
                nouvelle_attractionA = attraction.objects.get(nom=nom_attraction)
            except attraction.DoesNotExist:
            
                print(f"L'attraction '{nom_attraction}' n'existe pas.")
                return
         

            if nouvelle_attractionA.est_disponible() and nouvelle_attractionA.etat == "ouverte" and nouvelle_attraction.nom==nouvelle_attractionA.nom:
            
                if self.etat == "fatigué" and nom_attraction == "Zones de Repos":
               
                    self.etat = nouvel_etat
                
                    self.changer_etat(nouvel_etat, nouvelle_attraction)
                elif self.etat == "affamé" and nom_attraction == "Zones de Restauration":
               
                    self.etat = nouvel_etat
                
                
                    self.changer_etat(nouvel_etat, nouvelle_attraction)
                elif self.etat == "enjoué" and nom_attraction == "Attractions Légères":
               
                    self.etat = nouvel_etat
                
                    self.changer_etat(nouvel_etat, nouvelle_attraction)
                elif self.etat == "prêt" and nom_attraction == "Attraction Intense":
                
                    self.etat = nouvel_etat
                
                    self.changer_etat(nouvel_etat, nouvelle_attraction)
                else:
                    print(f"L'état '{self.etat}' du visiteur n'est pas compatible avec l'attraction '{nom_attraction}'")
            

    def __str__(self):
        return self.nom
