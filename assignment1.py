# Program Name:
# Course: IT3883/Section 
# Student Name: Ivan Yann NGAKU FOSSO
# Assignment Number: Lab 1
# Due Date: 06/12/2026
# Purpose: This program implements a tet-based menu that allows user to apped data to the input buffer, clear the input buffer, Display the input buffer,or exit program
# Resources:Textbook and PPTX files.
append_msg = ""

while True :
  print("\n")
  print ("""  *********Choose one the 4 option ********
        
  Option 1: Append data to the input buffer
  This option will prompt the user for a string and append it to any previous input that has been provided.\n
  Option 2: Clear the input buffer
  This option will clear any data that has been previously input. \n
  Option 3: Display the input buffer
  This option will print to the screen whatever input data is currently being saved.\n
  Option 4: Exit the program \n
  """)

  option = int(input("Enter your choice: "))

  if option == 1 :
      user_msg = input("Enter a message of your choice: ")
      append_msg = append_msg +" "+ user_msg
      print ("Message appended successfully")

  elif option == 2:
    append_msg = ""
    print ("Buffer has being clear")

  elif option == 3:
    if append_msg:
      print (append_msg)
    else:
      print("The buffer is empty")

  elif option ==4 :
    break

