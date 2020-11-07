from django.contrib import admin
from calendarapp.models import Event, EventMember, TypeEvents

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['name']

class TypeEventsAdmin(admin.ModelAdmin):
    model = TypeEvents
    list_display = ['name', 'color']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
admin.site.register(TypeEvents, TypeEventsAdmin)
