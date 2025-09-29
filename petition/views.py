from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Petition, PetitionVote

def index(request):
    """List all petitions"""
    petitions = Petition.objects.all().order_by("-created_at")
    template_data = {
        "title": "Petitions",
        "petitions": petitions
    }
    return render(request, "petition/index.html", {"template_data": template_data})


def show(request, id):
    """Show a single petition and votes"""
    petition = get_object_or_404(Petition, id=id)
    user_has_voted = False
    if request.user.is_authenticated:
        user_has_voted = PetitionVote.objects.filter(petition=petition, user=request.user).exists()

    template_data = {
        "title": petition.title,
        "petition": petition,
        "user_has_voted": user_has_voted
    }
    return render(request, "petition/show.html", {"template_data": template_data})


@login_required
def create(request):
    """Create a new petition"""
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        movie_name = request.POST.get("movie_name")

        if title and movie_name:
            petition = Petition.objects.create(
                title=title,
                description=description,
                movie_name=movie_name,
                created_by=request.user
            )
            messages.success(request, "Your petition has been created!")
            return redirect("petition:show", id=petition.id)
        else:
            messages.error(request, "Please provide at least a title and movie name.")

    template_data = {"title": "Create Petition"}
    return render(request, "petition/create.html", {"template_data": template_data})


@login_required
def vote(request, id):
    """Vote or unvote a petition"""
    petition = get_object_or_404(Petition, id=id)
    vote, created = PetitionVote.objects.get_or_create(petition=petition, user=request.user)

    if not created:
        # User already voted → remove vote
        vote.delete()
        messages.info(request, "You removed your vote.")
    else:
        messages.success(request, "You voted for this petition!")

    return redirect("petition:show", id=id)


# Create your views here.
