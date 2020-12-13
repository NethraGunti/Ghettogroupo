from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from groups.models import Group, Membership
from tasks.forms import CreateTaskForm
from tasks.models import Task, Subgroup

def create_task(request, code=None):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        data = form.get_cleaned_data(post_data=request.POST)
        new_task = Task.objects.create(
            assigned_by=request.user,
            assigned_group=Group.objects.get(code=code),
            task_title=data['task_title'][0],
            task_desc=data['task_desc'][0],
        )
        deadline = data['deadline'][0]
        if deadline:
            new_task.deadline=deadline
        attachment = data['attachment'][0]
        if attachment:
            new_task.attachment = attachment

        new_task.save()
        if data['subgroups']:
            for sub in data['subgroups']:
                s = Subgroup.objects.create(
                    assigned_to=Membership.objects.get(
                        group__code=code,
                        member__username=sub
                    ),
                    task=new_task
                )
                s.save()

        return redirect(reverse_lazy('group-home')) 
    else:
        form = CreateTaskForm(subgroups=tuple((q, q) for q in Membership.objects.filter(group__code=code)))
    return render(request, 'tasks/create-task.html', {'form': form, 'code': code})