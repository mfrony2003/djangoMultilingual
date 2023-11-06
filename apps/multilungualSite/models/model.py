from django.db import models


from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Menu(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("Name"), max_length=200),
        url = models.CharField(_("Url"),max_length=200)

    )

    def __str__(self):
        return self.name
    
class Blog(TranslatableModel):
    translations = TranslatedFields(
         title = models.CharField( max_length=200)  ,  
         content = models.TextField( max_length=700)

    )

    def __str__(self):
        return self.title
