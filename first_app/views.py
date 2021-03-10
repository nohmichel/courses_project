from django.shortcuts import render, redirect
from .models import Courses
from django.contrib import messages


# Create your views here.
def new_course(request):
	errors = Courses.objects.basic_validator(request.POST)
	if len(errors) > 0:	
		for key, value in errors.items():
			messages.error(request, value)
		return redirect ('/')	
	else: 
		create_new = Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect('/')

def index(request):
	context = {
		"all_courses": Courses.objects.all()
		}
	return render(request, 'index.html', context)

def destroy(request, course_id):
	context = {
		"one_course": Courses.objects.get(id=course_id),
		"all_courses": Courses.objects.all() 
	}
	return render(request, 'delete.html', context)

def delete_course(request, course_id):
	print("hello")
	delete_course = Courses.objects.get(id=course_id).delete()
	return redirect('/')

	


