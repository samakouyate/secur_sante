from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'admin':
        return render(request, 'core/admin_dashboard.html')
    elif user.role == 'medecin':
        return render(request, 'core/medecin_dashboard.html')
    elif user.role == 'patient':
        return render(request, 'core/patient_dashboard.html')
    else:
        return redirect('connexion')


def home(request):
    return redirect('connexion')  # ou 'dashboard' si utilisateur déjà connecté
