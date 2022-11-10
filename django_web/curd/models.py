# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BpDataType(models.Model):
    data_id = models.AutoField(primary_key=True)
    flame_model = models.CharField(max_length=30, blank=True, null=True)
    data_model = models.CharField(max_length=50, blank=True, null=True)
    precision = models.CharField(max_length=50, blank=True, null=True)
    instruction = models.CharField(max_length=50, blank=True, null=True)
    performance = models.CharField(max_length=50, blank=True, null=True)
    fp32 = models.CharField(max_length=30, blank=True, null=True)
    int8 = models.CharField(max_length=30, blank=True, null=True)
    metric = models.CharField(max_length=30, blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bp_data_type'


class BpTestData(models.Model):
    test_id = models.AutoField(primary_key=True)
    data_id = models.IntegerField()
    data = models.DecimalField(max_digits=50, decimal_places=25, blank=True, null=True)
    core = models.CharField(max_length=50, blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    fp32 = models.CharField(max_length=50, blank=True, null=True)
    int8 = models.CharField(max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=100, blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bp_test_data'


class MachineInfo(models.Model):
    machine_id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    cpu_name = models.CharField(max_length=100, blank=True, null=True)
    memory = models.CharField(max_length=50, blank=True, null=True)
    cpu_mhz = models.IntegerField(blank=True, null=True)
    cpu_max_mhz = models.IntegerField(blank=True, null=True)
    cpu_min_mhz = models.IntegerField(blank=True, null=True)
    l1d_cache = models.CharField(max_length=10, blank=True, null=True)
    l1i_cache = models.CharField(max_length=10, blank=True, null=True)
    l2_cache = models.CharField(max_length=10, blank=True, null=True)
    l3_cache = models.CharField(max_length=10, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    kernel = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    submission_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_info'


class OnnxWithoutAutoml(models.Model):
    training_time = models.CharField(max_length=50, blank=True, null=True)
    smape_for_avgrate = models.CharField(db_column='sMAPE_for_AvgRate', max_length=50, blank=True, null=True)
    smape_for_total = models.CharField(db_column='sMAPE_for_total', max_length=50, blank=True, null=True)
    mse_for_avgrate = models.CharField(db_column='MSE_for_AvgRate', max_length=50, blank=True, null=True)
    mse_for_total = models.CharField(db_column='MSE_for_total', max_length=50, blank=True, null=True)
    throughput = models.CharField(db_column='Throughput', max_length=50, blank=True, null=True)
    latency = models.CharField(db_column='Latency', max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'onnx_without_automl'


class OpenvinoWithoutAutoml(models.Model):
    training_time = models.CharField(max_length=50, blank=True, null=True)
    smape_for_avgrate = models.CharField(db_column='sMAPE_for_AvgRate', max_length=50, blank=True, null=True)
    smape_for_total = models.CharField(db_column='sMAPE_for_total', max_length=50, blank=True, null=True)
    mse_for_avgrate = models.CharField(db_column='MSE_for_AvgRate', max_length=50, blank=True, null=True)
    mse_for_total = models.CharField(db_column='MSE_for_total', max_length=50, blank=True, null=True)
    throughput = models.CharField(db_column='Throughput', max_length=50, blank=True, null=True)
    latency = models.CharField(db_column='Latency', max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openvino_without_automl'


class PytorchWithAutoml(models.Model):
    training_time = models.CharField(max_length=50, blank=True, null=True)
    smape_for_avgrate = models.CharField(db_column='sMAPE_for_AvgRate', max_length=50, blank=True, null=True)
    smape_for_total = models.CharField(db_column='sMAPE_for_total', max_length=50, blank=True, null=True)
    mse_for_avgrate = models.CharField(db_column='MSE_for_AvgRate', max_length=50, blank=True, null=True)
    mse_for_total = models.CharField(db_column='MSE_for_total', max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=50, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField()
    throughput = models.CharField(db_column='Throughput', max_length=50, blank=True, null=True)
    latency = models.CharField(db_column='Latency', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pytorch_with_automl'


class PytorchWithoutAutoml(models.Model):
    training_time = models.CharField(max_length=50, blank=True, null=True)
    smape_for_avgrate = models.CharField(db_column='sMAPE_for_AvgRate', max_length=50, blank=True, null=True)
    smape_for_total = models.CharField(db_column='sMAPE_for_total', max_length=50, blank=True, null=True)
    mse_for_avgrate = models.CharField(db_column='MSE_for_AvgRate', max_length=50, blank=True, null=True)
    mse_for_total = models.CharField(db_column='MSE_for_total', max_length=50, blank=True, null=True)
    throughput = models.CharField(db_column='Throughput', max_length=50, blank=True, null=True)
    latency = models.CharField(db_column='Latency', max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pytorch_without_automl'


class TkDataType(models.Model):
    data_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    model_precision = models.CharField(max_length=50, blank=True, null=True)
    config = models.CharField(max_length=50, blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tk_data_type'


class NaalDataType(models.Model):
    data_id = models.AutoField(primary_key=True)
    core_number = models.CharField(max_length=50, blank=True, null=True)
    batch_size = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'naal_data_type'


class NaalPerformanceData(models.Model):
    inference_mean_time = models.CharField(max_length=50, blank=True, null=True)
    latency_average_time = models.CharField(max_length=50, blank=True, null=True)
    throughput_fps_field = models.CharField(db_column='throughput(FPS)', max_length=50, blank=True, null=True)
    framework = models.CharField(max_length=50, blank=True, null=True)
    test_date = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'naal_performance_data'