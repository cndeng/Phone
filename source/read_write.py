import os

def write2file(a_list,file_name):
    f=open(file_name,'w',encoding='utf-8')
    for line in a_list:
        try:
            f.write(line+'\n')
        except:
            pass
    f.close()

def write_part2file(file_name,a_list,index_list):
    f=open(file_name,'w',encoding='utf8')
    for i in index_list:
        f.write(a_list[i]+'\n')
    f.close()

def append2file(file_path,a_list):
    f=open(file_path,'a',encoding='utf8')
    for i in a_list:
        f.write(i+'\n')
    f.close()
    print("Append %d md5sum to database"%(len(a_list)))

def read2memory(file_path):
    with open(file_path,'r',encoding='utf8') as f:
        return f.read()
