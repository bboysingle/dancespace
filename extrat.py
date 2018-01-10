import xlrd
data = xlrd.open_workbook(r'rawdata.xls') # 打开xls文件
table = data.sheets()[0]  # 打开第一张表
line = 1
for i in range(1129, 1188):  # 循环逐行打印
    h_col = table.row_values(i)[7]
    i_col = table.row_values(i)[8]
    A_choice = table.row_values(i)[9]
    B_choice = table.row_values(i)[10]
    C_choice = table.row_values(i)[11]
    D_choice = table.row_values(i)[12]
    E_choice = table.row_values(i)[13]
    F_choice = table.row_values(i)[14]
    if table.row_values(i)[4] == "判断题":
        print(line, h_col, i_col)
    elif E_choice != "":
        print(line, h_col, i_col, "  ", "A", A_choice, "B", B_choice, "C", C_choice,
              "D", D_choice, "E", E_choice, "F", F_choice)
    else:
        print(line, h_col, i_col, "  ", "A", A_choice, "B", B_choice, "C", C_choice,
              "D", D_choice)
    line += 1


