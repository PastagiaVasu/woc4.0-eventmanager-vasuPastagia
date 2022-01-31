from django.contrib import admin
from evenetManagementApp.models import event_tbl, participant_tbl

admin.site.register(event_tbl)
admin.site.register(participant_tbl)