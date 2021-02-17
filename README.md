# Engin Calculator Software

Open the dist file, and then the controller and run the .exe file located within

It may not work for all systems due to compatability and Windows not allowing unsigned files.
However all the code is available on the GitHub page -- https://github.com/GedikEngin/engin-maths-calculator
There should be a YouTube tutorial available on the following channel demonstrating the program running -- https://www.youtube.com/channel/UCuFDWT6cJpQFm3KfmA6nP0Q

Thank you
- Engin G.


# QA testing

Module:

	Adding:
		* Should be committed to the database
		* Should appear in the listbox
		* Should be automatically selected
		* Clears the chapters and subchapters listbox
		
	Removing:
		* Should delete all linked chapters and subchapters from the database
		* Should clear the chapters and subchapters listbox
		* Should remove the module itself from the listbox and dataase
		* Should automatically select the last module in the listbox if applicable
Chapter:
	Adding:
		- Should be committed to database, linked to a module
		- Should clear the subchapters listbox
		- Should appear in the listbox itself
		- Should be automatically selected
	Removing:
		- Should delete all linked subchapters from the database
		- Should clear the subchapters listbox
		- Should remove the chapter itself from the listbox and database
		- Should automatically select the last chapter in the listbox if applicable
Subchapter:
	Adding:
		- Should be commited to database and be linked to a module and subchapter
		- Should appear in the listbox
		- Should be automatically selected
	Removing:
		- Should delete all linked formulas
		- Should delete itself from listbox and database
		- Should automatically select the last subchapter if applicable

After every feature adding there are user stories
There are set of functionalities that are expected by adding the feature
To do the quality check, to make sure the software as expected and is user friendly
