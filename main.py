row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Where do you want to put the treasure?")
s_row = input("Specify Row Number: (1~3): ")
s_col = input("Specify Column Number: (1~3): ")
position = s_row + s_col
try:
    Row = int(position[0])
    Col = int(position[1])
    map[Row - 1][Col - 1] = "X"
except ValueError:
    print("Invalid input")
else:
    print(f"{row1}\n{row2}\n{row3}")
