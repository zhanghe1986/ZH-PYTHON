#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd
import xlrd
import csv
import re


class CVSController(object):
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.file_path_list = []
        self.file_type = 'csv'

    # def excel_to_csv(self, input_file_path, output_file_path):
    #     if not os.path.exists(os.path.dirname(output_file_path)):
    #         os.mkdir(os.path.dirname(output_file_path))
    #     workbook = xlrd.open_workbook(input_file_path)
    #     sheets = workbook.sheets()
    #     with open(output_file_path, 'w', encoding='utf-8') as f:
    #         write = csv.writer(f)
    #         for i in range(0, len(sheets)):
    #             table = workbook.sheet_by_index(0)
    #             for row_num in range(table.nrows):
    #                 row_value = table.row_values(row_num)
    #                 write.writerow(row_value)

    def excel_to_csv_by_pandas(self, input_file_path, output_file_path):
        if not os.path.exists(os.path.dirname(output_file_path)):
            os.mkdir(os.path.dirname(output_file_path))
        try:
            data = pd.read_excel(input_file_path, index_col=0)
            data.to_csv(output_file_path, encoding='utf-8')
        except:
            print("error info:", output_file_path)

    # read whole path of files from input
    def collect_path_of_file(self, input_dir):
        file_name_list = os.listdir(input_dir)
        for file_name in file_name_list:
            if os.path.isdir(os.path.join(input_dir, file_name)):
                self.collect_path_of_file(os.path.join(input_dir, file_name))
            else:
                self.file_path_list.append(os.path.join(input_dir, file_name).replace('\\', '/'))

    def read_file(self, file_path):
        content_list = []
        with open(file_path, "r", encoding="utf-8") as csv_f:
            read_csv = csv.reader(csv_f)
            for i, rows in enumerate(read_csv):
                line = ''
                for row in rows:
                    line = line + ',' + row
                if line != '':
                    line = line[1:len(line)] + '\n'

                line = re.sub(r'\t', '', line)
                line = re.sub(',', r'\t', line)
                content_list.append(line)
        return content_list

    def write_file(self, file_path, content_list):
        with open(file_path, "w", encoding="utf-8") as csv_f:
            # write_csv = csv.writer(csv_f)
            for line in content_list:
                csv_f.write(line)

    def do_process(self):
        self.collect_path_of_file(self.input)
        self.file_path_list.sort(reverse=False)

        for file_path in self.file_path_list:
            print(file_path)
            output_file_path = file_path.replace(self.input, self.output)
            file = os.path.splitext(output_file_path)
            output_file_path = output_file_path[0: len(output_file_path)-len(file[1])] + '.' + self.file_type

            self.excel_to_csv_by_pandas(file_path, output_file_path)

            # read csv file and change data format
            content_list = self.read_file(output_file_path)
            self.write_file(output_file_path, content_list)


if __name__ == "__main__":
    input = "D:/test"
    output = "D:/test_csv"
    cvs_controller = CVSController(input, output)
    cvs_controller.do_process()
