# First Glance at Python Powerhouse
## 1. Background
No doubt, MS Excel is an excellent tool. Yet, when dealing with large dataset, Python is a more optimal choice. In this project, Python (no libraries) is utilized for processing and analyzing two datasets: Mayoral Election & Company Financial Data. Reports of each process are exported into a text file `.txt`.

A quick glance at the final Election Analysis run in Windows Terminal - PowerShell:
<div align="center">
    <img src="./Images/demoE.gif" width=600px/>
</div>

## 2. Languages, Tools & Techniques
* **Languages:**
    * Python | Bash
* **Software/ Applications:**
    * Visual Studio Code | Jupyter Notebook (JPNB) | Notepad++ | Windows Terminal | GitBash | Google Chrome
* **Operating System:**
    * Windows 10 ver. 1909
## Table of Contents
* **Images:** screen captured (.gif) demo of programs run in PowerShell.
* **PyElections:** folder contains files and analysis of Mayoral Election Data:
    * **Jupyter Notebook:** used during the development of final `main.py`.
    * **Resources:** raw election data.
    * **Election_Results.txt:** exported report after running analysis.
    * **main.py:** final program (converted from JPNB) that can be run in Windows Terminal.
* **PyFinances:** folder contains files and analysis of Company Financial Data:
    * **Jupyter Notebook:** used during the development of final `main.py`.
    * **Resources:** raw financial data.
    * **Budget_Report.txt:** exported report after running analysis.
    * **main.py:** final program (converted from JPNB) that can be run in Windows Terminal.
In this project, I developed the codes to help the city of Houston modernize its vote-counting process for the next mayoral elections. Main taks is to write a script to find only the two candidates with the highest number of votes, who will advance to the runoff election. 

Source codes: in file name: "main.py"

Upon running the program, these results will show:

* The total number of votes cast
* A complete list o**f** candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* Print the names of the two candidates who will advance to the runoff election
* A text file contained results will only be exported, named: "Houston_Mayoral_Election_Results.txt"
