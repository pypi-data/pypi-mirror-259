# Prema Django

premadjango is a Python package designed to streamline the setup of new Django projects by providing default configurations and settings.

## Installation

You can install premadjango via pip:

pip install premadjango

## Features

### Field Validators

premadjango includes a collection of Django model field validators to ensure data integrity and consistency. These validators cover common validation scenarios and help maintain data quality within your Django models.

#### Basic Usage

from premadjango.models.field_validators import email_validator

class MyModel(models.Model):
    email = models.EmailField(validators=[email_validator])

### Field Converts

premadjango offers a variety of Django model field converters to transform field values into desired formats, such as lowercase, uppercase, etc. These converters help standardize data representation and facilitate data manipulation.

#### Basic Usage

from premadjango.models.field_converts import LowercaseCharField

class MyModel(models.Model):
    name = LowercaseCharField(max_length=100)

### Middleware

The package includes middleware components to enhance the functionality of Django projects. One such middleware is DisableClientSideCachingMiddleware, which disables client-side caching to ensure the most up-to-date content is served to users.

#### Basic Usage

To disable client-side caching, add the middleware to your MIDDLEWARE setting in the Django project's settings.py file:

MIDDLEWARE = [
    # Other middleware classes...
    'premadjango.middleware.DisableClientSideCachingMiddleware',
]

## Conclusion

With premadjango, setting up new Django projects becomes more efficient and straightforward. By leveraging its default configurations, field validators, converters, and middleware, developers can focus more on building their applications rather than configuring project settings from scratch.
