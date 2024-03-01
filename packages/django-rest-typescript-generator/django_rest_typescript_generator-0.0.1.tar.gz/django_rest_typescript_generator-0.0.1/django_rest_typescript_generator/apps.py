from django.apps import AppConfig


class TypeScriptGeneratorConfig(AppConfig):
    name = "django_rest_typescript_generator"
    verbose = "Django REST TypeScript Generator"

    def ready(self):
        pass
