#!/usr/bin/python3

for i in range(1,51):        #    iterates int 1 through 50
    if i % 3 == 0:    #    test if divisible by 3

        if i % 7 == 0:      #    test if divisible by 7 
            print('#{}\t'.format(i) + str(i % 7 == 0 and i % 3 == 0) + '\t CloudComputing')        #    if divisible by 3 & 7, prints iteration, arg response, and 'Computing'
            
        else:
            print('#{}\t'.format(i) + str(i % 7 == 0) + '\t Computing')        #    prints iteration, arg response, and 'Computing'

    elif i % 7 == 0:       #    test if divisible by 7
        print('#{}\t'.format(i) + str(i % 7 == 0 and i % 3 == 0) + '\t  Cloud')

    else:
        print('#{}\t\t\t\tFUCK'.format(i))

else:
    exit