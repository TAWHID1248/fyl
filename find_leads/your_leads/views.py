from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeleForm
# Create your views here.



# Find leads
def find_leads(request):
    form = TeleForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.owner = request.user
        new_post.save()
 
        # form.save()
        return redirect('your_leads:home')
    return render(request, 'your_leads/home.html', {'form': form})