from rest_framework import serializers
from .models import Topic


class PostTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'parent', 'title', 'childs']

    def get_childs(self, topic):
        return TopicSerializer(Topic.objects.filter(parent=topic), many=True).data

