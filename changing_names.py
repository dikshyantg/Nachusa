#import libraries
import os
import pandas as pd 
import shutil

#set file path and read csv file
path = "/Users/dikshyantgautam/downloads/nachusa_2019_2nd/"
file_name = "/Users/dikshyantgautam/Desktop/site_extract.csv"
file_input = pd.read_csv(file_name, ",")

#create new directory
path_2 = path + "renamed/"
os.makedirs(path_2,exist_ok= True) # argument 

#create dictionary from csv file
site = {}
for sitename, year in zip(file_input["Site Name"],file_input["Year of Planting"]):
    site[sitename]=year
    
#iterate over files in directory
for nachusa in os.listdir(path,):
    if not nachusa.endswith(".fastq"):
        continue
    #print file name
    print (nachusa)
    date= nachusa.split("_")[3] 
    m = date[0:2]
    d = date[2:4]
    y = date[4:6] 
    siteextr = nachusa.split("_")[2]
    extr_date = site.get(siteextr,"")
    out = f"{extr_date}_{siteextr}_20{y}-{m}-{d}.fastq"
    dest = path_2 + out
    src = path + nachusa 
    if not os.path.exists(dest):
        shutil.copy(src,dest)
