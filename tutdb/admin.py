from django.contrib import admin

# Register your models here.
from .models import User, Token

admin.site.register(User)

class TokenAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "access_token_expires_at"]
    list_filter = ["user"]


admin.site.register(Token, TokenAdmin)
