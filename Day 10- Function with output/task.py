def format_name(first_name, second_name) :
    """Take first and last name of person and format it to capitalize view"""
    if first_name == "" or second_name == "" :
        return "please fill the requirement"
    full_name = first_name.strip() + " " + second_name.strip()
    return str(full_name).title()

f_name = input("Please enter your first name. ")
l_name = input("Please enter your last name. ")

name = format_name(f_name, l_name)
print(name)