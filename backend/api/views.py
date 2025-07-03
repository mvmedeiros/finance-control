from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializer import TransactionSerializer

@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializedData = TransactionSerializer(transactions, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_transaction(request):
    serializer = TransactionSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)