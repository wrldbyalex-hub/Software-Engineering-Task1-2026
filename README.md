# Software Engineering Task 1 - Educational Python App
- **Student Name:** Alex Wearne
- **Target Audience:** Secondary Students

## How to use
- Before running the code, you need to install streamlit and the plugin code_editor:
    - pip install streamlit (if that doesn't work then try using python3 -m install streamlit)
    - pip install streamlit_code_editor (if that doesn't work use python3 -m pip install streamlit_code_editor)
- To run the code (for me at least (on mac)) use (in the terminal on vscode):
    - python3 -m streamlit run app.py 
- Once in the website, it should be self explanitory, but here are the key features:
    - You will first see a log in screen. As you don't have a account, type whatever username you want and the password you want. 
    - Then click sign up. Once that is done, use those same credentials to log in. 
    - Then you will be able to acess all the content, not just the homepage. To access each page, just click on the name of it in the sidebar, which will then direct you to said page. 
    - Some pages will have questions, which you will need to click to interact with. 
        - There are two types of questions; multiple choice and terminal questions.
        - Multiple choice questions can be answered by simply clicking on the answer you think is right. 
        - Terminal Questions will require you to click the code box, and then type the required code. On the final line, there will be a submit button on the right, and you will need to click this to submit it.
    - There is a test page, and questions on that will be answered with no haptics or feedback until you get to the final question. Each question appears after you answer the previous one, causing you to only see 1 and the start. Once you've done all of them, simply click the submit button to see your results. 
        - They will be stored on the final page, as well as any other times you take the test with the date and time you did it. 
    - Some pages will also have openable boxes or interactable graphs. Just click on a box to open it, and click on any buttons on the graph or scroll with your cursor on it to adjust the numbers shown. 

## Project Logbook (Progress Tracking)
- **Feb 27:** Started repository and set up project structure.
- **Feb 27:** Implemented the first structural element for the user welcome screen and established the sidebar.
- **Feb 27:** Changed the sidebar to be able to be collapsable and also movable 
- **Feb 28:** Updating page 2 to teach the user about strings, functions and variables.
- **Mar 2:** I added this dynamic progress bar using st.progress. It calculates the amount of completed session state variables against the total lesson count, the UI provides real-time feedback on learner advancement.
- **Mar 3:** I added a graph on the page to start adding more content there, and to show why one should learn python and not other languages. I also added a source link to prove that the stats are not made up. 
- **Mar 3:** I added tabs to "the basics" tab on the sidebar so that it wouldn't be one long page of scrolling. Furthermore, tabs are visually pleasing and each hold their own data, information and questions. 
- **Mar 3:** Did research on using questions, and found out that each question requires a key, similar to the sidebar.
- **Mar 3:** Added a second question in the strings tab to further someones understanding, with different results happening depending if you choose the right or wrong answer. 
- **Mar 3:** Updated opening page to have some statistics on python and some examples of the stuff you can do with it. 
- **Mar 3:** Finished the strings tab and changed the syntax error tab to the Functions tab, as I believe thats more important than alot of those. 
- **Mar 4:** Finshed the integers tab, with a table that included all main signs that you would use in your code.
- **Mar 4:** Started on the Variables tab, likely will Finish today and move on to week 2. 
- **Mar 4:** I designed a scenario-based debugging challenge to test the user's understanding of output functions. By simulating a real-world 'broken' script from a hypothetical game, requires the user to demonstrate syntax application.
- **Mar 5:** Currently trying to fix the problem with the script, as when the user enters the answer, even if its right it will say its wrong. My current theory is something is wrong with the brackets, as they are highlighted red on the website. 
- **Mar 6-13:** Added a Data Base called DB, also organised code into sections with titles for easy use, created log in and sign up page, as well as only showing the home page and not the content when logged out, and showing content when logged in. Furthermore, I also added a log out button on the side bar if they want to log out for some reason. Lastly, I make it so on the checkpoint page, questions appear after you do the question prior to it. 
- **Mar 13:** Changed the coding questions into a function to allow for easier use of it, and to allow to use it for different questions.
- **Mar 17:** Updated code. I also created new tabs and folders to call in in app.py so it isn't one long line of code and really unorganised. This was done to raise my marks (as read in the marking criteria)
- **Mar 18:** Bug fixes, such as the login button not appearing when on the conclusion page, and me missspelling the 'count' and 'connt'. Furthermore, I also changed the checkpoint page to show the next question after answering the question, not getting it right. 

## Requirements Definition
- Goal: Create an interactive web interface to teach Python in 4 weeks, with questions to test the knowledge that was learnt.
