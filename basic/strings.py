single_quoted_string = 'data science'
double_quoted_string = "data science"

print(single_quoted_string)
print(double_quoted_string)

tab_string = "\t"
print(tab_string)
print(len(tab_string))


non_tab_string = r"\t"
print(non_tab_string)
print(len(non_tab_string))


multi_line_string = """ first line
second line
third line
"""
print(multi_line_string)


first_name = "Ivan"
last_name = "Kyrylov"

full_name_1 = first_name + " " + last_name
full_name_2 = "{0} {1}".format(first_name, last_name)
full_name_3 = f"{first_name} {last_name}"

for i in [full_name_1, full_name_2, full_name_3]:
    print(i)

