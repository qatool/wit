from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wtifont.models import Test
from wtifont.serializers import TestSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

# Create your views here.

@csrf_exempt
def test_list(request):
    """
    list all or add Test
    """
    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def test_detail(request, t_id):
    """
    update,del,add,list Test.
    """
    try:
        test = Test.objects.get(pk=t_id)
    except test.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TestSerializer(test)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TestSerializer(test, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        test.delete()
        return HttpResponse(status=204)
