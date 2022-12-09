from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from django.db import connection
from django.conf import settings
from curd.upload_excel import UploadExcelData
import json, os


# Jump HW_Configuration.html
def index(request):

    return render(request, 'curd/HW_Configuration.html')


# Jump chronos_Performance.html
def chronos_performance(request):

    return render(request, 'curd/Chronos_Performance.html')


# obtain parameter
def chronos_performance_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        model = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        return chronos_performance_data(platform, model, framework, date)
    else:
        return HttpResponse('<h1>你在干什么</h1>')


# Jump chronos_Accuracy.html
def chronos_accuracy(request):

    return render(request, 'curd/Chronos_Accuracy.html')


# obtain parameter
def chronos_accuracy_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        model = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        return chronos_accuracy_data(platform, model, framework, date)
    else:
        return HttpResponse('<h1>你在干什么</h1>')

# Jump naal_Performance.html
def naal_performance(request):

    return render(request, 'curd/NAAL_Performance.html')


# naal performance view logic
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


# Jump Chronos_Performance_Compare.html
def chronos_performance_compare(request):

    return render(request, 'curd/Chronos_Performance_Compare.html')


# obtain parameter
def chronos_performance_compare_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        model = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        return chronos_performance_data(platform, model, framework, date)
    else:
        return HttpResponse('<h1>你在干什么</h1>')


# Jump Chronos_Accuracy_Compare.html
def chronos_accuracy_compare(request):
    return render(request, 'curd/Chronos_Accuracy_Compare.html')


# obtain parameter
def chronos_accuracy_compare_view(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        model = request.POST.getlist('model')
        framework = request.POST.get('framework')
        date = request.POST.get('date')
        return chronos_accuracy_data(platform, model, framework, date)
    else:
        return HttpResponse('<h1>你在干什么</h1>')


# chronos performance data logic
def chronos_performance_data(platform, model, framework, date):
    c = connection.cursor()
    m_l = []
    j_l = []
    for i in model:
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


# chronos accuracy data logic
def chronos_accuracy_data(platform, model, framework, date):
    c = connection.cursor()
    m_l = []
    j_l = []
    for i in model:
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


def chronos_upload(request):

    return render(request, 'curd/Chronos_UPLoad.html')


# chronos upload execl data to mysql
def chronos_upload_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = settings.UPLOAD_ROOT + file.name
        if not os.path.exists(settings.UPLOAD_ROOT):
                os.makedirs(settings.UPLOAD_ROOT)
        try:
            with open(file_path, 'wb') as f:
                for i in file.readlines():
                    f.write(i)
            try:
                ue = UploadExcelData(filename=file_path)
                ue.main()
            except Exception as e:
                return HttpResponse(e)
            return HttpResponse('yes')
        except Exception as e:
            return HttpResponse(e)
    return HttpResponse('no')


# chronos execl download
def chronos_execl_download(request):
    # file path
    file_path = str(settings.BASE_DIR) + r"/curd/static/curd/download/Network_AI_toolkit_Chronos_Performance_test_WW00.xlsx"
    try:
        f = open(file_path, 'rb')
        r = FileResponse(f, as_attachment=True, filename="Network_AI_toolkit_Chronos_Performance_test_WW00.xlsx")
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return r
    except Exception as e:
        raise  Http404("Download error")
