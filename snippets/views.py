from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import os
import datetime
from django.conf import settings
import hashlib


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    parser_classes = (MultiPartParser, FormParser,)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        snippet = get_object_or_404(Snippet, pk=pk)

        uploaded_file = request.FILES['file']
        if uploaded_file is not None:

            directory = os.path.dirname(os.path.abspath(__file__)) + "/.." + settings.MEDIA_URL + datetime.datetime.today().strftime('%Y-%m-%d')

            if not os.path.exists(directory):
                os.makedirs(directory)

            fileName = hashlib.md5(uploaded_file.name.encode()).hexdigest()
            fileExtention = os.path.splitext(str(request.FILES['file']))[1].replace(".", "")
            fileName = fileName +"."+ fileExtention
            with open(directory + "/" + fileName, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
                    destination.close()

            request.data["fileName"] = fileName
            request.data["filePath"] = settings.MEDIA_URL

        serializer = SnippetSerializer(snippet, request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


