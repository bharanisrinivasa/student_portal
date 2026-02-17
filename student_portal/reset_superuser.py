import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_portal.settings')
import django
django.setup()

from django.contrib.auth import get_user_model

username = 'bharani'
password = 'Srinivas12306569'

User = get_user_model()
user = User.objects.filter(username=username).first()
if user:
    user.set_password(password)
    user.save()
    print('PASSWORD SET for', username)
else:
    User.objects.create_superuser(username=username, email='admin@example.com', password=password)
    print('SUPERUSER CREATED', username)
