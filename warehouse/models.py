from django.db import models

# Create your models here.

# class User(models.Model):
#     ROLE_CHOICES =[
#         ('admin', 'Admin'),
#         ('manager', 'Manager'),
#         ('operator', 'Operator'),
#       ]
#     name = models.CharField(max_length=225, null=True, blank=True)
#     email = models.EmailField(unique=True)
#     # password = models.CharField(max_length=12, default='default_password')
#     role = models.CharField(max_length=225, choices=ROLE_CHOICES)

class User(models.Model):
    ROLE_CHOICES =[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('operator', 'Operator'),
      ]
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=True, null=True)
    role = models.CharField(max_length=9, blank=True, null=True, choices=ROLE_CHOICES)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='warehouse_user_set',  # Ensure a unique related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='warehouse_user_set',  # Ensure a unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email


class Warehouse(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    capacity = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warehouses', unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.name
