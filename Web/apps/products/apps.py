from django.apps import AppConfig


class Products(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
