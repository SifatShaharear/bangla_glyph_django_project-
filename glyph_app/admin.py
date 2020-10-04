from django.contrib import admin

from . models import Letter
from . models import JoinLetter


admin.site.register(Letter)
admin.site.register(JoinLetter)
