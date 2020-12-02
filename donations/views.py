from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from donations.models import Appeal, Donation
from donations.serializers import AppealSerializer, DonationSerializer
from rest_framework.decorators import api_view
# Create your views here.




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


def home(request):

    return render(request, 'index.html')