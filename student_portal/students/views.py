from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Student
from .form import StudentForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from .serialization import StudentSerializer
# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to Students Portal!")


def home(request):
    data = {
        'title' : 'Python Full Stack Development',
        'instructor' : 'BHARANI',
    }
    return render(request,'home.html',data)

@login_required
def students_page(request):
    students = Student.objects.all()

    query = request.GET.get('search')
    if query:
        students = students.filter(name__icontains=query)

    paginator = Paginator(students, 2)  # 2 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    
    #students = Student.objects.order_by('marks')
    #students = Student.objects.order_by('-marks')
    #students = Student.objects.filter(marks__gte = 80)
    #students = Student.objects.filter(marks__gt = 80)
    #students = Student.objects.filter(marks__range=(60,99))
    
    return render(request,'students.html',{'students':students})

@login_required
def add_student(request):

    if not request.user.is_staff:
        return redirect('/students/')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
        
    else:
        form = StudentForm()
    return render(request,'add_student.html',{'form':form})

# def add_student(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         course = request.POST.get('course')
#         marks = request.POST.get('marks')
#         age = request.POST.get('age')

#         if int(marks) > 100:
#             return render(request,'add_student.html',{
#                 'error':'Marks should be less than or equal to 100'
#                 })
        
#         Student.objects.create(
#             name = name,
#             course = course,
#             marks = marks,
#             age = age
#         )
#         return redirect('/students/')
#     return render(request,'add_student.html')

def delete_student(request,id):

    if not request.user.is_staff:
        return redirect('/students/')

    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students/')

# def edit_student(request,id):
#     student = Student.objects.get(id=id)
#     if request.method == 'POST':
#         student.name = request.POST.get('name')
#         student.course = request.POST.get('course')
#         student.marks = request.POST.get('marks')
#         student.age = request.POST.get('age')

#         student.save()
#         return redirect('/students/')
#     return render(request,'edit_student.html',{'student':student})

def edit_student(request,id):

    if not request.user.is_staff:
        return redirect('/students/')

    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form = StudentForm(instance=student)
    return render(request,'edit_student.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/students/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/students/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request=request,data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('/students/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form':form})
        
def student_api(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['PUT'])
def update_student_api(request, id):
    student = Student.objects.get(id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_student_api(request, id):
    student = Student.objects.get(id)
    student.delete()
    return JsonResponse({'message': 'Student deleted successfully'}, status=204)
