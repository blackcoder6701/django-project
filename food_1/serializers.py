from rest_framework import serializers
from food_1.models import First

class Foody(serializers.ModelSerializer):
    class Meta:
        model=First
        fields=['id','title','code','status','language']
    # id = serializers.IntegerField (read_only = True)
    # title = serializers.CharField (max_length = 100)
    # code = serializers.CharField (max_length = 100)
    # status= serializers.BooleanField()
    # language= serializers.CharField (max_length = 100)

    def create(self,validated_data):
        return First.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.status = validated_data.get('status',instance.status)
        instance.language = validated_data.get('language',instance.language)
        instance.save()
        return instance


