from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from user_detail.models import UserDetail
import onetimepad

def signUp(request):
  if request.session.has_key('username'):
    username = request.session['username']
    return redirect(index, username)
  elif request.method=="POST":
    try:
      user = UserDetail.objects.get(email_id=request.POST['email_id'])
    except:
      user = None
    try:
      user = UserDetail.objects.get(username=request.POST['username'])
    except:
      user = None
    if user is not None:
      messages.info(request, "User with the Email ID is already exists")
    else:
      new_user = UserDetail()
      new_user.username = request.POST['username']
      new_user.email_id = request.POST['email_id']
      new_user.password = onetimepad.encrypt(request.POST['password'], 'password')
      new_user.confirm_password = onetimepad.encrypt(request.POST['confirm_password'], 'password')
      new_user.save()
      messages.success(request, "New User is Created Successfully")
  return render(request, 'signup.html', {})


def login(request):
  if request.session.has_key('username'):
    username = request.session['username']
    return redirect(index, username)
  elif request.method=="POST":
    email_id = request.POST['email_id']
    password = request.POST['password']
    try:
      user = UserDetail.objects.get(email_id=email_id)
    except:
      user = None
    if user is None:
      messages.info(request, "Email ID and Password is Incorrect")
      return redirect(signUp)
    else:
      if user.email_id==email_id and onetimepad.decrypt(user.password, 'password')==password:
        request.session['username'] = user.username
        messages.success(request, "Login Successfully")
        return redirect(index, user.username)
      else:
        messages.info(request, "Username and Password Combination is Incorrect")
        return redirect(signUp)
  return render(request, 'login.html', {})


def logout(request):
  if request.session.has_key('username'):
    del request.session['username']
    return redirect(login)

def deleteUser(request):
  user = UserDetail.objects.get(username=request.POST['dropdown'])
  user.delete()
  messages.success(request, "The user is deleted")
  return redirect(index, request.session['username'])


def index(request, username):
  if request.session.has_key('username'):
    users = UserDetail.objects.all()
    username_list = list()
    for user in users:
      if user.username!=request.session['username']:
        username_list.append(user.username)
    return render(request, 'index.html', {'username_list' : username_list})
  else:
    return redirect(login)
