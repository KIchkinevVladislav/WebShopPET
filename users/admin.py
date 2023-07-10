from django.contrib import admin

from users.models import User, EmailVerifivation
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerifivation)
class EmailVerifivationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)