from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from payments.models import Subscription
from groups.models import Group, Membership, Request
from groups.forms import GroupCreationForm, JoinGroupForm

@login_required
def group_page_view(request, code):
    if Membership.objects.filter(member=request.user, group__code=code):
        return redirect(reverse_lazy('group-home'))

    try:
        user_req = Request.objects.get(user=request.user, group=code)
        if user_req.isInvite:
            #visiting the page for the first time after invite has been sent
            #Membership object is created
            #delete the pending invite
            new_mem = Membership.objects.create(member=request.user, group=Group.objects.get(code=code))
            new_mem.save()
            user_req.delete()
            return redirect(reverse_lazy('group-home'))
        else:
            return render(request, 'groups/join-group-specific.html', {'group': Group.objects.get(code=code), 'status': 'requested', 'code':code, 'user':user})

    except ObjectDoesNotExist:
        return render(request, 'groups/join-group-specific.html', {'group': Group.objects.get(code=code), 'status': 'norequest', 'code':code, 'user':user})

@login_required
def groupCreationView(request):
    user = request.user
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        data = form.get_cleaned_data(post_data=request.POST)

        new_group = Group.objects.create(
            owner=user,
            type=data['type'][0],
            name=data['name'][0],
            description=data['description'][0]
        )
        new_group.save()
        Membership.objects.create(
            group=new_group,
            member=user,
            isOwner=True,
            isManager=True,
            isAssigner=True,
        )
        return render(request, 'group-home')
    else:
        group_types = list(Subscription.objects.filter(
            user=user,
            isActive=True
        ).values_list('plan__plan'))
        types = [(i[0].title, i[0].title) for i in group_types]
        form = GroupCreationForm(types=types)
        if types:
            return render(request, 'groups/create-group.html', {'form':form, 'status':'hassubs', 'user':user})
        else:
            return render(request, 'groups/create-group.html', {'form':form, 'status':'nosubs', 'user':user})


@login_required
def join_group_view(request, code=None):
    user = request.user
    if not code:
        if request.method == 'POST':
            form = JoinGroupForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data['group_code']
                group = Group.objects.get(code=code)
                if group.type != 'REGULAR':
                    print('0000000000000000000000000000000000')
                    new_req = Request.objects.create(
                        user=user,
                        group=Group.objects.get(code=code),
                    )
                    print(new_req)
                    new_req.save()

                return redirect(
                    reverse_lazy(
                        'group-page',
                        kwargs={'code':code}
                        )
                )
        else:
            form = JoinGroupForm()
            return render(request, 'groups/join-group.html', {'form':form, 'user':user})