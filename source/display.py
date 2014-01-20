import ch
def show_list(list,sp):
	count=0
	len_list=[0]
	for l in list:
		field_list=l.split(sp)
		field_le=len(field_list)
		if(field_le>count)
			count=field_le
		index=0
		for field in field_list:
			try:
				tmp=len_list[index]
			except:
				len_list.append(0)
	
			if(get_len(field)>len_list[field_index]):
				len_list[field_index]=get_len(field)
			index += 1
	return len_list
def get_len(str):
	return len(str)+ch.count(str)
		
