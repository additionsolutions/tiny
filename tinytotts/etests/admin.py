from django.contrib import admin
from etests.models import TestSet, TestSetLine, Answer

admin.site.register(TestSet)
admin.site.register(Answer)
admin.site.register(TestSetLine)
