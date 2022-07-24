import json
import os
from colorama import init, Fore, Back, Style


def main(tasks):
    # tools
    error_input = False
    count_completed = 0
    count_deleted = 0
    list_of_digits = ['1','2','3','4','5','6','7']

    while True:
        i = input('> ')
        
        if i == '-':
            pass

        elif i == 'q':
            break

        elif i == 'del':
            i = input(Fore.RED + '! ')
            print (Style.RESET_ALL) 
            if i in list_of_digits:
                tasks[i] = "---"
            else:
                error_input = True
        
        elif i == 'complete':
            i = input(Fore.GREEN + '! ')
            if i in list_of_digits:
                tasks[i] =  'COMPLETED'
            else:
                error_input = True

        # if i is task
        else:
            for key in tasks:
                if tasks[key] == "---":
                    tasks[key] = json.dumps(i, ensure_ascii = False)          
                    break
                
        # visualization of all info
        with open('tasks.json','w') as j_file:
            os.system("mode con cols=80 lines=20")
            os.system('cls')
            json.dump(tasks, j_file, indent=4)
            
            init()                    
            for item in tasks.items():
                if item[1] == 'COMPLETED':
                        count_completed += 1
                        print(" " + Style.RESET_ALL + item[0] + " - " + Fore.GREEN + item[1] + Style.RESET_ALL)

                elif item[1] == "---":
                        count_deleted += 1
                        print(" " + Style.RESET_ALL + item[0] + " - " + Fore.RED + item[1] + Style.RESET_ALL)
                else:
                    print(" " + Style.RESET_ALL + item[0] + " - "  + item[1] + Style.RESET_ALL)
                print ('───────────────────────────────────────────────────────────────────────────────')
            
            if error_input:
                print (Fore.RED + 'Enter number from 1 to 7')
                print (Style.RESET_ALL)
                error_input = False
            print(Back.GREEN + "completed tasks - " + str(count_completed) + Style.RESET_ALL , 
                end="                                            ")
            print(Back.RED + "deleted tasks - " + str(count_deleted) + Style.RESET_ALL, end="")
            count_completed = 0
            count_deleted = 0
            
if __name__ == "__main__":
    with open('tasks.json','r+') as j_file:
        tasks = json.load(j_file)
        main(tasks)
