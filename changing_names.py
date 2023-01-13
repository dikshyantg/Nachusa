import os
import pandas as pd 
import shutil
path = "/Users/dikshyantgautam/downloads/nachusa_2019_2nd/"
file_name = "/Users/dikshyantgautam/Desktop/site_extract.csv"
file_input = pd.read_csv(file_name, ",")
path_2 = path + "renamed/"
os.makedirs(path_2,exist_ok= True) # argument 
# making dictionary , write meaningful names
site = {}
for sitename, year in zip(file_input["Site Name"],file_input["Year of Planting"]):
    site[sitename]=year
    

#print (file_input)

for nachusa in os.listdir(path,):
    if not nachusa.endswith(".fastq"):
        continue
    
    print (nachusa)
    date= nachusa.split("_")[3] 
    m = date[0:2]
    d = date[2:4]
    y = date[4:6] # variable name small  ,class name small
    siteextr = nachusa.split("_")[2]
    
    #print(siteextr)
    extr_date = site.get(siteextr,"")
    
    # if siteextr in site: 
    #     extr_date = site[siteextr]
    # else: 
    #     extr_date = ""

    out = f"{extr_date}_{siteextr}_20{y}-{m}-{d}.fastq"
    dest = path_2 + out
    src = path + nachusa 
    if not os.path.exists(dest):
        shutil.copy(src,dest)
    



# variable syntax , string syntax 
# python object definition 
# function, variable, string , object property access ( class and its access), object vs class 



    