from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import json


def chronos_performance(request):

    return render(request, 'curd/chronos_Performance.html')


def chronos_performance_view(request):
    if request.method == 'POST':

        platform = request.POST.get('platform')
        models_list = request.POST.getlist('model')
        framework = request.POST.get('framework')
        c = connection.cursor()
        m_l = []
        j_l = []

        if framework == "pytorch_without_automl":
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                          fw.training_time,fw.Throughput,fw.Latency from tk_data_type td \
                          inner join pytorch_without_automl fw on td.data_id = fw.type_id \
                          inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                          '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
                c.execute(sql)
                columns = [col[0] for col in c.description]
                data_list = [dict(zip(columns, row)) for row in c.fetchall()]
                m_l.append(data_list)

            for i in m_l:
                for j in i:
                    j_l.append(j)

            json_list = json.dumps(j_l)
            return HttpResponse(json_list)
        elif framework == "onnx_without_automl":
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                          fw.training_time,fw.Throughput,fw.Latency from tk_data_type td \
                          inner join onnx_without_automl fw on td.data_id = fw.type_id \
                          inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                          '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
                c.execute(sql)
                columns = [col[0] for col in c.description]
                data_list = [dict(zip(columns, row)) for row in c.fetchall()]
                m_l.append(data_list)

            for i in m_l:
                for j in i:
                    j_l.append(j)

            json_list = json.dumps(j_l)
            return HttpResponse(json_list)
        elif framework == "openvino_without_automl":
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                          fw.training_time,fw.Throughput,fw.Latency from tk_data_type td \
                          inner join openvino_without_automl fw on td.data_id = fw.type_id \
                          inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                          '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
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


def chronos_accuracy(request):

    return render(request, 'curd/chronos_Accuracy.html')


def chronos_accuracy_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        models_list = request.POST.getlist('model')
        framework = request.POST.get('framework')
        m_l = []
        j_l = []
        c = connection.cursor()
        if framework == 'pytorch_with_automl':
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                       fw.training_time,fw.sMAPE_for_AvgRate,fw.sMAPE_for_total,fw.MSE_for_AvgRate,fw.MSE_for_total \
                       from tk_data_type td \
                       inner join pytorch_with_automl fw on td.data_id = fw.type_id \
                       inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                       '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
                c.execute(sql)
                columns = [col[0] for col in c.description]
                data_list = [dict(zip(columns, row)) for row in c.fetchall()]
                m_l.append(data_list)

            for i in m_l:
                for j in i:
                    j_l.append(j)
            json_list = json.dumps(j_l)
            return HttpResponse(json_list)
        if framework == 'pytorch_without_automl':
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                       fw.training_time,fw.sMAPE_for_AvgRate,fw.sMAPE_for_total,fw.MSE_for_AvgRate,fw.MSE_for_total \
                       from tk_data_type td \
                       inner join pytorch_without_automl fw on td.data_id = fw.type_id \
                       inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                       '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
                c.execute(sql)
                columns = [col[0] for col in c.description]
                data_list = [dict(zip(columns, row)) for row in c.fetchall()]
                m_l.append(data_list)

            for i in m_l:
                for j in i:
                    j_l.append(j)

            json_list = json.dumps(j_l)
            return HttpResponse(json_list)
        if framework == 'onnx_without_automl':
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                       fw.training_time,fw.sMAPE_for_AvgRate,fw.sMAPE_for_total,fw.MSE_for_AvgRate,fw.MSE_for_total \
                       from tk_data_type td \
                       inner join onnx_without_automl fw on td.data_id = fw.type_id \
                       inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                       '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
                c.execute(sql)
                columns = [col[0] for col in c.description]
                data_list = [dict(zip(columns, row)) for row in c.fetchall()]
                m_l.append(data_list)

            for i in m_l:
                for j in i:
                    j_l.append(j)

            json_list = json.dumps(j_l)
            return HttpResponse(json_list)
        if framework == 'openvino_without_automl':
            for i in models_list:
                # write Source SQL
                sql = "select mi.platform,td.model,td.model_precision,td.config,\
                       fw.training_time,fw.sMAPE_for_AvgRate,fw.sMAPE_for_total,fw.MSE_for_AvgRate,fw.MSE_for_total \
                       from tk_data_type td \
                       inner join openvino_without_automl fw on td.data_id = fw.type_id \
                       inner join  machine_info mi on fw.machine_id = mi.machine_id where td.model = \
                       '{model}' and mi.platform = '{platform}';".format(model=i, platform=platform)
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
