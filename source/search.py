#-------------------------------------------------------------------------------
# Name:        search phone num
# Purpose:     search phone num by pinyin
#
# Author:      john
#
# Created:     19/01/2014
# Copyright:   (c) john 2014
# Licence:     <GPL3>
#-------------------------------------------------------------------------------

import read_write as rw
import os

pinyin_db=r'convert-utf-8.txt'
phone_db=r'PHONE.txt'

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def load_db():
    pinyin_list=rw.read2memory(pinyin_db).split('\n')
    pinyin_dic={}
    for pinyin in pinyin_list:
        pinyin_dic[pinyin[0]]=pinyin[1:-1]
    phone_list=rw.read2memory(phone_db).split('\n')
    p2=list()
    index=0
    for p in phone_list:
        for ps in p.split('\t'):
            for s in ps:
                if(is_chinese(s)):
                    try:
                        p2[index] += pinyin_dic[s]
                    except:
                        p2.append(pinyin_dic[s])
            try:
                p2[index] += " "
            except:
                pass

        index += 1
    #print(len(p2),len(phone_list))
    return phone_list,p2

def search(phone_list,pinyin_list):
    key=""
    while(len(key)==0):
        key=input(">> ")
    index=0
    for pinyin in pinyin_list:
        if (pinyin.__contains__(key)):
            print(phone_list[index])
        index += 1
    for phone in phone_list:
        if (phone.__contains__(key)):
            print(phone)
    pass


def main():
    db=load_db()
    while(1>0):
        search(db[0],db[1])
        input("\n\n\tPress Enter Search Again")
        tmp=os.system('cls')
    pass

if __name__ == '__main__':
    main()
