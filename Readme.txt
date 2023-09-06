The program uses itunes API to get top listed songs of the named artist.


The sys module let's you enter your arguments in the command line or the terminal itself.
Example: itunes.py Eminem

                              
                              MODIFICATIONS YOU CAN MAKE


The "Limit" variable in the url given on line 9 of the code will let you choose the number of songs you
want the program to fetch from the API.

Example: "---------------------------limit=50----", will print 50 songs of the artist as the limit is 
given value of 50.



The "sys.argv" argument in the url given on line 9 of the code will let you choose the number of arguments
your program can accept from the terminal or command line.

Example: sys.argv[3], will let you enter 3 arguments i.e. the first name and last name seperated by 
a blank space like "The weekend". 