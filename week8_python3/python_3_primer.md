# Python primer III, Data Science I 

## Topics to cover
- working with files (input/output)
- processing command line arguments in your code
- introduction to using libraries (`sys`) and (`re`)
- Haddock and Dunn chapters 9 and 10, bit of 11 (`sys.argv`)
- updated document that has corrections for python3 where necessary (PythonLesson2_Chapter9.pdf, PythonLesson3_Chapter10.docx)


# Working with Files

For almost every task you attempt with Python, you will need to 1) open and read data from existing text files; and 2) write the products of your code to new text files. Sometimes you will work with one file at a time, while other tasks will involve reading and writing to multiple files and at some times large numbers of files. As hopefully you will see here, all of the above is fairly straightforward with Python. 

## I. Input

Input involves several steps

**A.** assigning the name of the file to a variable (based on its location), and opening a connection to the file (creating a file object with `open()`)

**B.** reading the contents of the file with `.read` or using a `for` loop, using one of several available methods in Python(detailed below)

### A. Establishing file handles: `open()`can be used to open a connection (also could be called a file handle) to files stored in directories on your computer. 

### This can be done by 'hardcoding' the name of a file or files into your code:

If the file is in your working directory:

    IN_file=open('data.txt', 'r')

Of course, you can also use an absolute path:

    IN_file=open('/working/parchman/data.txt', 'r')


### Perhaps more usefully, file names can be processed from command line arguments. This is often advantageous in that the same script can be used to process different files or different sets of files without. Let's walk through how to do this below, while also giving you a preview of using python libraries/modules.


A strength of python is the enormous number of libraries/packages that exist to facilitate specific tasks. We will soon start to learn more about more libraries in Python; here we will introduce a commonly used library and the process of importing libraries. Importing a library into your python scrip is done with a simple line (below, import function, followed by name of library):

    import sys

Such library statements are typically placed at the top of python scripts. As time goes on, you may find yourself importing multiple libraries:

    import sys
    import numpy
    import pandas

Or, you can input all on one line:

    import sys, numpy, pandas

Command line arguments can be accessed from you code using `argv` function of the `sys` library. `sys.argv` allows you to directly access a list of command line arguments.  

From here, you can see that using the `open()` function to make file objects from filenames contained in the `sys.argv` list is an efficient way to access files in your code. For most cases, this strategy will be more efficient and useful than hardcoding file names into your scripts.

    import sys
    IN = open(sys.argv[1], 'r') 
    
If you provide a file name as an argument, `sys.argv[1]`, as above, the second element of that list will be the file name (remember that list indexing in Python begins with zero). So if you ran the code below, the file `data.txt` would be opened and assigned to `IN`.

	python3 read_file.py data.txt
	
	import sys
	IN = open(sys.argv[1], 'r')

The [1:] below skips the first argument in the list (sys.argv[0]), which is the script itself, and will access the remaining command line arguments.

    import sys
    for Arg in sys.argv[1:]:       
        print(Arg)

If you had placed just the above in a script, and executed that script as below:

    $ python argtest.py Lebron AD Rondo

you should see Lebron, AD and Rondo printed consecutively to the screen

<p>&nbsp;</p>

## B. Reading data from a file.

### Below is example sytax for several ways to read data from files:

To read the *entire* contents of file (note, this is rarely useful for large files, and in general)

    IN = IN_file.read()

To read one line at a time:

    IN = IN_file.readline()

If you wanted to read all of the lines in a file straight into a list:

    File_as_List = IN_file.readlines()

Or:

    list(IN_file)

### Looping through file objects with `for`, reading one line at a time. *This is often an ideal way to work with data from files.*

What you will often (perhaps usually) want to do is loop over a file to read each line one at a time from the file. In other words, we will run this block of code on the first line of the file, then we will run this block of code on the second line, and so on. This is memory efficient, fast, and leads to simple code:

    for Line in IN:
        print(Line)

Once you start processing files one line at a time,  you will realize that line ending characters (`\n`) often get in the way, and can be most effectively dealt with by removing them right off the bat. We can use the `.strip` function to do this.

The below code provides a simple example of specifying a file for reading, opening the file, looping through file one line at a time with a `for` loop, and incrementing to keep track of how many lines are being processed. Note, that once you read each line as a scalar, you can essentially do whatever you want within the `for` loop that is extracting lines from the file.

    IN_Name = sys.argv[1]
    IN = open(IN_Name, 'r')
    LineNumber = 0  ## setting to 0 to count lines while looping through the file. 

    for Line in IN:
	    Line = Line.strip('\n') #### critical, removing line ending
	    print(LineNumber, ":", Line)
	
	    LineNumber += 1 ## incrementing LineNumber to count runs through loop
	
    print(LineNumber) # this will be the number of lines processed of IN
    IN.close() #closing IN, see below.

## C. Keeping file names, file objects (also called file handles or file connections), and file contents straight.

Below are three lines of code to 1. create a file name, 2. make a file object, or connection, from your code to that file, and 3. read all contents of that file into a single scalar. Each line below is described as a reminder of how they differ.

    input_file= "~/python_practice/DNA_seq_allosaurus.fasta"
    IN = open(input_file, 'r')
    my_file_contents = IN.read()

1). Create file name pointing to location on device:

    input_file= "~/python_practice/DNA_seq_allosaurus.fasta"

2). Making a file object, or connection, from your code to that file:

    IN = open(input_file, 'r')

3). Using the `.read()` function to read all contents of that file into a single scalar:

    my_file_contents = IN.read()

## II. Output

Opening a file for output, and writing to that file (as opposed to printing the output to the terminal using `print`), works similarly to the examples above and also uses `open()`. With this function, we use either the "r", "w", and "a" arguments for the `open()` function to specify read, write, or append actions. For writing output from your code, we will use "w" or "a".


    OUT = open("outfile.txt", "w")
    OUT.write("Here is the data my python code processed \n")

The `.write` function above works similarly to `print`. Hence, you can write strings of text, variables, and even  variables processed by functions. A few examples below. Two important points about `.write` in how it differs from `print`. `.write()` is picky about what it will write out, preferring strings, and requiring some specific notation (examples below). Also, while `print` automatically appends line endings to statements, `.write` does not. Thus, you will need to add line endings.

    OUT.write("Here is the data my python code processed \n") # string of text, note line ending added

    OUT.write("Data: %d %f" % (VarA, VarB)) # string and variables
    OUT2.write("Data %s \n" % (Line))
    OUT3.write("%d\n" % (VarName))

Strings can be written using just a variable name, but Python doesnt like lists

    OUT4.write(Name + "\n")

For appending to an already existing file, we use option with the "a"

    OUTa = open("existing_file.txt", "a")
    OUTa.write("%d\n" % (VarName)) # will write to end of already existing file

Finally, note that you can control output with `print` as well by using unix redirect (`>`), if you only need to send output to one file.

    $ python myscript.py > output.txt


## III. Closing files 

It may take some experience before you realize that closing files  when you are done with them is good form. While learning and writing straightforward scripts, you may not encounter problems when you fail to close files, but that will change as you ramp up what you are doing. Nonetheless, get in the habit of doing this now, and try not to forget. It is simple using the `.close()` function. While you are learning python, you will commonly want to these commands towards the end of your scripts.

    IN.close()
    OUT.close()


## IV. Processing lines, one at a time

The code below gives an example of looping through every line in a file.

    InFile=open("genenames.txt", 'r')
	for Line in InFile:
		Line = Line.strip('\n') #removing line ending
		


### Example code for opening a file, looping through one line at a time, and splitting each line into a workable list, extracting a range of values:

After removing line endings, you will often want to split the line (which is read in as a string) into a list using `.split()`. Once the line is split, you can work on each element separately using list notation or you can loop through the list with another for loop.

    InFile=sys.argv[1]
    IN=open(InFile, "r")
    OUT1=open("filetowrite.txt", "w")

    LineNumber = 0
	for Line in IN:
		Line = Line.strip('\n')
		ElementList = Line.split('\t') #tab delimited text.
        OUT1.write(str(ElementList[1:5]))
		LineNumber += 1     # incrementing lines to keep track.

## V. Introduction to regular expressions
Thus far, we have used tools that allow pattern recognition as a basis for completing some task or file manipulation in both Unix (e.g., `grep`, `sed`, `tr`, `awk`) and Python (`str.count()`). However, our use of these tools has largely involved searching for fixed patterns. While working with biological data, and really any other form of big data, we will encounter many problems that will require more flexible match patterns. 

We will start working with regular expressions using the `re` module. As hinted above with `sys`, modules/libraries will play a major role in enabling your python code. We will cover that in more detail in a few weeks, and we will get into more detail on regular expressions next week. First, lets introduce pattern matching for regular expressions using `re` (which stands for regular expression).

To use functionality in the `re` module in your code, you want to add a line near the top of your script (just after your shebang line) that uses the `import` function. 

    import re

In general, `re` requires you to specify a pattern to match, followed by a string to match the pattern in. There are numerous functions built into `re`, but lets start here with `re.search`, which simply returns a true/false based on whether the match occurs in the string or not. The general idea is as follows:

    re.search(pattern, string)

We can search a specified string, using an `if` statement as an example of how to control our code based on the presence or absence of matches:

    Seq = "ATCGGGGCCTAGAAT"
    if re.search("TAG", Seq):
        print("Stop codon (TAG) found.\n")


The `^` character can be used to anchor the pattern at the beginning of the string, and the `$` anchors the pattern at the end
    
    Seq = "ATCGGGGCCTAGAAT"
    if re.search("^A", Seq):
        print("Seq begins with A.\n")

    Seq = "ATCGGGGCCTAGAAT"
    if re.search("T$", Seq):
        print("Seq ends with T.\n")
    else:
        print("Seq does not end with T.\n")

This is just a brief introduction to get you started. We will cover more depth on working with regular expressions next week.

Starting next week we will learn more detailed and useful use of the `re` library for matching, extracting, and otherwise taking advantage of the power of regular expression searches. The below table summarizes the functions we will learn, and what they can accomplish:


| Function | utility |
|---------- | ---------- |
|`re.search`| returns boolean for match occurrence in string|
|`re.iter`| processes multiple matches and returns a list of match objects             |
|`re.findall`|Returns all non-overlapping matches of pattern as a list |            |
|`re.sub`|Find and replace expression match|
|`re.split`|Split string by the occurrences of pattern            |
|`re.escape`|Escape special characters in pattern|