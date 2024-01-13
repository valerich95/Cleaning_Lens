from .models import InputQueryModel
from rest_framework import serializers
from .models import ResponseDataModel

class ResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseDataModel
        exclude = ['input_query_model']

class InputQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = InputQueryModel
        fields = '__all__'

    def validate(self, attrs):
        search_query = attrs.get('search_query' , '')
        user_voice = attrs.get('user_voice' , '')
        if not search_query and not user_voice:
            raise serializers.ValidationError('You must provide at least one of search query or voice')
        return super().validate(attrs)