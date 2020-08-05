from django.contrib import admin

from conversations import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    pass
