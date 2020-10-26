from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from message import models
import time
import datetime
import json
from django.core import serializers


def get_message(request):
    p = int(request.GET['page'])
    res = {}
    s = models.Message.objects.filter(isShow=True).order_by('-time')
    res['pages'] = (len(s)+4) // 5
    st = (p-1) * 5
    ed = p*5 if p * 5 < len(s) else len(s)
    json_data = serializers.serialize('json', s[st:ed])
    json_data = json.loads(json_data)
    res['data'] = json_data
    return HttpResponse(json.dumps(res), content_type="application/json")


def submit_message(request):
    if request.method == 'POST':
        try:
            msg = models.Message()
            msg.time = datetime.datetime.now()
            msg.name = request.POST['name']
            msg.grade = request.POST['grade']
            msg.classNum = request.POST['classNum']
            msg.title = request.POST['title']
            msg.message_text = request.POST['message_text']
            msg.save()
            res = '提交成功'
        except:
            res = '提交失败'
        return HttpResponse(res)
    else:
        return HttpResponse('请求方式错误')
