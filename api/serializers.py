from rest_framework import  serializers
from api.models import *

#----------------------------
# Tablet_Daily_Analytics SERIALIZER
#----------------------------

class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search_Results
        fields = '__all__'

class SearchQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Search_Query
        fields = '__all__'