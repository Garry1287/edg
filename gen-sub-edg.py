#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://code.tutsplus.com/ru/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
# https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python
# https://ru.stackoverflow.com/questions/806572/%D0%92%D0%B7%D1%8F%D1%82%D1%8C-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%BC-%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%81%D0%BA%D0%BE%D0%B1%D0%BA%D0%B0%D1%85
# https://regex101.com/r/UlrpBR/1
# https://stackoverflow.com/questions/55503639/with-python-convert-csv-file-to-xml-file
# https://roytuts.com/how-to-convert-csv-to-xml-using-python/
# https://www.geeksforgeeks.org/create-xml-documents-using-python/

import csv
import re


txtFile = open('mts2.txt', "w")
csvFile = open('mts2.csv', "r")

csvData = csv.reader(csvFile, delimiter='|', quotechar=',')
data = []

for row in csvData:
    data.append(row)
csvFile.close()


def convert_row(row):
    return """
interface TenGigabitEthernet1/1/0.%s%s
 description UIK-%s id-%s p/p %s  %s:%s 
 encapsulation dot1Q %s second-dot1q %s 
 ip vrf forwarding p03v038
 ip address %s 255.255.255.240
end
!""" % (row[12], row[13], row[2], row[3], row[0], row[5], row[6], row[12], row[13], row[11])



# Создаем паттерн для поиска варажения в строке

for row in data[1:]:
  if len(str(row[13])) == 3:
    row[13] = "0" + str(row[13])
  txtFile.writelines(convert_row(row))


txtFile.close()
# print (data[1:])
