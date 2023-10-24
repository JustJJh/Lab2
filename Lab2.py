def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    print(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    userinput = input()
    userlist = userinput.split(",")
    Ulist = [float(ele) for ele in userlist]
    return Ulist

def calc_average(numlist):
    Nlist = numlist
    avgVal = sum(Nlist)/len(Nlist)
    return avgVal

def find_min_max(numlist):
    List = numlist
    maxVal = max(List)
    minVal = min(List)
    Intlist = [minVal,maxVal]
    return Intlist
if __name__ == "__main__":
    main()
