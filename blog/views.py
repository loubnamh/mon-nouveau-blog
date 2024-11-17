from django.shortcuts import render,get_object_or_404, redirect
from .models import visiteur, attraction
from .forms import MoveForm

def post_list(request):
    
    visiteurs = visiteur.objects.all()
    attractions = attraction.objects.all()

    
    return render(request, 'blog/post_list.html', {
        'Visiteurs': visiteurs ,
        'Attractions':attractions,
        })


def visiteur_detail(request, id_visiteur):
    
    visiteur_instance = get_object_or_404(visiteur, id_visiteur=id_visiteur)
    ancienne_attraction = visiteur_instance.attraction

    message = ""  

    if request.method == "POST":
        form = MoveForm(request.POST, instance=visiteur_instance)
        if form.is_valid():
            
            visiteur_instance = form.save(commit=False)
            
            ancienne_attraction = get_object_or_404(attraction, id_attraction=visiteur_instance.attraction.id_attraction)

            
            nouvelle_attraction = visiteur_instance.attraction
            

            if nouvelle_attraction.est_disponible() and nouvelle_attraction.etat == "ouverte":
                
                if visiteur_instance.etat == "fatigué" and nouvelle_attraction.nom == "Zones de Repos":
                   
                    visiteur_instance.etat = "affamé"
                elif visiteur_instance.etat == "affamé" and nouvelle_attraction.nom == "Zones de Restauration":
                    
                    visiteur_instance.etat = "enjoué"
                elif visiteur_instance.etat == "enjoué" and nouvelle_attraction.nom == "Attractions Légères":
                    
                    visiteur_instance.etat = "prêt"
                elif visiteur_instance.etat == "prêt" and nouvelle_attraction.nom == "Attraction Intense":
                    
                    visiteur_instance.etat = "fatigué"
                else:
                    
                    message = "L'état du visiteur n'est pas compatible avec l'attraction choisie."
                    
                    return render(request, 'blog/visiteur_detail.html', {
                        'visiteur': visiteur_instance,
                        'attraction': ancienne_attraction,
                        'form': form,
                        'message': message 
                    })

                
                visiteur_instance.changer_etat(visiteur_instance.etat, nouvelle_attraction)

                
                visiteur_instance.save()
                
                nouvelle_attraction.ajouter_visiteur()

                
                return redirect('visiteur_detail', id_visiteur=id_visiteur)
            else:
                
                message = "La nouvelle attraction n'est pas disponible ou ouverte."
               
                return render(request, 'blog/visiteur_detail.html', {
                    'visiteur': visiteur_instance,
                    'attraction': ancienne_attraction,
                    'form': form,
                    'message': message  
                })

    else:
        form = MoveForm(instance=visiteur_instance)

    return render(request, 'blog/visiteur_detail.html', {
        'visiteur': visiteur_instance,
        'attraction': ancienne_attraction,
        'form': form,
        'message': message  
    })
