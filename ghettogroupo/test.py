from users.models import User as u
from groups.models import Group as g
x = u.objects.first()
z = g.objects.first()
z.group_url(x)