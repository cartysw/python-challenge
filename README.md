# python-challenge

Hello!

This is a project for the third module of the Data Analyst Bootcamp. 

We were given two different csv data files: one containing data of a company's financial performance over many months, and another containing voting data showing specific candidate's names and the corresponding vote id/county.
The challenge asked us to create two python scripts for each data set and perform some specific actions.

For the first data set regarding the company financial performance, we were tasked with having the program calculate and print:
- The total amount of month entries in the data set
- The total profit the company earned
- The average of the change of profit/loss values over time
- The greatest increase in profits recorded and the month it occurred
- The greatest decrease in profits recorded and the month it occurred

All of these findings should be printed in the terminal you are using to run the code, and to print the same output summary into a text file.
Here is a snippet of the script's code used to find and display the desired results:
![pybank_snippet](https://github.com/user-attachments/assets/46458bfe-0049-401d-8b62-0ccb36c4f1d2)


For the second data set regarding the voting data tied to a few specific candidates, we were tasked with having the program calculate and print:
- The total number of votes that were cast across all given candidates
- Gather a list of each unique candidate's name
- The names of each candidate and the total amount of votes they received, as well as displaying the percentage of the votes they received compared to the total amount of votes earned
- Display the name of the winner based on who received the most votes

As with the previous script, this was also required to print the results into your terminal and to a text file.
Here is a snippet of the script's code:
![pypoll_snippet](https://github.com/user-attachments/assets/a144ccf9-cba2-4fcc-b5a4-5bd7e98d96bf)

I hope these programs prove to be helpful and informational!

It's important that I mention some online resources I referenced during the development of these scripts.
A Google ai result i used to figure out how to find the index of specific months in a list:
https://www.google.com/search?q=python+list+call+specific+unknown+position&client=firefox-b-1-d&sca_esv=ce985a1e0c81157c&sxsrf=ADLYWIJDA9u4XltKlqIODA8y7njakOksyw%3A1729395255947&ei=N3oUZ8W9Oe2pptQP-a3B4A4&ved=0ahUKEwiFtaCvg5yJAxXtlIkEHflWEOwQ4dUDCBA&uact=5&oq=python+list+call+specific+unknown+position&gs_lp=Egxnd3Mtd2l6LXNlcnAiKnB5dGhvbiBsaXN0IGNhbGwgc3BlY2lmaWMgdW5rbm93biBwb3NpdGlvbjIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAFI8IcBUMslWMmFAXACeACQAQCYAYIBoAGvF6oBBDkuMTm4AQPIAQD4AQGYAh2gAqYXwgIKEAAYsAMY1gQYR8ICBRAAGIAEwgIGEAAYFhgewgIFECEYqwLCAgUQIRifBZgDAIgGAZAGCJIHBDguMjGgB_eiAQ&sclient=gws-wiz-serp

This helped me figure out how to tackle the process of adding negative numbers together in the script:
https://www.geeksforgeeks.org/python-program-to-find-sum-of-negative-positive-even-and-positive-odd-numbers-in-a-list/

Another google ai result that helped me figure out how to handle average change, and the greatest increase/decrease functions. Also had some help with formatting from this:
https://www.google.com/search?client=firefox-b-1-d&q=python+bank+profit+calculation+using+csv

Additional reference used for printing out results table using f-strings:
https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

Used this to reference how to write variables to a text file:
https://stackoverflow.com/questions/1900956/write-variable-to-file-including-name

Referenced this to write the function that grabs each unique candidate's name from the data:
https://www.geeksforgeeks.org/python-get-unique-values-list/
