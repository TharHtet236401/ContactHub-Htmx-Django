from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create you@ views here.
@login_required
def index(request):
    #get all contacts for the current user
    contacts= request.user.contacts.all().order_by('-created_at')
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts.html', context)