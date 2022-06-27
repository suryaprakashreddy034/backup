import re
element_string=(u'gs://vz-poc-gcs1/VzDIPOC/Inbound/vz_one_hr_25_03_2023.csv', u'ENTERPRISE_ID,PLAN_ID,DESCRIPTION_LONG,COMP_PLAN_TYPE,COMMISSION_START_DATE,COMMISSION_END_DATE\r\n,Plan1,Desc1,Type1,2022-03-25,2022-03-25\r\nEtest2,Plan2,Desc2checking asperthrerequirementoftheuse,Type2,2022-03-25,2022-03-25\r\nEtest7,Plan7test7,Detest7,Type7tes7,2022-03-25,2022-03-25\r\nEtest4,Plan4,Desc4,Type4,3/2022/25,2022-03-25\r\n')

#element_list = element_string.split(",")

print(element_string[0])

file_name=element_string[0].replace('://','/').split('/')[4]
print("file name below here")
print(file_name)

element_list = re.sub('\r\n', '',element_string[1])
element_list2 = element_string[1].split("\r\n")

element_list2.remove("")
print(element_list2)
header=element_list2[0]

print("printing header below")
print(header)

print("slicing the elements")
print(element_list2[1::])

new_element_list=element_list2[1::]

for new_value in new_element_list:
        new_value_list=new_value.split(",")
        header_value_list=header.split(",")
        # its a zip of data
        mapped = zip(new_value_list, header_value_list)

        # making as dict
        new_dict = dict(zip(header_value_list, new_value_list))
        print(new_dict)
        

 



