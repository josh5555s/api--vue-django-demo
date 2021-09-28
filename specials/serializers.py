from rest_framework import serializers
from specials.models import Special

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ['id','title','description','locations','reoccuring_weekend','start_date','start_time','end_date','end_time','linenos','language','style']

    def create(self, validated_data):
        """
        Create and return a new `Special` instance, given the validated data.
        """
        return Special.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Special` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.locations = validated_data.get('locations', instance.locations)
        instance.reoccuring_weekend = validated_data.get('reoccuring_weekend', instance.reoccuring_weekend)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance