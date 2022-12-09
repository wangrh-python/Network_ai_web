from traceback import print_tb
from django.conf import settings
from django.db import connection
import pandas as pd


class UploadExcelData():

    def __init__(self, filename):
        self.df = pd.read_excel(filename, index_col=0, sheet_name="Chronos_Performance_test", usecols="G:AH")
        self.week = self.df.values[10][26]
        self.start_line = 1
        self.end_line = 1

    def pytorch_with_automl(self, machine_id):
        df = self.df
        machine_id = machine_id
        week = self.week
        start_line = self.start_line
        end_line = self.end_line
        # machine_id 1 is spr, 5 is icl
        if machine_id == 5:
            start_line = 12
            end_line = 23
        elif machine_id == 1:
            start_line = 49
            end_line = 60
        type_id = 1
        c = connection.cursor()
        sql = "INSERT INTO pytorch_with_automl (`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line, end_line):
            values = str(df.values[i][0]), str(df.values[i][1]), str(df.values[i][2]), str(df.values[i][3]),str(df.values[i][4]),week, type_id, machine_id
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)    
        #read propheforecast and arimaforecast (29,31)
        type_id = 18
        c = connection.cursor()
        sql = "INSERT INTO pytorch_with_automl (`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line + 17, end_line + 8):
            values = (
                str(df.values[i][0]), str(df.values[i][1]), str(df.values[i][2]), str(df.values[i][3]),
                str(df.values[i][4]),
                week, type_id, machine_id)
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)

    def pytorch_without_automl(self, machine_id):
        df = self.df
        machine_id = machine_id
        week = self.week
        start_line = self.start_line
        end_line = self.end_line
        # machine_id 1 is spr, 5 is icl
        if machine_id == 5:
            start_line = 12
            end_line = 31
        elif machine_id == 1:
            start_line = 49
            end_line = 68
        type_id = 1
        c = connection.cursor()
        sql = "INSERT INTO pytorch_without_automl(`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `Throughput`, `Latency`,  `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line, end_line):
            values = (str(df.values[i][5]), str(df.values[i][6]), str(df.values[i][7]), str(df.values[i][8]),
                      str(df.values[i][9]), str(df.values[i][10]), str(df.values[i][11]), week, type_id, machine_id)
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)

    def onnx_without_automl(self, machine_id):
        df = self.df
        machine_id = machine_id
        week = self.week
        start_line = self.start_line
        end_line = self.end_line
        # machine_id 1 is spr, 5 is icl
        if machine_id == 5:
            start_line = 12
            end_line = 23
        elif machine_id == 1:
            start_line = 49
            end_line = 60
        type_id = 1
        c = connection.cursor()
        sql = "INSERT INTO onnx_without_automl(`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `Throughput`, `Latency`,  `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line, end_line):
            # 获取每一行的内容
            values = (str(df.values[i][12]), str(df.values[i][13]), str(df.values[i][14]),
                      str(df.values[i][15]), str(df.values[i][16]), str(df.values[i][17]), str(df.values[i][18]), week,
                      type_id, machine_id)
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)

    def openvino_without_automl(self, machine_id):
        df = self.df
        machine_id = machine_id
        week = self.week
        start_line = self.start_line
        end_line = self.end_line
        # machine_id 1 is spr, 5 is icl
        if machine_id == 5:
            start_line = 12
            end_line = 23
        elif machine_id == 1:
            start_line = 49
            end_line = 60
        type_id = 1
        c = connection.cursor()
        sql = "INSERT INTO openvino_without_automl(`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `Throughput`, `Latency`,  `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line, end_line):
            # 获取每一行的内容
            values = (str(df.values[i][19]), str(df.values[i][20]), str(df.values[i][21]), str(df.values[i][22]),
                      str(df.values[i][23]), str(df.values[i][24]), str(df.values[i][25]), week, type_id, machine_id)
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)

    def main(self):
        ue = UploadExcelData
        ue.pytorch_with_automl(self,1)
        ue.pytorch_without_automl(self,1)
        ue.onnx_without_automl(self,1)
        ue.openvino_without_automl(self,1)
        ue.pytorch_with_automl(self,5)
        ue.pytorch_without_automl(self,5)
        ue.onnx_without_automl(self,5)
        ue.openvino_without_automl(self, 5)
