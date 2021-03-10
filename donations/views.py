from django.shortcuts import render
from django.http  import HttpResponse, Http404
# from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appeal, Donation, Location
from .models import Donation
from donations.serializers import AppealSerializer, DonationSerializer
from rest_framework.decorators import api_view
from .forms import AppealForm, DonationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.=l


def home(request):
    appeals = Appeal.all_appeals()
    locations = Location.all_locations()

    return render(request, 'index.html',{"locations": locations, "appeals": appeals})

def appeals(request):
    appeals = Appeal.all_appeals()

    return render(request, 'appeals.html', {"appeals": appeals})

def donations(request):
    donations = Donation.all_donations()

    return render(request, 'donations.html', {"donations": donations})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    return render(request, 'works.html')

def register(request):
    return render(request, 'registration.html')

def add(request):
    context ={} 
  
    # create object of form 
    form = AppealForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
    return render(request, 'add.html', context)

def donate(request):
    context ={} 
    
        # create object of form 
    form = DonationForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
  
    return render(request, 'donate.html', context)


@api_view(['GET', 'POST','DELETE'])
def appeal_list(request):

    if request.method == 'GET':
        appeals = Appeal.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            appeals = appeals.filter(title__icontains=title)
        
        appeals_serializer = AppealSerializer(appeals, many=True)
        return JsonResponse(appeals_serializer.data, safe=False)

    elif request.method == 'POST':
        appeal_data = JSONParser().parse(request)
        appeal_serializer = AppealSerializer(data=appeal_data)

        if appeal_serializer.is_valid():
            appeal_serializer.save()

            return JsonResponse(appeal_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(appeal_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Appeal.objects.all().delete()
        return JsonResponse({'message': '{} appeals were deleted successfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def appeal_detail(request, pk):

    try:
        appeal = Appeal.objects.get(pk=pk)
    except Appeal.DoesNotExist:
        return JsonResponse({'message': 'The Appeal does not exist'}, status=status.HTTP_)

    if request.method == 'GET':
        appeal_serializer = AppealSerializer(appeal)
        return JsonResponse(appeal_serializer.data)

    elif request.method == 'PUT':
        appeal_data = JSONParser().parse(request)
        appeal_serializer = AppealSerializer(appeal, data=appeal_data)
        if appeal_serializer.is_valid():
            appeal_serializer.save()
            return JsonResponse(appeal_serializer.data)
        return JsonResponse(appeal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appeal.delete()
        return JsonResponse({'message': 'Appeal was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def appeal_list_published(request):

    appeals = Appeal.objects.filter(published=True)

    if request.method == 'GET':
        appeals_serializer = AppealSerializer(appeals, many=True)
        return JsonResponse(appeals_serializer.data, safe=False)


@api_view(['GET', 'POST','DELETE'])
def donation_list(request):

    if request.method == 'GET':
        donations = Donation.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            donations = donations.filter(title__icontains=title)
        
        donations_serializer = DonationSerializer(donations, many=True)
        return JsonResponse(donations_serializer.data, safe=False)

    elif request.method == 'POST':
        donation_data = JSONParser().parse(request)
        donation_serializer = DonationSerializer(data=donation_data)

        if donation_serializer.is_valid():
            donation_serializer.save()

            return JsonResponse(donation_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(donation_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Donation.objects.all().delete()
        return JsonResponse({'message': '{} donations were deleted successfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)




class AppealList(APIView):
    def get(self, request, format=None):
        all_appeals = Appeal.objects.all()
        serializers = AppealSerializer(all_appeals, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AppealSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    


class DonationList(APIView):
    def get(self, request, format=None):
        all_donations = Donation.objects.all()
        serializers = DonationSerializer(all_donations, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = DonationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'