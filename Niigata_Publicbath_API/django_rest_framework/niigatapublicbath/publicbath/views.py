from django.shortcuts import render
from .serializers import PublicbathModelsSerializers
from rest_framework.generics import ListCreateAPIView
from .models import PublicbathModels


class apiView(ListCreateAPIView):
    queryset=PublicbathModels.objects.all().order_by('-online_review_rate')
    serializer_class = PublicbathModelsSerializers

    def get_queryset(self):
        #id,name,distance,time,business_holiday,opening_time,ending_time,total_time,online_review_numb er,online_review_rate,fee,adrenss
        name = self.request.query_params.get('name', None)
        distance = self.request.query_params.get('distance', None)
        time = self.request.query_params.get('time', None)
        business_holiday = self.request.query_params.get('business_holiday', None)
        opening_time = self.request.query_params.get('opening_time', None)
        ending_time = self.request.query_params.get('ending_time', None)
        total_time = self.request.query_params.get('total_time', None)
        online_review_number = self.request.query_params.get('online_review_number', None)
        online_review_rate = self.request.query_params.get('online_review_rate', None)
        fee = self.request.query_params.get('fee', None)
        address = self.request.query_params.get('address', None)

        queryset = super().get_queryset()

#含む
        if name:
            queryset = queryset.filter(name__contains=name)
        if business_holiday:
            queryset = queryset.filter(business_holiday__contains=business_holiday)
        if address:
            queryset = queryset.filter(address__contains=address)
#以下
        if distance:
            queryset = queryset.filter(distance__lte=distance)
        if ending_time:
            queryset = queryset.filter(ending_time__lte=ending_time)
        if time:
            queryset = queryset.filter(time__lte=time)
        if total_time:
            queryset = queryset.filter(total_time__lte=total_time)
        if fee:
            queryset = queryset.filter(fee__lte=fee)
#以上
        if opening_time:
            queryset = queryset.filter(opening_time__gte=opening_time)
        if online_review_rate:
            queryset = queryset.filter(online_review_rate__gte=online_review_rate)
        if online_review_number:
            queryset = queryset.filter(online_review_number__gte=online_review_number)


        return queryset
