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

A summary of the results are printed to a Google document so the user is able to keep a record of their results to refer back to if required.

## Features
During the planning stages of my project, I utilized Lucidchart.com to brain storm and plan the algorithm which would be required to prepare for the flow of the programme.
![screenshot of Lucidchart algorithm](/documentation/lucid_chart_algo.webp) 

### Existing Features
The structure of the programme is split into an introduction and 3 other sections. 

The initial screen begins with a welcoming message, enhanced with emojis using the *Rich* framework. This is followed by an introduction to the program’s purpose, including a note that the results will be summarized and saved to an external Google document.

The introduction is separated by a line break before the initial questions are introduced and the first question is displayed. 

![screenshot of the initial screen](/documentation/intro_screen.jpg)

The *Rich* framework has been applied to style the text using a colour scheme to distinguish the main content and create some division whilst improving the user experience.

The next question is not displayed until the first question is satisfactorily answered. The input field is prepared to only accept a numerical value and if any letters are entered, an error message is displayed and the question repeated to allow the user to make a valid entry. 

![screenshot of error message associated with first question](/documentation/first_q_error.jpg)

This feature applies to all of the initial questions, so that if the invalid type of input is made, the error message appears and the opportunity to try again is presented until the valid type of characters has been inputted. 

Once all three of the initial questions are answered, a *Rich* loading graphic has been applied to demonstrate that some behind the scenes 'calculations' are taking place. This feature has been added to engage the user and lead to the final part of the initial questions. 

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

A summary of the the expense is then displayed to the user and then prompts the user to confirm whether the details provided are correct. If 'y' is entered, the program continues; if 'n' is entered, the subsequent questions are repeated.

![screenshot of the category question and error message](/documentation/select_category.jpg)

  The loading graphic is displayed again before the expense summary is displayed. The user is then prompted if they wish to enter more expenses. As additional expenses are added, the summary updates to reflect the new totals per category.

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

* The instructions and explanations within the programme are a bit unclear or clunky, I would look at refining the content to make it more user friendly and easier to navigate.

## Technologies used 
### Languages Used 
* Python
### Frameworks, Libraries & Programmes Used
* [Lucidchart](https://www.lucidchart.com/pages) - to map and plan the flow of the app
* [Github](https://github.com/) - For version control 
* VS Code - used as the code editor and to save files
* [*Rich* Library and Documentation](https://rich.readthedocs.io/en/stable/index.html)
* [chatgpt.com](https://chatgpt.com/) - used to help troubleshoot when encountering bugs in the system

### Code used 
* See *Category and table bug* under the *Bugs* section below. 


## Testing 
Testing was conducted continuously throughout the development of the programme. As each function was built, it was tested immediately, with necessary fixes implemented along the way.

Once the programme was completed I carried out manual testing as well asking a fellow student to provide any feedback and placed some fixes or streamlined some of the current processes. During my second meeting with my mentor Moritz, he suggested some improvements that I could make to make the processes work more efficiently and also improved the functioning of the google document. 

The fixes put in place are explained in the next section.

### Bugs 

#### Category and table bug
To enhance the visual presentation of the expenses summary, I used [*Rich*/tables](https://rich.readthedocs.io/en/stable/tables.html) and [*Rich*/Box](https://rich.readthedocs.io/en/stable/appendix/box.html#appendix-box) to display an ASCII-style table. While this significantly improved the console output, it introduced a formatting issue when the same output was sent to a Google Document, as the styling did not carry over correctly.

Additionally, the inclusion of emojis in the original category function caused issues, as the system failed to consistently recognize them as part of the string. Despite this, I felt it was important to retain the emojis to make the program more engaging and user-friendly.

To resolve the issue, I created two separate category objects—one with plain text for compatibility, and another styled version featuring emojis and colored text for enhanced terminal output.

![screenshot of the category objects](/documentation/styled_cat.jpg)
![screenshot or tables error in terminal](/documentation/table_error.jpg)

To resolve the issue of the formatting of the table to the Google document I carried out some internet searches to see how to resolve this but was unable to find a solution. I used *chatgpt* to see if there was any suggestion or enhancement that could be made and decided to use the code provided as shown in the screenshot below.
![screenshot of chatgpt suggestion](/documentation/chatgpt_table.jpg)

#### Colours bug
When developing the project in *VS Code*, the terminal had a white background, which influenced the initial color scheme for the text. However, after deploying the project to *Render*, it became clear that the chosen colors did not display well against a black background. To address this, I used [*Rich*/Colours](https://rich.readthedocs.io/en/stable/appendix/colors.html) to apply brighter, more vibrant colors that would stand out clearly and remain easy to read on dark backgrounds.
![screenshot of poor colour choice](/documentation/rich_color.jpg)

#### Overflow bug
Another issue identified on the deployed version was that when entering text or numbers into the input fields the words would be cut off when overflowing to the next line.

![screenshot of overflow issue](/documentation/overflow_bug.jpg)

After consulting the [*Rich*/text](https://rich.readthedocs.io/en/stable/reference/text.html), I applied the `overflow` parameter to ensure no words were split. 

 To improve user visuals I set the necessary input fields to start on the next line instead of the same.

#### £ bug
My fellow student Lana, who tested the programme for me identified that some of the input fields which required words and letters was prefixed with a £ sign. This was set up initially when the `get_input` function was created. 

![screenshot of input field with £ prefixed](/documentation/pound_error_2.jpg)
![screenshot of input field with £ prefixed](/documentation/pound_error_1.jpg)

To fix this I added an additional argument `show_symbol` with the default set to `False`. I then went through all the iterations of `get_input` and added the new argument, particularly entering the value of `True` in the two above questions. 

![screenshot of get_input function](/documentation/get_input_func.jpg)

#### Google Document hyperlink
When I first set up the project in VS Code, I created a hyperlink to the document via the terminal. However, after deploying the project to Render, the link no longer functioned as expected. I discussed the issue with my mentor, Moritz, who explained that this kind of functionality isn't supported in an external terminal in the same way, and suggested exploring alternative ways to share the link.

At first, I considered using the direct 'share link' from the Google Document, but the URL was quite long and didn’t look visually appealing within the program. To improve the appearance, I used [tinyurl.com](https://tinyurl.com/) to create a shortened version of the link. I also added a brief instruction prompting users to copy and paste the URL into a browser in order to access the Google Doc.

#### Clearing the Google Document 
When running through the progress of my project with my Mentor Moritz, he made some suggestions to improve the use of the Google Document. 

The initial version of the programme, printed to the Google document every time the programme was run. This meant that multiple entries were logged and there was no clear way to identify which results related to which user. 

I decided to create a new function to wipe all the content in the google document on confirmation by the user at the end of the programme. 
![screenshot of clear_google_doc function](/documentation/clear_google_doc.png)
![screenshot of clear_google_doc message](/documentation/clear_doc.jpg)

In addition another issue identified was that the google document updates at various stages throughout the programme, this creates an issue if the terminal is refreshed or restarted as the summaries may print to the document when not necessarily required by the user. 

To fix this I run the function `clear_google_doc` function at the very beginning of the programme to ensure the document is cleared at the start.

### Validator Testing 
The code has been run through the [CI Python Linter](https://pep8ci.herokuapp.com/) and no errors have been found.

![Screenshot of Python linter](/documentation/python_linter.jpg)

### User Experience
#### User Stories
**"I'm planning my first trip and researching holiday options, but I'm unsure if my current savings will be enough to afford it."**

**"There are a lot of different expenses attributed to planning my next holiday and I want to use something that can help me organize and display the breakdown of the expenses"**

**"I'm not very good with calculations and just want to be able to input in all the amounts and get an itemized response that clearly explains if I have enough in my budget or not"**

#### User Goals 
**Simple and straightforward questions** 

The main questions have been kept to a minimum of three per section, not including the confirmation questions. 

**Clear and concise result that displays the end results and whether or not the budget will allow for the trip.**

The program consolidates the results at the end of each section, presenting a summary statement and prompting the user to confirm whether they are satisfied with the information they’ve entered before proceeding.

At the conclusion of the program, a final summary is displayed. This includes the total of all entered expenses, the remaining budget, and a calculation of the daily spending allowance for the trip. If the user exceeds their budget, the remaining values are shown as negative figures.

The program ends with a final message, giving the user either a "green light" to go ahead and book the trip, or a "red light" suggesting they take some time to save more before proceeding.

**An itemized breakdown of the various types of expenses**

After the second set of questions is completed, a statement is displayed confirming the expense amount, its type, and the category it falls under.

Additionally, a summary table is shown, presenting the running total of expenses for each category. This table updates dynamically with each new expense entered.

At the end of the process, all expense statements—including the type, cost, and category—are written to the Google Document, along with a single summary table that outlines the total of all recorded expenses.

The user is encouraged to make a copy of the information in the google document for them to refer back to.

## Deployment 
This project has been deployed using [Render](https://render.com/) following the [CI Render Tutorial](https://code-institute-students.github.io/deployment-docs/15-pp3-deploy/). 

### Steps for Deployment: 
1. Log in and activate your Render account
2. Install your Render account to your Github profile to allow access to all repositories.
3. Select to create a new 'Web service' and connect to the relevant repository.
4. Create a name and ensure the settings are set for the closest region to you. Set the build command to ' pip install -r requirements.txt && npm install' and start command to ' node index.js'.
5. Set up the environment variables relevant to the project and ensure the credentials JSON file in the IDE has been copied and pasted as a secret file to ensure personal details are kept private.
6. Set the programme to Auto-Deploy, so that the project is deployed every time a commit is pushed to the repository. This will ensure the programme is up to date.
7. Select "Create Web Services" and wait for the deployment to complete.

## Credits
* [*Rich* Framework](https://rich.readthedocs.io/en/stable/index.html)
* [*Rich* library tutorials](https://calmcode.io/course/rich/introduction)
* [*Rich* README.md](https://github.com/textualize/rich/blob/master/README.md)
* [PEP8 guide](https://peps.python.org/pep-0008/)
* [Lucidchart](https://www.lucidchart.com/pages) - to map and plan the flow of the app
* [Render](https://render.com/)
* [Endgrate.com - blog](https://endgrate.com/blog/how-to-get-document-texts-with-the-google-docs-api-in-python) - used as guidance to link Google Docs API and to create function to print to the google doc.
* [Google Workspace Guides](https://developers.google.com/workspace/docs/api/quickstart/python) - Guides used to enable API.
* [Internet Made Coder - youtube tutorial](https://www.youtube.com/watch?v=4TZ1K8EHT2M)
* [pixegami - youtube tutorial](https://www.youtube.com/watch?v=HTD86h69PtE)
* [pixegami - python-for-beginners repository](https://github.com/pixegami/python-for-beginners/tree/main)
* [Diffchecker](https://www.diffchecker.com/)
* [Chatgpt](https://chatgpt.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)
* [CI Render tutorial](https://code-institute-students.github.io/deployment-docs/03-render/)
* [How to trade - Youtube - Google doc API tutorial](https://www.youtube.com/watch?v=j7JlI6IAdQ0)
* [Jie Jenn - Youtube - Google Drive API tutorial](https://www.youtube.com/watch?v=9K2P2bWEd90&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz)
* [Youtube - Google Workspace tutorial](https://www.youtube.com/watch?v=-dX-fWb3ogE)
* [DevOps Journey - Youtube - Python Rich tutorial](https://www.youtube.com/watch?v=JrGFQp9njas)
* [tinyurl](https://tinyurl.com/)
* [befunky.com](https://www.befunky.com/dashboard/)

### Acknowledgements
* Moritz Wach - my Code Institute Mentor who made himself available when I needed support and provided great suggestions of external frameworks that could be applied to this project as well as feedback to improve the functionality of the programme.
* LanaD_5P and Ivan Kimpl - fellow students who supported me throughout this project and provided encouragement and advice.
* Tom, Prash, Suraj, Anj and Nik - family and friends who helped to test out the site on various devices.