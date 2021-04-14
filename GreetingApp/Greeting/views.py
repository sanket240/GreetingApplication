
import logging
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .greeting_exception import GreetingException
import json
from .models import Greet

logger = logging.getLogger('django')

# Function to create new greeting
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'index.html')


def create_user(request):
    """
      Creates new greeting with name and message
        Parameters:
              request:request generated
        Returns:
              renders the request from page
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        user = Greet(name=name, msg=msg)
        try:
            user.save()
            messages.success(request, 'Your greeting is added!!!')
        except:
            pass
        logger.info("New user is added to greeting database.")
        return redirect('/show')
    return render(request, 'index.html')

# Function to print all greetings
def show(request):
    """
         Prints all the greetings present in the database
           Parameters:
                 request:request generated
           Returns:
                 renders the request from page and pass the context
       """
    context = {
        "users": Greet.objects.all()
    }
    logger.info("All data is fetched from greeting database.")
    return render(request, 'show.html', context)


# Function to update all greetings
def update(request, id):
    """
            Updates the greeting present in the database
              Parameters:
                    request:request generated
                    id:id of the user
              Returns:
                    renders the request from page and pass the context
    """
    userid = id
    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        user_object = Greet(name=name, msg=msg, id=userid)
        try:
            user_object.save()
            messages.success(request, 'Your greeting has been updated!!!')
        except:
            logger.warning("Invalid Data in greetings")
            GreetingException("Invalid Data!!")
        logger.info(f"data for user id {userid} is updated in greeting databse ")
        return redirect('/show')
    else:
        context = {
            "users": Greet.objects.filter(id=userid)
        }
        logger.info(f"Update page is rendered for user {userid}.")
        return render(request, 'update.html', context)
