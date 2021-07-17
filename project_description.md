# Project Description & Conclusion

### Work Flow Logic
* First step is to get and validate user input
    * program specifies input can only be 'p', 'r', 's'
    * if invalid inputs are entered, ask user to re-enter input until a valid 
    input is received
* Next, determines computer's choice by using `random.randint()` function and import the `random` module
* Then, compare the two choices from user and computer
    * if both choices are the same, then the game is a tie
    * if user choose **rock**, then it will lose against **paper**, but win against **scissor**
    * if user choose **paper**, then it will lose against **scissor**, but win against **rock**
    * if user choose **scissor**, then it will lose against **rock**, but win against **paper**
 * Finally, ask the user if he or she still wants to continue playing
    * validate input as only 'y' or 'n' should be accepted
    
### Possible Improvement
* The mechanism for valid input checking can be improved:
    * use of try/except block
    * user inputs can be stored as `IntEnum` so inputs can be stored as `int`, so less string comparison is done
* Game logic has too many  `if/elif/else` statements  
    * maybe look into using dictionary data structure that describe the win conditions