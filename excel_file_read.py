import openpyxl


# permanent values - ONLY CHANGE IF EXCEL FILE IS DIFFERENT
start_row = 0
max_rows = 186
column_read = 3
# list to
discord_ID_list = []

def read_save():
    # Define variable to load the dataframe
    dataframe = openpyxl.load_workbook("ID_List.xlsx")

    # Define variable to read sheet
    dataframe1 = dataframe.active

# Iterate the loop to read the cell values
    for row in range(start_row, max_rows):
        for col in dataframe1.iter_cols(column_read, column_read):
            cell_value = col[row].value
            discord_ID_list.append(cell_value)

    return sorted(discord_ID_list)