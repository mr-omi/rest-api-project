import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_app.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ["uuid", "created_on", "updated_on"]

    def validate(self, validated_data):
        if validated_data.get('title'):
            title = validated_data['title']
            regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
            regi = re.compile('[0123456789]')
            if regex.search(title) is not None:
                raise ValidationError("Title cannot contain any special character")
            if regi.search(title) is not None:
                raise ValidationError("Title cannot contain any Numbers")

        return validated_data
