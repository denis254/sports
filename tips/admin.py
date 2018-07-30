from django.contrib import admin
from django.contrib import admin
from . models import Ticket, FreeTipsGame, VipTipsGame, PunterTipsGame, RollTipsGame
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'join_vip')
    list_select_related = ('profile', )

    def join_vip(self, instance):
        return instance.profile.join_vip
    join_vip.short_description = 'Join Vip'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(VipTipsGame)
admin.site.register(PunterTipsGame)
admin.site.register(RollTipsGame)
admin.site.register(Ticket)
admin.site.register(FreeTipsGame)
