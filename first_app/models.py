from django.db import models
# Create your models here.
class CoursesManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['name']) < 5:
			errors['name'] = "Course name should be at least 5 characters"

		if len(postData['description']) < 15:
			errors['description'] = "Description should be at least 15 characters"
		return errors

class Courses(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = CoursesManager()

	def __repr__(self):
		return f"<Courses object: {self.name} ({self.id})>"

