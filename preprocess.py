
from os import close


def remove_lines(file):
    with open(file,'r+',encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()
        
def tokenize_sentence(file):
    f = open(file,"r+",encoding="utf-8")
    a = f.read()
    new_a = a.split("。")
    print(len(new_a))
    f.seek(0)
    for i in new_a:
        f.write(i + "\n")
    f.truncate()
    remove_lines(file)

def append_dot(file):
    f = open(file,'r+',encoding="utf-8")
    a = f.readlines()
    dot = "。"
    new_a = [x + dot for x in a]
    new_a2 = []
    for i in new_a:
        new_a2.append(i.replace("\n", ""))
    f.seek(0)
    for i in new_a2:
        f.write(i + "\n")
    f.truncate()
    remove_lines(file)

def remove_special_senc(file):
    f = open(file,'r+',encoding="utf-8")
    a = f.readlines()
    print("len of a before remove :",len(a))
    for x in a:
        if len(x) == 3:
            a.remove(x)
    print("len of a after remove :",len(a))
    f.seek(0)
    for i in a:
        f.write(i + "\n")
    f.truncate()
    remove_lines(file)

def remove_special_character(file):
    import re
    f = open(file,'r+',encoding="utf-8")
    a = f.readlines()
    new_a = []
    for i in a:
        i_after = i.replace("@","").replace("！","").replace("；","").replace("？","?").replace("▲","").replace("■","").replace("●","").replace("◆","").replace("＃","")
        new_a.append(i_after)
    f.seek(0)
    for j in new_a:
        f.write(j + "\n")
    f.truncate()
    remove_lines(file)

def remove_duplicate(file,output_file0):
    import hashlib
    import os
    #1
    output_file_path = output_file0
    input_file_path = file
    #2
    completed_lines_hash = set()
    #3
    output_file = open(output_file_path, "w", encoding="utf-8")
    #4
    for line in open(input_file_path, "r", encoding="utf-8"):
    #5
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        #6
        if hashValue not in completed_lines_hash:
            output_file.write(line)
            completed_lines_hash.add(hashValue)
    #7
    output_file.close() 

file = "data/clean_data/data_ch.txt"
output_file = "data/clean_data/data_ch_2.txt"
# tokenize_sentence(file)
# append_dot(file)
# remove_special_senc(file)
# remove_special_character(file)
remove_duplicate(file,output_file)
