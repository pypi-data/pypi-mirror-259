# django-rest-typescript-generator

A TypeScript code generator for Django Rest Framework, which saves your hand-working and guarantees consistency
between Python codes and modern frontend codes written in TypeScript.

## Features

It generates TypeScript codes from the following Python types.

- Django REST Framework serializers: manual working on `Serializer`, `ModelSerializer`
  derived from Django ORM models, `DataclassSerializer` via [djangorestframework-dataclasses].
- Python dataclasses: Classes decorated by `dataclasses.dataclass`.
- Python enums: Subclasses of `enum.Enum`.

It also supports nested types and composite types.

[djangorestframework-dataclasses]: https://github.com/oxan/djangorestframework-dataclasses

## Requirements

- Python >=3.9
- Django >=3.0
- Django REST Framework >=3.12

## Usage

Install using `pip`.

```bash
$ pip install django-rest-typescript-generator
```

Put a tsgconfig.py file with build tasks into your Django project's root.
```python
from django.conf import settings
from django_rest_typescript_generator.build import build

BUILD_DIR = settings.BASE_DIR / "statics/types"

BUILD_TASKS = [
    build(Foo),
    build(BarSerializer, {"alias": "Foobar"}),
]
```

Add django_rest_typescript_generator to your INSTALLED_APPS.
```python
INSTALLED_APPS = [
    ...
    "django_rest_typescript_generator"
]
```

Run the buildtypescript command on manage.py.
```bash
$ python manage.py buildtypescript
```

Or you can switch to another place.
```bash
$ python manage.py buildtypescript --build-dir /somewhere/you/cannot/explain
```
Or you can switch to another place.
```bash
$ python manage.py buildtypescript --build-dir /somewhere/you/cannot/explain
```
# Examples
## Input: Serializer
```python
class PathSerializer(serializers.Serializer):
    name = serializers.CharField()
    suffix = serializers.CharField()
    suffixes = serializers.ListField(child=serializers.CharField())
    stem = serializers.CharField()
    is_directory = serializers.BooleanField(source="is_dir")
    size = serializers.IntegerField(source="stat.st_size")
```
## Output: Interface
```typescript
export interface Path {
  name: string;
  suffix: string;
  suffixes: string[];
  stem: string;
  isDirectory: boolean;
  size: number;
}
```
There are more examples in test cases.

## Build Options

All options are listed in the table below.

| Name               | Context          | Value            |
| ------------------ | ---------------- | ---------------- |
| alias              | All              | `str`            |
| build_dir          | All              | `str` or `Path`  |
| enforce_uppercase  | Enum             | `bool` (False)   |
