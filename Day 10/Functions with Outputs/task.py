#Functions with Outputs

f_name = input("Please enter your first name\n")
l_name = input("Please enter your last name\n")

def format_name(f_name,l_name):

    f_name_formatted = ""

    for i in range (len(f_name)):
        if i == 0:
            f_name_formatted += f_name[i].upper()

        else:
            f_name_formatted += f_name[i].lower()

    l_name_formatted = ""

    for i in range (len(l_name)):
        if i == 0:
            l_name_formatted += l_name[i].upper()

        else:
            l_name_formatted += l_name[i].lower()

    return f"{f_name_formatted} {l_name_formatted}"

name = format_name(f_name,l_name)

print(name)