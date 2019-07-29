from csv2json import convert, load_csv, save_json
import datetime,random
from os import path
import subprocess,os
from json2xml import json2xml, readfromjson
import xmltodict,json,csv,re
from xmlutils.xml2csv import xml2csv
import logging  

logging.basicConfig(filename="conversion.log",format='%(levelname)s %(asctime)s %(message)s',filemode='a') 

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


format_glob = ["CSV","JSON","XML"]

def read_json(filename):
    return json.loads(open(filename).read())
def write_csv(data,filename):
    with open(filename, 'w+') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def convert_csv_to_json(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".json"
    with open(filename) as r, open(output_file_name, 'w') as w:
        convert(r, w)
    print("File conversion completed!, output filename= ",output_file_name)
    return output_file_name

def convert_json_to_csv(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
       output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".csv"
    #print(filename,output_file_name)
    write_csv(read_json(filename), output_file_name)
    
    print("File conversion completed!, output filename= ",output_file_name)
    return output_file_name
    
def convert_json_to_xml(filename): 
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".xml"
    data = readfromjson(filename)
    fob=open(output_file_name,'w')
    fob.write(json2xml.Json2xml(data).to_xml())
    fob.close()
    print("XML file was created, filename= ",output_file_name)
    return output_file_name

def convert_xml_to_json(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".json"
    filedata = ""
    with open(filename, 'r') as file:
        filedata = file.read()
    filedata = json.dumps(xmltodict.parse(filedata))
    fob=open(output_file_name,'w')
    fob.write(filedata)
    fob.close()
    print("JSON file was created, filename= ",output_file_name)
    return output_file_name


def convert_xml_to_csv(filename):
    logger.warning("User trying xml to csv, this may not work correctly all the times!") 
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".csv"
    data=""
    tname = convert_xml_to_json(filename)
    with open(tname, 'r') as myfile:
        data = myfile.read()
    #print(data)
    if data[0]!='[':
        data = '['+data+']'
    #print(data)
    fob = open(tname,'w')
    fob.write(data)
    fob.close()
    tname2 = convert_json_to_csv(tname)
    os.remove(tname)
    print("CSV file was created, filename= ",tname2)
    return tname2

def get_filenames(format1):
    fname = input("Enter the filename to be converted: ")
    #add checks for file type and file existence here
    if fname.split('.')[-1].upper() != format1:
        print("The file type is not of %s type" %format1)
        return False
    if not path.exists(fname):
        print("The input file does not exist!")
        return False
    return(fname)

def convert_csv_to_xml(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".xml"
    tname = convert_csv_to_json(filename)
    tname2 = convert_json_to_xml(tname)
    os.remove(tname)
    return tname2

def initiate_convert_seq(format1, format2):
    filename = get_filenames(format1)
    if filename == False:
        return
    if(format1 =="CSV" and format2 == "JSON"):
        logger.info("CSV TO JSON conversion") 
        convert_csv_to_json(filename)
    elif(format1 == "JSON" and format2 == "CSV"):
        logger.info("JSON TO CSV conversion")
        convert_json_to_csv(filename)
    elif(format1 == "JSON" and format2 == "XML"):
        logger.info("JSON TO XML conversion")
        convert_json_to_xml(filename)
    elif(format1 == "XML" and format2 == "JSON"):
        logger.info("XML TO JSON conversion")
        convert_xml_to_json(filename)
    elif(format1 == "XML" and format2 == "CSV"):
        logger.info("XML TO CSV conversion")
        convert_xml_to_csv(filename)
    elif(format1 == "CSV" and format2 == "XML"):
        logger.info("CSV TO XML conversion")
        convert_csv_to_xml(filename)
