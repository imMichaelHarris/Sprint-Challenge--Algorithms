#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This block of code has a run time complexity of O(n)
     As the value of n gets higher our run time increases proportionately. Say n is 5, first it will compare if 0 is less than 125 which is true then it will set a = 25.
     Then keep repeating until eventually a is greater than 125. This is called linear time the larger n is the longer it will take to get a to be greater than n * n * n 

b) This block also has a runtime of 0(n^2)
    As our n gets larger we have to loop more so that would be 0(n) but in that loop we have a while loop that will compare j which will always be 1 when entering the while loop to n. So each time you have to multiply j times 2 to get it so j is greater than n which will take awhile because you are starting at 1 and multiplying by 2 until you can exit the while loop. Loop within a loop that will both increase as n increases


c) This block is also 0(n)
    Bunnyears will be called recursively with the previous number minus 1. So as n gets larger the amount of functions calls increases. The return + 2 doesn't matter here for calculating Big 0. It's about how many times bunny ears will be called

## Exercise II


