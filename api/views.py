from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer,PostTopicSerializer
from rest_framework.status import *
from django.db.models import Q


@api_view(['GET', 'POST'])
def topics(request):
    if request.method == 'GET':
        all_topic = Topic.objects.all().order_by('created_at').exclude(~Q(parent=None))
        serialized_topic = TopicSerializer(all_topic, many=True)
        return Response(serialized_topic.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        serialized_topic = PostTopicSerializer(data=request.data)
        if serialized_topic.is_valid():
            topic = serialized_topic.save()

            # all_topic = Topic.objects.all().order_by('created_at').exclude(~Q(parent=None))

            serializer = TopicSerializer(topic)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serialized_topic.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def one_topic(request, id):
    if request.method == 'GET':
        try:
            topic = Topic.objects.get(pk=id)
        except Topic.DoesNotExist:
            return Response({'No Topic Exist Against this Id'}, status=HTTP_404_NOT_FOUND)
        serialized_topic = TopicSerializer(topic)
        return Response(serialized_topic.data, status=HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            topic = Topic.objects.get(pk=id)
        except Topic.DoesNotExist:
            return Response({'No Topic Exist Against this Id'}, status=HTTP_404_NOT_FOUND)

        serialized_topic = PostTopicSerializer(topic, data=request.data)
        if serialized_topic.is_valid():
            serialized_topic.save()

            all_topic = Topic.objects.get(pk=id)
            serializer = TopicSerializer(all_topic)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serialized_topic.data, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            Topic.objects.get(pk=id).delete()
            return Response({'Deleted Successfully'}, status=HTTP_200_OK)
        except Topic.DoesNotExist:
            return Response({'No Topic Exist Against this Id'}, status=HTTP_404_NOT_FOUND)

