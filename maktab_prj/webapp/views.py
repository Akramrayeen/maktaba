from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

 

def index(request):
    template= loader.get_template('index.html')
    return HttpResponse(template.render())

def home(request):
    template= loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template= loader.get_template('about.html')
    return HttpResponse(template.render())



def contact(request):
    template= loader.get_template('contact.html')
    return HttpResponse(template.render())



def registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        if pass1!=pass2:
            return HttpResponse('password and c password is not same')
        else:
             my_user=User.objects.create_user(uname,email,pass1)
             my_user.save()
             return redirect('loginPage')

        # print(uname,email,pass1,pass2)
        
    # template= loader.get_template('registration.html')
    return render(request, 'registration.html')


def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('password')  # Use 'password' instead of 'pass1'
        
        # Authenticate the user
        user = authenticate(username=uname, password=pass1)
        
        if user is not None:
            # If authentication succeeds, log in the user and redirect to home
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual home URL name
        else:
            # If authentication fails, display an error message
            return HttpResponse("User not found or invalid credentials!")
    
    # If the request method is not POST, show the login form
    return render(request, 'login.html')



from django.shortcuts import render
from .models import Location
from cities_light.models import Country, Region, City

def dashbord(request):
   
    countries = Country.objects.all()
    return render(request, 'dashbord.html', {'countries': countries})




from django.http import JsonResponse
from cities_light.models import Country, Region, City

def get_countries(request):
    countries = Country.objects.all()
    country_data = [{'id': country.pk, 'name': country.name} for country in countries]
    return JsonResponse(country_data, safe=False)

def get_states(request):
    country_id = request.GET.get('country_id')
    states = Region.objects.filter(country_id=country_id)
    state_data = [{'id': state.pk, 'name': state.name} for state in states]
    return JsonResponse(state_data, safe=False)

def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(region_id=state_id)
    city_data = [{'id': city.pk, 'name': city.name} for city in cities]
    return JsonResponse(city_data, safe=False)