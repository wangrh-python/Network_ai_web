from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import json


def index(request):

    return render(request, 'curd/HW_Configuration.html')


def chronos_performance(request):

    return render(request, 'curd/chronos_Performance.html')


def chronos_performance_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        models_list = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        c = connection.cursor()
        m_l = []
        j_l = []
        for i in models_list:
            # write Source SQL
            c.execute("select mi.platform,td.model,td.model_precision,td.config,fw.training_time,fw.Throughput,\
                       fw.Latency,fw.test_date from tk_data_type td \
                       left join "+ framework + " fw on td.data_id = fw.type_id \
                       left join  machine_info mi on fw.machine_id = mi.machine_id \
                       where td.model = %s and fw.test_date = %s and mi.platform = %s;", [i, date, platform,])
            columns = [col[0] for col in c.description]
            data_list = [dict(zip(columns, row)) for row in c.fetchall()]
            m_l.append(data_list)

        for i in m_l:
            for j in i:
                j_l.append(j)

        json_list = json.dumps(j_l)
        return HttpResponse(json_list)

    else:
        return HttpResponse('<h1>你在干什么</h1>')


def chronos_accuracy(request):

    return render(request, 'curd/chronos_Accuracy.html')


def chronos_accuracy_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        models_list = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        m_l = []
        j_l = []

        c = connection.cursor()
        for i in models_list:
            # write Source SQL
            sql = "select mi.platform,td.model,td.model_precision,td.config,fw.training_time, \
                    fw.sMAPE_for_AvgRate,fw.sMAPE_for_total,fw.MSE_for_AvgRate,fw.MSE_for_total,fw.test_date \
                    from tk_data_type td \
                    left join "+ framework +" fw on td.data_id = fw.type_id \
                    left join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                    '{model}' and fw.test_date = '{date}' and mi.platform = '{platform}';".format(model=i, date=date, platform=platform,)
            c.execute(sql)
            columns = [col[0] for col in c.description]
            data_list = [dict(zip(columns, row)) for row in c.fetchall()]
            m_l.append(data_list)

        for i in m_l:
            for j in i:
                j_l.append(j)
        json_list = json.dumps(j_l)
        return HttpResponse(json_list)
    else:
            return HttpResponse('<h1>你在干什么</h1>')


def naal_performance(request):

    return render(request, 'curd/naal_Performance.html')


def naal_performance_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        c = connection.cursor()
        # write Source SQL
        c.execute("select mi.platform,ndt.core_number,fw.framework,ndt.batch_size,ndt.model,fw.inference,fw.throughput,fw.latency,fw.test_date \
                   from network_ai.machine_info mi \
                   left join network_ai.naal_performance_data fw on mi.machine_id = fw.machine_id \
                   left join network_ai.naal_data_type ndt on fw.type_id = ndt.data_id \
                   where mi.platform = %s and fw.framework = %s and fw.test_date = %s;", [platform, framework, date])

        columns = [col[0] for col in c.description]
        data_list = [dict(zip(columns, row)) for row in c.fetchall()]
        json_list = json.dumps(data_list)
        return HttpResponse(json_list)
    else:
            return HttpResponse('<h1>你在干什么</h1>')

