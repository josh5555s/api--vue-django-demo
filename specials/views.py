from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from specials.models import Special
from specials.serializers import SpecialSerializer
from specials.funcs.create_weekend_dates import create_weekend_dates


@api_view(['GET', 'POST'])
def special_list(request, format=None):
    """
    List all specials, or create a new special.
    """
    if request.method == 'GET':
        specials = Special.objects.all()
        serializer = SpecialSerializer(specials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.data['reoccuring_weekend'] != '':
            start_date, start_time, end_date, end_time = create_weekend_dates(request.data['reoccuring_weekend'])
            request.data['start_date'] = str(start_date)
            request.data['start_time'] = float(start_time * 1000)
            request.data['end_date'] = str(end_date)
            request.data['end_time'] = float(end_time * 1000)
        serializer = SpecialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def special_detail(request, pk, format=None):
    """
    Retrieve, update or delete a special.
    """
    try:
        special = Special.objects.get(pk=pk)
    except Special.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecialSerializer(special)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SpecialSerializer(special, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        special.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
