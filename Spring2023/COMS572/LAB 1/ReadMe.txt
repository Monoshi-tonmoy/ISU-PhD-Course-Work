To solve the lab 1 assignment, I have used the (https://github.com/aimacode/aima-python) repository. 

From the repository, I have used their two modules(search.py and utils.py). I have written the codes in the Solve.py file, and we have to run this Solve.py file to get results.


                                              

							                       *******************How to run***********************



1. To run the code  use this command: python Solve.py "File Path" "Algorithm Name."

For example, Consider this command, python Solve.py "F:\ISU\Spring2023\COMS572\LAB 1\Part2\Part2\S1.txt" "h1" this command will execute the program with S1.txt initial state and the algorithm it will A* search with h1 heuristic.
The choices for "Algorithm Name" are BFS, h1, h2, h3, or IDS. 


2. We will get output in a terminal and a text file. Line 13 in Solve.py determines where we would like to store our results. I have already run all the given initial states (for part 2 and part 3), and for convenience, I have 
stored the results in multiple text files. In part 2, there are five text files (S1-S5), and I have compiled the results of all these files in "OutputForFile2.txt". The output format looks like this:


		Total Nodes Generated 121139
		Total time taken 4.0 minutes 52.0 seconds 53 millisecond 
		Path Length: 24
		Path: ['U', 'U', 'L', 'L', 'D', 'D', 'R', 'U', 'U', 'L', 'D', 'R', 'U', 'R', 'D', 'D', 'L', 'L', 'U', 'R', 'U', 'R', 'D', 'D']
		...............Ran the FILE F:\ISU\Spring2023\COMS572\LAB 1\Part2\Part2\S1.txt on ALGORITHM BFS.........................



Here the last line indicates the initial state and which algorithm we are using. All the preceding lines shows the result of the algorithm on the given text file containing initial state. 

Similarly, I have stored the results of all part 3 levels in different text files. They are "OutputForFile3Level8.txt", "OutputForFile3Level15.txt," and "OutputForFile3Leve24.txt". The output format for the file is the same. You can 
check  these text files to get a rough idea about the performance of the algorithms on different initial states.