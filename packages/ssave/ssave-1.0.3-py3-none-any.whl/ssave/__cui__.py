import configparser
import sys
import ssave

global N1
global N2
global N3

print("SCOS Config & Save Editor and __main__er.")

print("NOTE: Do NOT close the program while in write function.")

print("Functions:\n1. Read\n2. Write\n3. Open File (Will cause error if not done)\n4. Exit\n5. Help")

selection = None

while (True):
    selection = input("Selection: ")
    if (selection == "1"):
        N1 = input("Define Class: ")
        N2 = input("Define Class Variable: ")
        if (N1 == "") or (N2 == ""):
            while (N1 == "") or (N2 == ""):
                print("Warning: Variables Are None.")
                N1 = input("Define Class: ")
                N2 = input("Define Class Variable: ")
        print(ssave.read(N1, N2))
    elif (selection == "2"):
        N1 = input("Define Class: ")
        N2 = input("Define Class Variable: ")
        N3 = input("Define Change: ")
        if (N1 == "") or (N2 == "") or (N3 == ""):
            while (N1 == "") or (N2 == "") or (N3 == ""):
                print("Warning: Variables Are None.")
                N1 = input("Define Class: ")
                N2 = input("Define Class Variable: ")
                N3 = input("Define Change: ")
        ssave.write(N1, N2, N3)
    elif (selection == "3"):
        ssave.sopen(input("File path: "))
    elif (selection == "4"):
        exit()
    elif (selection == "5"):
        print("SCOS Config & Save Editor and __main__er.")

        print("NOTE: Do NOT close the program while in write function.")
        
        print("Functions:\n1. __main__\n2. Write\n3. Open File (Will cause error if not done)\n4. Exit\n5. Help")