<h1 align="center"><b>CS50P Project</b></h1>
<h2>Title: MGInventoryCSV</b></h2>
<h2><b>Overview</b></h2>
<p>This program was designed to meet a specific need of creating a Comma Separated Value file for inventory purposes on the Mountain Grove Campus.  These csv files are sent to a vendor when purchasing chromebooks, so that the vendor can U.V. print our custom campus inventory I.D. from the csv to each chromebook.  They then populate the rest of the csv file with the Manufacture Serial Number, the vendor Warranty Serial Number, and the unit MAC Address.  They then send it back to me for my inventory system.</p>
<p>I originally created a class for each of the functions, but decided that a class was only really necessary for the 'info' data structure and the rest would be better as functions.</p>
<p>I struggled with deciding on prompting the user to re-enter data if the user input did not pass the regex check or to stop the program on invalid data entry. If the program did not re-prompt the user and instead stopped the program, the code would be cleaner than having multiple 'while' loops, but the user experience would suffer if the user had to re-enter all the data every time there was a typo.</p>
<p>I did not add a header row to the csv files as the vendor that uses this data often restructures the order of the data with their own headers.  It would be easy to implement using a dictionary and the writeheader() function included in the <a href="https://docs.python.org/3/library/csv.html#module-csv">csv</a> module, or by manually having the csv writer create the first row with header information.</p></br>
<h4><b>Needed Modules</b></h4>
<h5><b>Note: These are all included in <a href="https://docs.python.org/3/library/index.html">The Python Standard Library</a> version 3.10.8</b></h5>
<ul><a href="https://docs.python.org/3/library/sys.html">sys</a></br>
<a href="https://docs.python.org/3/library/csv.html#module-csv">csv</a></br>
<a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">re</a></br>
<a href="https://docs.python.org/3/library/subprocess.html">subprocess</a></br>
<a href="https://docs.python.org/3/library/glob.html">glob</a></br></ul></br>
<h4><b>Included test_project.py File</b></h4>
<p>The test_project.py file included in the project is just a basic test file that tests the Class methods and the program functions using the <a href="https://docs.pytest.org/en/7.1.x/">pytest</a> module.
<h4><b>Setup()</b></h4>
<p>The Setup class takes user input to declare the cart the units belong too, the Purchase Order number for the units, the year the units were purchases, the semester code during which the units were purchased, the type of units (predefined codes for our campus), and the starting unit serial number.  The ending unit serial number is calculated by the class, based on the number of units in specified for the order.</p>
The class uses regex checking from the <a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">re</a> module to verify that the user is inputting data correctly, and will re-prompt the user to input correct data for the requested data.</p></br>
<h4><b>duplicate()</b></h4>
<p>The duplicate function is designed to check for the use of duplicate serial numbers.  This would cause an issue as we only want unique serial numbers.</p>
<p>The function uses the <a href="https://docs.python.org/3/library/glob.html">glob</a> module to create a list of existing csv files in the current directory.  The function then "greps", using the <a href="https://docs.python.org/3/library/subprocess.html">subprocess</a> module, through each file and checks to see if there are any occurrences of the starting unit serial number using a regex.</p>
<p>If an occurrence is found then a ValueError is raised telling the user which csv file holds the occurrence.  This is to make sure that the user does not inadvertently reuse serial numbers.</p>
<p>If no duplicate is found then the function returns "False".</p></br>
<h4><b>compose()</b></h4>
<p>The compose function is designed to compose the csv file with the correct file name of</p>
<p>("cart name"-"PO Number"-"number of units"-"start serial number"-"end serial number".csv)</p>
<p>The function creates the file if it does not exist, then appends each line (unit info) to the file.</p>
