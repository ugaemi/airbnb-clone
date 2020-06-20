from django.contrib import admin

from conversations import models


@admin.register(models.Message)
class Message(admin.ModelAdmin):

    """Message Admin Definition"""

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    pass
