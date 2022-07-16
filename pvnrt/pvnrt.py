import time
r_si: float = 8.31
r_cgs: float = 8.31 * 10 ** 7


def get_pressure(volume, mole_num, temperature):
    instruction1 = input("Are the values in SI?(y/n): ")
    if instruction1 == "y":
        pressure = (float(mole_num) * r_si * float(temperature)) / float(volume)
        print("The pressure of the gas is " + str(pressure))
    elif instruction1 == "n":
        pressure = (float(mole_num) * r_cgs * float(temperature)) / float(volume)
        print("The pressure of the gas is " + str(pressure))
    else:
        print("Wrong command!!\nTerminating program...")
        time.sleep(2)
        print("Terminated.")
        exit()


def get_volume(pressure, mole_num, temperature):
    instruction1 = input("Are the values in SI?(y/n): ")
    if instruction1 == "y":
        volume = (float(mole_num) * r_si * float(temperature)) / float(pressure)
        print("The volume of the gas is " + str(volume))
    elif instruction1 == "n":
        volume = (float(mole_num) * r_cgs * float(temperature)) / float(pressure)
        print("The volume of the gas is " + str(volume))
    else:
        print("Wrong command!!\nTerminating program...")
        time.sleep(2)
        print("Terminated.")
        exit()


def get_mole_number(pressure, volume, temperature):
    instruction1 = input("Are the value in SI?(y/n): ")
    if instruction1 == "y":
        mole_number = (float(pressure) * float(volume)) / (r_si * float(temperature))
        print("The mole number of the gas is " + str(mole_number))
    elif instruction1 == "n":
        mole_number = (float(pressure) * float(volume)) / (r_cgs * float(temperature))
        print("The mole number of the gas is " + str(mole_number))
    else:
        print("Wrong command!!\nTerminating program...")
        time.sleep(2)
        print("Terminated.")
        exit()


def get_temperature(pressure, volume, mole_num):
    instruction1 = input("Are the value in SI?(y/n): ")
    if instruction1 == "y":
        temperature = (float(pressure) * float(volume)) / (float(mole_num) * r_si)
        print("The temperature of the gas is " + str(temperature))
    elif instruction1 == "n":
        temperature = (float(pressure) * float(volume)) / (float(mole_num) * r_cgs)
        print("The temperature of the gas is " + str(temperature))
    else:
        print("Wrong command!!\nTerminating program...")
        time.sleep(2)
        print("Terminated.")
        exit()


# if __name__ == "__main__":
def calc():
    while True:
        instruction2 = input("What you want to get? (Pressure[p]/Volume[v]/Mole Number[mn]/Temperature[t]/Nothing["
                             "none]): ")
        if instruction2 == "v":
            pres = input("Enter the pressure of the gas: ")
            mn = input("Enter the mole number of the gas: ")
            temp = input("Enter the temperature of the gas: ")
            get_volume(pres, mn, temp)
            print("_______________________________________")
        elif instruction2 == "p":
            vol = input("Enter the volume of the gas: ")
            temp = input("Enter the temperature of thr gas: ")
            mn = input("Enter the mole number of the gas: ")
            get_pressure(vol, mn, temp)
            print("_______________________________________")
        elif instruction2 == "mn":
            vol = input("Enter the volume of the gas: ")
            temp = input("Enter the temperature of thr gas: ")
            pres = input("Enter the pressure of the gas: ")
            get_mole_number(pres, vol, temp)
            print("_______________________________________")
        elif instruction2 == "t":
            vol = input("Enter the volume of the gas: ")
            pres = input("Enter the pressure of thr gas: ")
            mn = input("Enter the mole number of the gas: ")
            get_temperature(pres, vol, mn)
            print("_______________________________________")
        elif instruction2 == "none":
            print("Terminating program...")
            time.sleep(2)
            print("Terminated.")
            exit()
        else:
            print("Wrong command!!\nTerminating program...")
            time.sleep(2)
            print("Terminated.")
            exit()