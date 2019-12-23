import inquirer
import json
from fpdf import FPDF
from format_list import FORMAT_LIST

user_list = []
add_customer = True


def add_customers():
    """
    """
    name_date = input('Please Enter Name :').strip()
    mobile_number = input('Please Enter Mobile Number :').strip()
    age = input('Please Enter Age :').strip()
    city = input('Please Enter City :').strip()
    user_list.append({'name_date': name_date, 'mobile_number': mobile_number, 'age': age, 'city': city})


def export_option_choices():
    """
    """
    questions = [
        inquirer.List('user_input',
                      message="In Which Formate you want to Export?",
                      choices=FORMAT_LIST,
                      ),
    ]
    return inquirer.prompt(questions)


def ask_choices():
    """
    """
    questions = [
        inquirer.List('user_input',
                      message="What you want?",
                      choices=['Add Customer', 'Export'],
                      ),
    ]
    return inquirer.prompt(questions)


def generate_pdf():
    """
    """
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', '', 10.0)
    th = pdf.font_size
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 4
    pdf.ln(4 * th)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Customer List', align='C')
    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)

    ### Adding Header
    for single_header in list(user_list[0]):
        pdf.cell(col_width, 2 * th, str(single_header), border=1)

    pdf.ln(2 * th)
    for row in user_list:
        for datum in list(row.values()):
            # Enter data in colums
            pdf.cell(col_width, 2 * th, str(datum), border=1)

        pdf.ln(2 * th)

    pdf.output('customer_list.pdf', 'F')


def generate_text_file():
    """
    """
    with open("customer_list.txt", "w") as file:
        for single_date in user_list:
            file.write(json.dumps(single_date))
            file.write("\n")


while True:
	"""
	Add multiple customer and export data as PDF or Text File
	"""
    ask_quess = ask_choices()
    add_customer = True if ask_quess['user_input'] == 'Add Customer' else False
    while add_customer:
        add_customers()
        user_choices = ask_choices()
        add_customer = True if user_choices['user_input'] == 'Add Customer' else False

    else:
        export_answer = export_option_choices()
        if len(user_list) == 0:
            raise Exception("Please Add Customer For Export Data")
        if export_answer['user_input'] == "Text":
            generate_text_file()
        elif export_answer['user_input'] == "PDF":
            generate_pdf()
        else:
            print("New Format options")
        break

