from traceback import print_tb
import pandas as pd
from django.conf import settings
from django.db import connection

class UploadExcelData():
    def __init__(self, filename):
        filename = settings.UPLOAD_ROOT + "\\" + filename
        self.df = pd.read_excel('%s'%filename, index_col=0, sheet_name="Chronos_Performance_test", usecols="G:AG")
        #print(pd.__version__)
        self.week = "WW46"
        self.start_line = 1
        self.end_line = 1

    def pytorch_with_automl(self, machine_id,):
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
        sql = "INSERT INTO test (`training_time`, `sMAPE_for_AvgRate`, `sMAPE_for_total`, `MSE_for_AvgRate`, `MSE_for_total`, `test_date`, `type_id`,`machine_id`)VALUES"
        for i in range(start_line, end_line):
            values = str(df.values[i][0]), str(df.values[i][1]), str(df.values[i][2]), str(df.values[i][3]),str(df.values[i][4]),week, type_id, machine_id
            type_id += 1
            sql = sql + str(values) +","
        sql = sql[:-1]
        c.execute(sql)    
        # read propheforecast and arimaforecast (29,31)
        type_id = 18
        for i in range(start_line + 17, end_line + 8):
            values = (
                str(df.values[i][0]), str(df.values[i][1]), str(df.values[i][2]), str(df.values[i][3]),
                str(df.values[i][4]),
                week, type_id, machine_id)
            type_id += 1
            

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
        for i in range(start_line, end_line):
            values = (str(df.values[i][5]), str(df.values[i][6]), str(df.values[i][7]), str(df.values[i][8]),
                      str(df.values[i][9]), str(df.values[i][10]), str(df.values[i][11]), week, type_id, machine_id)
            type_id += 1
            print(values)

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
        for i in range(start_line, end_line):
            # 获取每一行的内容
            values = (str(df.values[i][12]), str(df.values[i][13]), str(df.values[i][14]),
                      str(df.values[i][15]), str(df.values[i][16]), str(df.values[i][17]), str(df.values[i][18]), week,
                      type_id, machine_id)
            type_id += 1
            print(values)

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
        for i in range(start_line, end_line):
            # 获取每一行的内容
            values = (str(df.values[i][19]), str(df.values[i][20]), str(df.values[i][21]), str(df.values[i][22]),
                      str(df.values[i][23]), str(df.values[i][24]), str(df.values[i][25]), week, type_id, machine_id)
            type_id += 1
            print(values)

    def main(self):
        ue = UploadExcelData
        ue.pytorch_with_automl(self,1)
        # ue.pytorch_without_automl(1)
        # ue.onnx_without_automl(1)
        # ue.openvino_without_automl(self, 1)
    
        

# if __name__ == '__main__':
#     ue = UploadExcelData()
#     ue.main()
