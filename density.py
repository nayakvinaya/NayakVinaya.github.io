import openpyxl

def select_rows_below_density(excel_file, density_value):
    """Selects the 4 rows below a particular row that has the value "density" in an Excel file.

    Args:
        excel_file (str): The path to the Excel file.
        density_value (str): The value of the cell that you want to find.

    Returns:
        None.
    """

    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active

    density_cells = sheet.findall(density_value)

    for density_cell in density_cells:
        rows_below = density_cell.row + 1
        rows_to_select = rows_below + 4

        sheet.rows[rows_below:rows_to_select].select()

if __name__ == "__main__":
    excel_file = "/Users/vinayanayak/Downloads/Partha_Datasets/allcounties.xlsx"
    density_value = "Density"

    select_rows_below_density(excel_file, density_value)