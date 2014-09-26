"""
WSGI config for ctest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ctest.settings")
virtenv =os.path.join(os.environ['HOME'],'webapps','djcelery','myenv','bin','activate_this.py')
#virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtenv, dict(__file__=virtenv))
except IOError:
    pass
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
