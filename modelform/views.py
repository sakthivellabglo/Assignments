import json
from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django .contrib import messages
from django.contrib.auth. forms import AuthenticationForm 
from django.contrib.auth import login,logout ,authenticate
from django.contrib.auth.decorators import login_required
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            messages.error(request, 'username and password is wrong')
            return redirect('login')
    else:
        form = AuthenticationForm(request.POST)
        return render(request,'login.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('add')	



@login_required(redirect_field_name='next', login_url='login')
def add(request):
    context ={}
    form = GeeksForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('view')	
    context['form']= form
    return render(request, "add_student.html", context);


@login_required(redirect_field_name='next', login_url='login')
def list_table(request):
	stu_obj = stu.objects.all()
	return render(request,'student_list.html',{'my_data':stu_obj})


@login_required(redirect_field_name='next', login_url='login')
def delete_data(request,id):
    context ={"data":"your data will be deleted"}
    obj1 = stu.objects.get(id=id)
    obj1.delete()
    return render(request, "delete_student.html", context)


@login_required(redirect_field_name='next', login_url='login')
def detail_view(request,id):
    obj1 = mark.objects.filter(student_id =id).values()
    return render(request,'mark_list.html',{'my_data':obj1})


@login_required(redirect_field_name='next', login_url='login')
def update_student(request, id):  
    stu_obj = stu.objects.get(id=id) 
    form = GeeksForm(request.POST or None, request.FILES or None, instance = stu_obj)  
    if form.is_valid():  
        form.save()
        return redirect('view')    
    return render(request, 'update_mark.html', {'form':form})


@login_required(redirect_field_name='next', login_url='login')
def mark_add(request):
    context ={}
    form = markForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.created_by = (request.user).username
        form.save()	
        return redirect('view')
    context['form']= form
    return render(request, "add_mark.html", context)
@login_required(redirect_field_name='next', login_url='login')
def delete_mark(request,id):
    obj1 = mark.objects.get(id=id)
    obj1.delete()
    return HttpResponse("your data will be deleted") 
@login_required(redirect_field_name='next', login_url='login')
def update_mark(request, id):  
    stu_obj = mark.objects.get(id=id) 
    form = markForm(request.POST or None, request.FILES or None, instance = stu_obj)  
    if form.is_valid():
        form.updated_by = (request.user).username  
        form.save()
        return redirect('view')    
    return render(request, 'update_mark.html', {'form':form})



def jsondisplay(request):
    stu_obj = mark.objects.all()
    result_list = list(stu_obj.values())
    result_list=json.dumps(result_list, default=str,indent=2)
    return HttpResponse(result_list ,content_type = "Application/json")
 
   

