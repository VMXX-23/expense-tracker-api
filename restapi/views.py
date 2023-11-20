'''from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_api_key.authentication import ApiKeyAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    """def get(self, request):
        expenses = models.Expense.objects.all()
        serializer = serializers.Expense(expenses, many=True)
         all_expenses = [model_to_dict(expenses) for expense in expenses]
        return Response(serializer.data, status=200)

    def post(self, request):
         amount = request.data["amount"]
         merchant = request.data["merchant"]
         description = request.data["description"]
         category = request.data["category"]

         expense = models.Expense.objects.create(
           amount=amount, merchant=merchant, description=description, category=category
         )
        serializer = serializers.Expense(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    """

    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ["category", "merchant"]
    authentication_classes = [SessionAuthentication]
    permission_classes = [HasAPIKey]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey]
    '''
'''
# doubt code
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, ApiKeyAuthentication
from rest_framework_api_key import import ApiKeyAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
class ExpenseListCreate(ListCreateAPIView):
    """
    List and create expenses.
    """
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ["category", "merchant"]
    authentication_classes = [SessionAuthentication, BasicAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    """
    Retrieve and delete an expense by its ID.
    """
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey, IsAuthenticated]
'''
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    """def get(self, request):
        expenses = models.Expense.objects.all()
        serializer = serializers.Expense(expenses, many=True)
         all_expenses = [model_to_dict(expenses) for expense in expenses]
        return Response(serializer.data, status=200)

    def post(self, request):
         amount = request.data["amount"]
         merchant = request.data["merchant"]
         description = request.data["description"]
         category = request.data["category"]

         expense = models.Expense.objects.create(
           amount=amount, merchant=merchant, description=description, category=category
         )
        serializer = serializers.Expense(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    """

    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ["category", "merchant"]
    authentication_classes = [SessionAuthentication]
    permission_classes = [HasAPIKey]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey]
