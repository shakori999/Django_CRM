from django.db.models import query
from django.db.models.fields import Field
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .filters import *
from .models import *
from .forms import *
from .decorators import *
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            messages.success(request, 'account was created '+ username)
            return redirect('login')


    context = {
        'form':form,
        }
    return render(request, 'accounts/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password Is Incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    deliverd = orders.filter(status='Deliverd').count()
    pending = orders.filter(status='Pending').count()
    deliverd_paid = orders.filter(status='D&P').count()

    context = {
        'orders': orders, 
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'deliverd': deliverd,
        'pending': pending,
        'dp': deliverd_paid,
        
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    clint = request.user.customer
    total_orders = orders.count()
    deliverd = orders.filter(status='Deliverd').count()
    deliverd_paid = orders.filter(status='D&P').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders,
        'total_orders': total_orders,
        'deliverd': deliverd,
        'pending': pending,
        'clint': clint,
        'dp': deliverd_paid,
    }

    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {
        'form':form,
        'customer': customer,
    }
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customers'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'customer':customer,
        'orders': orders,
        'total_orders': total_orders,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    name = ''
    phone = ''
    location = ''
    platform = ''
    if customer.discount() > 0 :
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('name','platform','phone','price','location','gifts','note',), extra=1)
    else:
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('name','platform','phone','price','location','note',), extra=1)
    form = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        form = OrderFormSet(request.POST, instance=customer)
        name = ''
        phone = ''
        location = ''
        platform = ''
        if form.is_valid():
            form.save()
            for felid in form.cleaned_data:
                name = felid.get('name')
                phone = felid.get('phone')
                location = felid.get('location')
                platform = felid.get('platform')
            try:
                client = Client.objects.get(
                                            phone = phone,
                                            )
            except Client.DoesNotExist:
                client = Client.objects.create(
                                                name=name,
                                                phone = phone,
                                                location = location,
                                                platform = platform,
                                            )
                client.save()    
            return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = UpdateOrderForm(instance=order)

    if request.method == 'POST':
        form = UpdateOrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        }
    return render(request, 'accounts/update_order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'order': order
    }


    return render(request, 'accounts/delete.html', context)