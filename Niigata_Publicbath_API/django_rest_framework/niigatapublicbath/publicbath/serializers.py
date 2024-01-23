from rest_framework import serializers
from .models import PublicbathModels

class PublicbathModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model= PublicbathModels
        fields=["id","name","distance","time","business_holiday","opening_time","ending_time","total_time","online_review_number","online_review_rate","fee","address"]