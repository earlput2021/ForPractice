#!/usr/bin/python
class Fibonacci:

    def main_menu(self):
        menu_options = {
            1: 'Start 1',
            2: 'End 2'
        }   
        print("**************************************************************************************************")
        print("                                            START                                                 ")
        print("**************************************************************************************************")

        for key in menu_options.keys():
            print (key, '--', menu_options[key] )
        option = ''
        option = input('Enter a positive integer value: ')
        value = self.triggerTransaction(option)
        print("output-->" + value)
        
    def triggerTransaction(self,val):
        try:
            print(val)
            option = int(val)
            if(option < 0 or option > 2):
                print("Please provide a positvie integer only for option and not greater than 2")
                return 0
        except:
            print('Wrong input. Please enter a number ...')      
            exit
        if option == 1:
            option1 = 0
            try:
                print("start")
                option1 = int(input('Enter a valid number: '))
                if(option1 < 0):
                    raise Exception("Please enter postive integer")
                else:
                    dataRet = self.executeFibonacciSeries(option1) 
            except:
                print("Input value error. Please select a positive integer only")  
            return dataRet            
        else:
            exit()
       

    def executeFibonacciSeries(self,x):
        retVal = ''
        currentVal = 0
        prevVal = 0
        x = 1 if x == 0 else x
        for i in range(x):
            if(i <= 0):
                retVal = str(currentVal + prevVal) + ","
            elif(i == 1 ):
                currentVal = 1
                retVal = retVal + str(1) + ","
            elif(i == 2):
                prevVal = 1
                retVal = retVal + str(1) + ","
            else:
                retVal = retVal + str(currentVal + prevVal) + ","
                tempVal = currentVal
                totalVal = currentVal + prevVal
                currentVal = totalVal
                prevVal = tempVal
        return retVal.rstrip(retVal[-1])

if __name__=='__main__':
    fibonacci = Fibonacci()
    while(True):
        fibonacci.main_menu()
        