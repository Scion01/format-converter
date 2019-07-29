from csv2json import convert, load_csv, save_json
import datetime,random
import pandas as pd
from os import path

format_glob = ["CSV","JSON"]

def convert_csv_to_json(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
        output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".json"
    with open(filename) as r, open(output_file_name, 'w') as w:
        convert(r, w)
    print("File conversion completed!, output filename= ",output_file_name)

def convert_json_to_csv(filename):
    output_file_name = filename.split('.')[-2]
    if '/' in output_file_name:
       output_file_name = output_file_name.split('/')[-1]
    output_file_name += "_"+str(int(random.random()* 10000))+".csv"

    with open(filename, encoding='utf-8-sig') as f_input:
        df = pd.read_json(f_input)
    df.to_csv(output_file_name, encoding='utf-8', index=False) 
    print("File conversion completed!, output filename= ",output_file_name)


def get_filenames(format1):
    fname = input("Enter the filename to be converted: ")
    #add checks for file type and file existence here
    if fname.split('.')[-1].upper() != format1:
        print("The file type is not of %s type" %format1)
        return False
    if not path.exists(fname):
        print("The input file does not exists!")
    return(fname)

def initiate_convert_seq(format1, format2):
    filename = get_filenames(format1)
    if filename == False:
        return
    if(format1 =="CSV" and format2 == "JSON"):
        convert_csv_to_json(filename)
    elif(format1 == "JSON" and format2 == "CSV"):
        convert_json_to_csv(filename)
