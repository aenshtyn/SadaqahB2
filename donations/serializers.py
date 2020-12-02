from rest_framework import serializers
from donations.models import Appeal,Donation

class AppealSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Appeal
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Donation
        fields = '__all__'


