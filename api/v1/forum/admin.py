from django.contrib import admin

from api.v1.forum.models import Answer, Question

# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)