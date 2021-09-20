from rest_framework import serializers
from .models import Projects, Users

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'image','link','date_posted','design','content','usability','user')

class MerchUser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'username', 'bio','profile_photo')