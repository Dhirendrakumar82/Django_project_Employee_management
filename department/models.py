# from django.db import models

# class Department(models.Model):
#     department_name = models.CharField(max_length=100)
#     department_code = models.CharField(max_length=20, unique=True)
#     manager_name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.department_name

from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=20, default='DEFAULT')
    manager_name = models.CharField(max_length=100, default='NA')
    location = models.CharField(max_length=100, default='NA')

    def __str__(self):
        return self.department_name