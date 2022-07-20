from django.db import models


class Employee(models.Model):
	full_name = models.CharField(max_length=32)
	age = models.PositiveIntegerField()
	salary = models.IntegerField(blank=True)
	gender = models.BooleanField(null=True)
	email = models.EmailField()
	about = models.TextField(default='felan.')


	def __str__(self):
		emp_gender = 'mr' if self.gender else 'mis'
		return f'{emp_gender} {self.full_name} is {self.age} years old.'
