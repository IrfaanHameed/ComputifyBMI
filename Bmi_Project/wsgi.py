import os

from django.core.asgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bmi_Project.settings')

application = get_wsgi_application()