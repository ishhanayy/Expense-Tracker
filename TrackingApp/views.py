from ast import In
from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Expense, User, Income
#from django.contrib import messages
#import MySQLdb
# Create your views here.
def home(req):
    return render(req,'home.html')

def signup(req):
    return render(req, 'signup.html')
    
def login(req):
    return render(req, 'login.html')

def master(req):
    return render(req, 'master.html')

def RenderIncome(req):
    return render(req, 'Income.html')

def RenderExpense(req):
    return render(req, 'Expense.html')

def Dashboard(req):
    if 'uid' in req.session:
        uid = req.session['uid']
        expenses=Expense.objects.filter(user_id=uid)
        income=Income.objects.filter(user_id=uid)
        totalExpense=0
        totalIncome=0
        for exp in expenses:
            totalExpense+=exp.Amount
        for inc in income:
            totalIncome+=inc.Amount
        netBalance=totalIncome-totalExpense
        return render(req,"Dashboard.html",{'netBls':netBalance,'exp':totalExpense,'inc':totalIncome})
    else:
        return render(login)

def RegisterUser(req):
    obj = User()
    obj.First_name=req.GET.get('fn')
    obj.Last_name=req.GET.get('ln')
    obj.Email=req.GET.get('email')
    obj.Password=req.GET.get('pass2')
    obj.mobile_number=req.GET.get('mobile')
    #obj.ProfilePic=req.GET.get('uploadProPic')
    obj.save()
    #return HttpResponse("data saved")
    return redirect(home)

def CheckloginUser(req):
    username=req.GET.get('email')
    password=req.GET.get('pass1')
    #checking if user exist or not
    user=User.objects.filter(Email=username, Password=password)
    if user:
        list = user.values()
        #storing the unique id of user in the form of session
        req.session['uid']=list[0]['id']
        req.session['uname']=list[0]['Email']
        #return HttpResponse("successful login")
        #return redirect("Dashboard")
        return redirect(master)
    else:
        #return HttpResponse('username or password not correct')
        #messages.error(req,'username or password not correct')
        return render(req, 'home.html', {'Msg':"Invalid Username or Password"})
        #return redirect('home')

def SaveIncome(req):
    if 'uid' in req.session:
        uid= req.session['uid']
        obj=Income()
        obj.Date=req.GET.get('date')
        obj.Time=req.GET.get('time')
        obj.Source=req.GET.get('source')
        obj.Amount=req.GET.get('amount')
        obj.Remark=req.GET.get('remark')
        obj.user_id=uid
        obj.save()
        return redirect(ShowIncome)
    else:
        return redirect("login")

def ShowIncome(req):
    if 'uid' in req.session:
        uid=req.session['uid']
        record=Income.objects.filter(user_id=uid)
        #if record is containing some values
        if record:
            ListRecord=record.values()
            return render(req, 'ShowIncome.html', {'record':ListRecord})
        #else the uid means the id is not matching the saved ids in database
        else:
            return redirect()

def SaveExpense(req):
    if 'uid' in req.session:
        uid= req.session['uid']
        obj=Expense()
        obj.Date=req.GET.get('date')
        obj.Time=req.GET.get('time')
        obj.Amount=req.GET.get('amount')
        obj.Expenses=req.GET.get('expenses')
        obj.Remark=req.GET.get('remark')
        obj.user_id=uid
        obj.save()
        return redirect(ShowExpense)
    else:
        return redirect("login")

def ShowExpense(req):
    if 'uid' in req.session:
        uid=req.session['uid']
        record=Expense.objects.filter(user_id=uid)
        #if record is containing some values
        if record:
            ListRecord=record.values()
            return render(req, 'ShowExpense.html', {'record':ListRecord})
        #else the uid means the id is not matching the saved ids in database
        else:
            return redirect()

def allTransaction(req):
    if 'uid' in req.session:
        uid=req.session['uid']
        inc=Income.objects.filter(user_id=uid)
        exp=Expense.objects.filter(user_id=uid)
        return render(req, 'allTransaction.html', {'exp':exp, 'inc':inc})