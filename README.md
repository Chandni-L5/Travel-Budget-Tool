# Travel Budget Planner 
The Travel Budget Planner application is a Python tool created to assist the user in working out if they have enough money in their budget to book an overseas holiday. 

The user inputs required information for the tool to calculate the total cost, remainder of budget and whether you have enough left over for daily spending. 

[Click here to view the programme](https://travel-budget-tool.onrender.com)

## User Experience
The purpose of this programme is to assist a user in deciding if they have the finances in place to book a holiday abroad. Based on the responses it clarified and repeats back to the user the relevant information to decided if they have enough within their budget to go ahead and book or to take some time to save up a bit more. 

The programme is aimed at adults of all ages who are considering booking a holiday but unsure if their budget will allow for all the required expenses and also leave enough spending money at the end. 

### User Stories
* "I'm planning my first trip and researching holiday options, but I'm unsure if my current savings will be enough to afford it."
* "There are a lot of different expenses attributed to planning my next holiday and I want to use something that can help me organize and display the breakdown of the expenses"
* "I'm not very good with calculations and just want to be able to input in all the amounts and get an itemized response that clearly explains if I have enough in my budget or not"

#### User Goals 
* Simple and straightforward questions
* Clear and concise result that displays the end results and whether or not the budget will allow for the trip. 
* an itemized breakdown of the various types of expenses

## How does it work?
Initially users input information about their budget and length of their trip. Next they are prompted to input a type of expense, the cost of the expense and to select which category it falls within. The pre-set categories include flights, accommodation, travel insurance, transfers, excursions and an open category named miscellaneous. 

Once all the required information has been entered it is repeated back to the user for clarity. In addition a running total of the expenses by category is displayed. The user is then prompted to consider if they wish to add further expenses. If answered yes the questions loop back to the type, cost and category questions and if answered no the final results are displayed.

The final results include the running total of expenses by category, the amount left from the budget after considering these expenses and also how much that would work out as remaining spend per day. Finally a message is displayed to the user dependant on the comparison between the calculated daily spend allowance against the amount initially inputted in the first set of questions. 

A summary of the results are printed to a [Google document](https://docs.google.com/document/d/1ev4aBGg3904TWkGkpIIZq0NqTvKKHihuFNdtoBOZ9Rk/edit?usp=sharing) so the user is able to keep a record of their results to refer back to if required.

## Features
During the planning stages of my project, I utilized Lucidchart.com to brain storm and plan the algorithm which would be required to prepare for the flow of the programme.
![screenshot of Lucidchart algorithm](/documentation/lucid_chart_algo.webp) 

### Existing Features
The structure of the programme is split into an introduction and 3 other sections. 

The initial screen begins with a welcoming message, enhanced with emojis using the Rich framework. This is followed by an introduction to the program’s purpose, including a note that the results will be summarized and saved to an external Google document.

The introduction is separated by a line break before the initial questions are introduced and the first question is displayed. 

![screenshot of the initial screen](/documentation/intro_screen.jpg)

The Rich framework has been applied to style the text using a colour scheme to distinguish the main content and create some division whilst improving the user experience.

The next question is not displayed until the first question is satisfactorily answered. The input field is prepared to only accept a numerical value and if any letters are entered, an error message is displayed and the question repeated to allow the user to make a valid entry. 

![screenshot of error message associated with first question](/documentation/first_q_error.jpg)

This feature applies to all of the initial questions, so that if the invalid type of input is made, the error message appears and the opportunity to try again is presented until the valid type of characters has been inputted. 

Once all three of the initial questions are answered, a Rich loading graphic has been applied to demonstrate that some behind the scenes 'calculations' are taking place. This feature has been added to engage the user and lead to the final part of the initial questions. 

![Video showing the functionality of the loading graphic](/documentation/loading_graphic.gif)
![screenshot of the summary statement result of the initial questions](/documentation/intial_q_statement.jpg)

A summary statement is provided back to the user, repeating back the inputted data and asking the user to confirm if the details entered are correct. The user is invited to enter 'Y' or 'N'. Although the meaning of '(Y/N)' is not provided initially, if the user is unsure and enters anything other than 'Y' or 'N', an error message is displayed clearly explaining what is required to proceed. 

Once the statement is confirmed, the statement is also printed to the Google document.

![screenshot of the confirmation message and error message](/documentation/y_n.jpg)

Once the initial questions have been confirmed the next section is implemented. There is a small paragraph introducing this section and the first question is displayed, including examples of the types of entries that can be made. 

 The input field for the first question will allow for any characters to be entered with the only restriction being numbers only. If only numbers have been entered an Invalid input error will be displayed.

 The input field for the second question will only allow for numbers to be entered and will display an error message if any alphabetic characters are entered. 

 ![screenshot of subsequent questions with error messages displayed](/documentation/subsequent_questions.jpg)

The third question prompts the user to select the category that best fits the expense by entering a number between 1 and 4. The input field only accepts values within this range and will display an error message if an invalid number is entered.

The user is then prompted to confirm whether the details provided in the following questions are correct. If 'y' is entered, the program continues; if 'n' is entered, the subsequent questions are repeated.

![screenshot of the category question and error message](/documentation/select_category.jpg)

 Once 'y' has been selected a summary of the expense is displayed and a table is presented to display the expenses per category. The loading graphic is displayed again before the expense summary is displayed. The user is then prompted if they wish to enter more expenses. As additional expenses are added, the summary updates to reflect the new totals per category.

![screenshot of the expense summary](/documentation/expense_summary.jpg)

 Each time 'y' is selected the subsequent questions are repeated, allowing the user to input additional expenses. When the user has finished entering all expenses and selects 'n', the program proceeds to the final stage. The loading graphic is again displayed just before the final stage.

 The final stage displays the totals of all of the entered expenses. the statement also provides a value of how much money remains in your budget and how much this leaves the user for spending per day. This value is also displayed if there are negative values, and this is shown for reference to give the user an idea of how much more they may need to save before they can book that trip. 

 ![screenshot of final summary](/documentation/final_summary.jpg)
![screenshot of final question](/documentation/clear_doc.jpg)
 This is preceded with an explanation and link to the google doc, where a summary of the expenses per category and final summary is printed. The user is encouraged to copy and paste this summary for their own records.
 
 ![screenshot of google doc](/documentation/google_doc.jpg)

  Finally the user is asked if they have finished viewing the Google Doc. If 'n' is selected, the user is informed that the programme cannot end until 'y' is selected. This is because once 'y' is selected the google document will be wiped, ready for the next user.

  ![screenshot of final question](/documentation/final_message.jpg)

  Once 'y' has been selected the concluding message is presented and the programme ends.


### Future Features

There are a number of limitations currently to the programme. In future implementations I would consider adding or amending the following: 

* The google document updates at various stages throughout the programme, this creates an issue if the terminal is refreshed or restarted as the summaries may print to the document when not necessarily required by the user. A fix would need to be implemented to remove any prints if the terminal is restarted.
* The instructions and explanations within the programme are a bit unclear or clunky, I would look at refining the content to make it more user friendly and easier to navigate.

## Data Model

## Technologies used 
### Languages Used 
* Python
### Frameworks, Libraries & Programmes Used
* [Lucidchart](https://www.lucidchart.com/pages) - to map and plan the flow of the app
* [Github](https://github.com/) - For version control 
* VS Code - used as the code editor and to save files
* [Rich Library and Documentation](https://rich.readthedocs.io/en/stable/index.html)

## Testing 
### Bugs 
### Validator Testing 

## Deployment 
* Render

## Credits
### Code Used 
### Content
* [Rich Framework](https://rich.readthedocs.io/en/stable/index.html)
* [Rich library tutorials](https://calmcode.io/course/rich/introduction)
* [Rich README.md](https://github.com/textualize/rich/blob/master/README.md)
* [Lucidchart](https://www.lucidchart.com/pages) - to map and plan the flow of the app
* [Render](https://render.com/)
* [Endgrate.com - blog](https://endgrate.com/blog/how-to-get-document-texts-with-the-google-docs-api-in-python) - used as guidance to link Google Docs API and to create function to print to the google doc.
* [Google Workspace Guides](https://developers.google.com/workspace/docs/api/quickstart/python) - Guides used to enable API.
### Media
* [Internet Made Coder - youtube tutorial](https://www.youtube.com/watch?v=4TZ1K8EHT2M)
* [pixegami - youtube tutorial](https://www.youtube.com/watch?v=HTD86h69PtE)
* [pixegami - python-for-beginners repository](https://github.com/pixegami/python-for-beginners/tree/main)
### Documentation and Testing
* [Diffchecker](https://www.diffchecker.com/)
* [Chatgpt](https://chatgpt.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)
* [CI Render tutorial](https://code-institute-students.github.io/deployment-docs/03-render/)

### Acknowledgements
