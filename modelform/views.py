import json
from django.shortcuts import render,HttpResponse,redirect
from modelform.forms import *
from modelform.models import *
from django .contrib import messages
from django.contrib.auth. forms import AuthenticationForm
from django.contrib.auth import login,logout ,authenticate
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.views.generic.list import ListView
from django.core.paginator import Paginator


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


class StudentList(ListView):
    model = stu
    def render_to_response(self, *args,**kwargs):
		#queryset = list(studentModel.objects.all().values())
            queryset = list(stu.objects.all())
            mark_queryset = list(mark.objects.all())
            
            queryset =queryset + mark_queryset
            #js_studentdata = json.dumps(queryset, default=str,indent=2)
            js_data = serializers.serialize("json", queryset,indent=2)
            print(type(js_data))
            #return JsonResponse(js_data  , safe=False)
            return HttpResponse(js_data ,content_type="Application/json" )


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
        form = form.save(commit = False)
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
        form = form.save(commit = False)
        form.updated_by = (request.user).username 
        form.save()
        return redirect('view')    
    return render(request, 'update_mark.html', {'form':form})



def jsondisplay(request):
    stu_obj = mark.objects.all()
    result_list = list(stu_obj.values())
    paginator = Paginator(result_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_list=json.dumps(result_list, default=str,indent=2)
    return HttpResponse(result_list ,content_type = "Application/json")
 

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)



