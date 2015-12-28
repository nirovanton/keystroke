#python
import sys

def recursivate(cmd_list,index,combo,checklist):
    
    if index == len(cmd_list)-1: #bottom of the hole
        foo = str()
        for n in combo: foo += n
        for m in cmd_list[index]:
            if checklist.count(foo+m) == 0: 
                print(foo+m)
                checklist.append(foo+m)
        foo = str()
        return True
    if index < len(cmd_list)-1: #falling
        for m in cmd_list[index]:
            combo.append(m)
            recursivate(cmd_list,index+1,combo,checklist)
            combo.remove(m)
        return True




def main():
    
    input_string = list(str(sys.argv[1]))
    finger_dict = {'0': False, # 0&9 evaluate null keys.
                   '1':['1','q','a','z'],  #start with left pinky
                   '2':['2','w','s','x'],  # move right @ 1 finger/line
                   '3':['3','e','d','c'],
                   '4':['4','r','f','v','5','t','g','b'],
                   '5':['6','y','h','n','7','u','j','m'],
                   '6':['8','i','k'],
                   '7':['9','o','l'],
                   '8':['0','p'],
                   '9': False} # 0&9 evaluate null keys.

    cmd_list = []
    chk = []
    for stroke in input_string:
        if finger_dict[stroke]: 
            cmd_list.append(finger_dict[stroke])
    
    # send the command list and a counter down the recursive rabbit hole. 
    index = 0
    permutae = []
    recursivate(cmd_list, index, permutae, chk)
    return

if __name__ == "__main__":
    main()
