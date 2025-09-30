
def binary_search(the_list, key):

    lower = 0
    upper = len(the_list) - 1

    index = int(upper/2)

    while( upper >= lower ):
        target = the_list[index]
        if target == key:
            return(key)
        elif (target > key):
            upper = index - 1
        elif ( target < key):
            lower = index + 1
        index = (lower + upper) // 2
    return ("None")

def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()