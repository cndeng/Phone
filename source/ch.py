def is(uchar):
     if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
         return True
     else:
         return False
def contains(ustring):
     for c in ustring:
         if(is_chinese(c)):
             return True
         else:
             return False
def count(str):
	c=0
	for c in str:
		if is(c):
			c +=1
	return c
