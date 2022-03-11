print("Enter the columns and entries for the matrix.")
M1_1 = int(input("Enter the entry at 1x1: "))
M1_2 = int(input("Enter the entry at 1x2: "))
M2_1 = int(input("Enter the entry at 2x1: "))
M2_2 = int(input("Enter the entry at 2x2: "))

denominator = (M1_1*M2_2) - (M2_1*M1_2)

if denominator != 0:
  print("The Matrix is invertible.")
  value = 1/denominator
  place_holder = M1_1
  M1_1 = M2_2 * value
  M2_2 = place_holder * value
  M1_2 = M1_2 * -value
  M2_1 = M2_1 * -value

  print(str(M1_1) + "   "+str(M1_2))
  print(str(M2_1) + "   "+str(M2_2))
  
  

else:
  print("The Matrix is not invertible.")