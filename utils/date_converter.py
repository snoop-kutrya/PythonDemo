from datetime import datetime


def convert_date_to_month(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        month_name = date_obj.strftime("%B")
        return month_name

    except ValueError:
        print("Invalid date format. Please use 'dd-mm-yyyy'.")
        return None

def date_fomat_converter(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        return formatted_date

    except ValueError:
        print("Invalid date format. Please use 'dd-mm-yyyy'.")
        return None