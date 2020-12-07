from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from groups.models import Membership
from groups.forms import GroupCreationForm

def group_page_view(request, code):
    if Membership.objects.filter(member=request.user, group__code=code):
        return HttpResponse('{} IS in group {}.\n User will be redirected to user-group-page'.format(request.user, str(code)))
    return HttpResponse('{} IS NOT in group {}.\n User will be asked to join or request to join'.format(request.user, str(code)))


def groupCreationView(request):
    user = request.user
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = user
            group.save()
            Membership.objects.create(
                group=group,
                member=user,
                isOwner=True,
                isManager=True,
                isAssigner=True,
            )
            return render(request, 'group-home')
    else:
        form = GroupCreationForm()
    return render(request, 'groups/create-group.html', {'form':form})