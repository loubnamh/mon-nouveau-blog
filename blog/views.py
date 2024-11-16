from django.shortcuts import render,get_object_or_404, redirect
from .models import visiteur, attraction
from .forms import MoveForm

def post_list(request):
    # Récupérer tous les personnages et lieux
    visiteurs = visiteur.objects.all()
    attractions = attraction.objects.all()

    # Rendre la page avec les données
    return render(request, 'blog/post_list.html', {
        'Visiteurs': visiteurs ,
        'Attractions':attractions,
        })








'''def visiteur_detail(request, id_visiteur):
    # Récupère le visiteur spécifié ou retourne une erreur 404
    visiteur_instance = get_object_or_404(visiteur, id_visiteur=id_visiteur)
    ancienne_attraction = visiteur_instance.attraction

    message = ""  # Initialisation du message vide

    if request.method == "POST":
        form = MoveForm(request.POST, instance=visiteur_instance)
        if form.is_valid():
            # Sauvegarder l'instance du visiteur sans encore la valider en base
            visiteur_instance = form.save(commit=False)
            # Sauvegarder l'ancienne attraction
            ancienne_attraction = get_object_or_404(attraction, id_attraction=visiteur_instance.attraction.id_attraction)

            # Mettre à jour le nombre actuel de visiteurs dans l'ancienne attraction
            ancienne_attraction.retirer_visiteur()

            # Récupérer la nouvelle attraction choisie dans le formulaire
            nouvelle_attraction = visiteur_instance.attraction

            # Vérifier si la nouvelle attraction est disponible
            if nouvelle_attraction.est_disponible() and nouvelle_attraction.etat == "ouverte":
                # Vérifier la compatibilité entre l'état du visiteur et la nouvelle attraction
                if visiteur_instance.etat == "fatigué" and nouvelle_attraction.nom == "Zones de Repos":
                    visiteur_instance.etat = "affamé"
                elif visiteur_instance.etat == "affamé" and nouvelle_attraction.nom == "Zones de Restauration":
                    visiteur_instance.etat = "enjoué"
                elif visiteur_instance.etat == "enjoué" and nouvelle_attraction.nom == "Attractions Légères":
                    visiteur_instance.etat = "prêt"
                elif visiteur_instance.etat == "prêt" and nouvelle_attraction.nom == "Attraction Intense":
                    visiteur_instance.etat = "fatigué"
                else:
                    # Si l'état du visiteur n'est pas compatible avec la nouvelle attraction, un message d'erreur est affiché
                    message = "L'état du visiteur n'est pas compatible avec l'attraction choisie."
                    return render(request, 'blog/visiteur_detail.html', {
                        'visiteur': visiteur_instance,
                        'attraction': ancienne_attraction,
                        'form': form,
                        'message': message  # On passe le message à la vue
                    })
                
                # Mettre à jour l'attraction du visiteur et l'état
                visiteur_instance.changer_etat(visiteur_instance.etat, nouvelle_attraction)
                
                # Sauvegarder la modification dans la base de données
                visiteur_instance.save()
                # Ajouter le visiteur à la nouvelle attraction
                nouvelle_attraction.ajouter_visiteur()

                # Rediriger vers la page de détails du visiteur après le changement
                return redirect('visiteur_detail', id_visiteur=id_visiteur)
            else:
                # Si la nouvelle attraction n'est pas disponible ou n'est pas ouverte
                message = "La nouvelle attraction n'est pas disponible ou ouverte."
                return render(request, 'blog/visiteur_detail.html', {
                    'visiteur': visiteur_instance,
                    'attraction': ancienne_attraction,
                    'form': form,
                    'message': message  # On passe le message à la vue
                })
    else:
        form = MoveForm(instance=visiteur_instance)

    return render(request, 'blog/visiteur_detail.html', {
        'visiteur': visiteur_instance,
        'attraction': ancienne_attraction,
        'form': form,
        'message': message  # On passe le message à la vue
    })'''
from django.shortcuts import render, get_object_or_404, redirect
from .models import visiteur, attraction
from .forms import MoveForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import visiteur, attraction
from .forms import MoveForm

def visiteur_detail(request, id_visiteur):
    # Récupère le visiteur spécifié ou retourne une erreur 404
    visiteur_instance = get_object_or_404(visiteur, id_visiteur=id_visiteur)
    ancienne_attraction = visiteur_instance.attraction

    message = ""  # Initialisation du message vide, il sera utilisé pour l'affichage d'erreur

    if request.method == "POST":
        form = MoveForm(request.POST, instance=visiteur_instance)
        if form.is_valid():
            # Sauvegarder l'instance du visiteur sans encore la valider en base
            visiteur_instance = form.save(commit=False)
            # Sauvegarder l'ancienne attraction
            ancienne_attraction = get_object_or_404(attraction, id_attraction=visiteur_instance.attraction.id_attraction)

            # Vérifier si la nouvelle attraction est disponible
            nouvelle_attraction = visiteur_instance.attraction

            if nouvelle_attraction.est_disponible() and nouvelle_attraction.etat == "ouverte":
                # Vérifier la compatibilité entre l'état du visiteur et la nouvelle attraction
                if visiteur_instance.etat == "fatigué" and nouvelle_attraction.nom == "Zones de Repos":
                    # L'état 'fatigué' est compatible avec la "Zone de Repos"
                    visiteur_instance.etat = "affamé"
                elif visiteur_instance.etat == "affamé" and nouvelle_attraction.nom == "Zones de Restauration":
                    # L'état 'affamé' est compatible avec les "Zones de Restauration"
                    visiteur_instance.etat = "enjoué"
                elif visiteur_instance.etat == "enjoué" and nouvelle_attraction.nom == "Attractions Légères":
                    # L'état 'enjoué' est compatible avec les "Attractions Légères"
                    visiteur_instance.etat = "prêt"
                elif visiteur_instance.etat == "prêt" and nouvelle_attraction.nom == "Attraction Intense":
                    # L'état 'prêt' est compatible avec "Attraction Intense"
                    visiteur_instance.etat = "fatigué"
                else:
                    # Si l'état du visiteur n'est pas compatible avec la nouvelle attraction, ne pas déplacer et afficher le message
                    message = "L'état du visiteur n'est pas compatible avec l'attraction choisie."
                    # Ne pas changer l'attraction et retourner au template avec le message
                    return render(request, 'blog/visiteur_detail.html', {
                        'visiteur': visiteur_instance,
                        'attraction': ancienne_attraction,
                        'form': form,
                        'message': message  # On passe le message à la vue
                    })

                # Si l'état est compatible, on change l'attraction et l'état du visiteur
                visiteur_instance.changer_etat(visiteur_instance.etat, nouvelle_attraction)

                # Sauvegarder la modification dans la base de données
                visiteur_instance.save()
                # Ajouter le visiteur à la nouvelle attraction
                nouvelle_attraction.ajouter_visiteur()

                # Rediriger vers la page de détails du visiteur après le changement
                return redirect('visiteur_detail', id_visiteur=id_visiteur)
            else:
                # Si la nouvelle attraction n'est pas disponible ou n'est pas ouverte
                message = "La nouvelle attraction n'est pas disponible ou ouverte."
                # Retourner au template avec le message d'erreur
                return render(request, 'blog/visiteur_detail.html', {
                    'visiteur': visiteur_instance,
                    'attraction': ancienne_attraction,
                    'form': form,
                    'message': message  # On passe le message à la vue
                })

    else:
        form = MoveForm(instance=visiteur_instance)

    return render(request, 'blog/visiteur_detail.html', {
        'visiteur': visiteur_instance,
        'attraction': ancienne_attraction,
        'form': form,
        'message': message  # On passe le message à la vue
    })
