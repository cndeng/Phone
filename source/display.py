def show_list(list,sp):
	count=0
	len_list=[0]
	for l in list:
		field_list=l.split(sp)
		field_le=len(field_list)
		if(field_le>count)
			count=field_le
		field_index=0
		for field in field_list:
			try:
				tmp=field_list[field_index]
			except:
				field_list.append(0)
	
			if(get_len(field)>len_list[field_index]):
				field_list[field_index]=get_len(field)
			field_index += 1

