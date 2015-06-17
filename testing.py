__author__ = 'Sylvestre'

print('file is running!')

from django.contrib.auth.models import User

self = User.objects.get(id=4)

def check_if_email_registered_as_user(self):
        l = list()
        users = User.objects.all()
        for u in users:
            l.append(u.email)
        return self.email in l

print(check_if_email_registered_as_user(self))

