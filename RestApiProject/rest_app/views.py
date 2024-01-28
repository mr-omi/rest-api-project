from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def home(response):
    return HttpResponse('<h1 style="text-align:center">Home Page</h1>')


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def index(response):
    if response.method == "GET":
        objs = ToDo.objects.all()
        serializer = ToDoSerializer(objs, many=True)
        return Response({
            'message': 'Successful',
            'data': serializer.data
        })

    elif response.method == 'POST':
        data = response.data
        try:
            serializer = ToDoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message": "Successful",
                    "Data": serializer.data
                })
            else:
                return Response({
                    "Message": "Unsuccessful",
                    "Data": serializer.errors
                })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Something went wrong"
            })

    elif response.method == 'PATCH':
        data = response.data
        if not data.get('uuid'):
            return Response({
                "Message": "Unsuccessful",
                "Data": "Uuid is required"
            })
        try:
            uuid = data['uuid']
            obj = ToDo.objects.get(uuid=uuid)
            serializer = ToDoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message": "Successful",
                    "Data": serializer.data
                })
            else:
                return Response({
                    "Message": "Successful",
                    "Data": serializer.errors
                })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Invalid Uid"
            })

    elif response.method == 'DELETE':
        data = response.data
        if not data.get('uuid'):
            return Response({
                "Message": "Unsuccessful",
                "Data": "Uuid is Required"
            })
        try:
            uuid = data['uuid']
            obj = ToDo.objects.get(uuid=uuid)
            obj.delete()
            return Response({
                "Message": "Successful",
                "Data": "Data Deleted Successfully"
            })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Invalid Uuid"
            })


class TodoClass(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # admin = "token": "a731b407315eb1ae9b7d048c7f8b084092a5df61"
    # omi = "token": "f964f6241654c429c2a252d81f7f785549ac2489"

    def get(self, response):
        ids = response.user
        objs = ToDo.objects.filter(user=ids)
        serializer = ToDoSerializer(objs, many=True)
        return Response({
            'message': 'Successful',
            'data': serializer.data
        })

    def post(self, response):
        data = response.data
        data['user'] = response.user.id
        try:
            serializer = ToDoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message": "Successful",
                    "Data": serializer.data
                })
            else:
                return Response({
                    "Message": "Unsuccessful",
                    "Data": serializer.errors
                })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Something went wrong"
            })

    def patch(self, response):
        data = response.data
        if not data.get('uuid'):
            return Response({
                "Message": "Unsuccessful",
                "Data": "Uuid is required"
            })
        try:
            uuid = data['uuid']
            obj = ToDo.objects.get(uuid=uuid)
            serializer = ToDoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message": "Successful",
                    "Data": serializer.data
                })
            else:
                return Response({
                    "Message": "Successful",
                    "Data": serializer.errors
                })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Invalid Uid"
            })

    def delete(self, response):
        data = response.data
        if not data.get('uuid'):
            return Response({
                "Message": "Unsuccessful",
                "Data": "Uuid is Required"
            })
        try:
            uuid = data['uuid']
            obj = ToDo.objects.get(uuid=uuid)
            obj.delete()
            return Response({
                "Message": "Successful",
                "Data": "Data Deleted Successful"
            })
        except:
            return Response({
                "Message": "Unsuccessful",
                "Data": "Invalid  Uuid"
            })


class ToDoViewsets(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
