from django.contrib import admin
from etests.models import TestSet, TestSetLine, Answer,Category,TestQuestion,Option, TestSetUser

admin.site.register(TestSet)
admin.site.register(Answer)
admin.site.register(TestSetLine)
admin.site.register(Category)
admin.site.register(TestQuestion)
admin.site.register(Option)
admin.site.register(TestSetUser)
