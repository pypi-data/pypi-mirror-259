
"""
    @Author:				Henry Obegi <HenryObj>
    @Email:					hobegi@gmail.com
    @Creation:			    Thursday 18th of January 2024
    @LastModif:             
    @Filename:			    gpt.py
    @Purpose                Giving access to preconfigured GPT4 roles and functions.
    @Partof                 PIP package
"""

# ************** IMPORTS ****************
from .oai import *
import sys
import threading
import pathspec

# ****** PATHS & GLOBAL VARIABLES *******

BUFFER_README_INPUT = 30000
LARGE_INPUT_THRESHOLD = 10000  # Threshold for considering an input as large

# *************************************************************************************************
# *************************************** SUPPORT FUNCS *******************************************
# *************************************************************************************************

def contains_code(file_path: str) -> bool:
    """
    Check if the given file contains code based on its file extension.
    """
    # List of file extensions associated with code - can be increased.
    code_extensions = {'.py', '.js', '.jsx', '.java', '.c', '.cpp', '.cs', '.html', '.css', '.php', '.rb', '.swift', '.go'}
    _, file_extension = os.path.splitext(file_path)
    return file_extension in code_extensions

def joining_and_summarizing_modules(repository_path: str) -> str:
    """
    Process the modules in the repository and subdirectories to create the code context.
    """
    gitignore_spec = read_gitignore(repository_path)
    result, _ = process_directory(repository_path, "", 0, gitignore_spec)
    return result

def process_directory(directory_path: str, result: str, total_token: int, gitignore_spec) -> tuple:
    """
    Recursively process directories and files within the given path.
    """
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        # Check against .gitignore rules
        if gitignore_spec and gitignore_spec.match_file(full_path):
            continue  # Skip files and directories that match the .gitignore patterns
        if os.path.isdir(full_path):
            result, total_token = process_directory(full_path, result, total_token, gitignore_spec)
        elif contains_code(full_path):
            print(f"Processing the file {entry}")
            with open(full_path, "r") as doc:
                content = doc.read()
            file_token_count = calculate_token(content)  # Ensure calculate_token is defined elsewhere
            if total_token + file_token_count < MAX_TOKEN_WINDOW_GPT4_TURBO - BUFFER_README_INPUT:
                result += f"\n### START OF {entry} ###\n" + content + f"\n### END OF {entry} ###\n\n"
                total_token += file_token_count
            else:
                print("Repo is too large for a single README. Consider breaking down the content.")
                return result, total_token
    return result, total_token

def progress_indicator(message: str):
    """
    Display a dynamic progress indicator in the console.
    """
    for _ in range(10):
        for phase in [".   ", "..  ", "... "]:
            sys.stdout.write("\r" + message + phase)
            sys.stdout.flush()
            time.sleep(1)
    sys.stdout.write("\r" + " " * (len(message) + 5) + "\r")  # Clear line
    sys.stdout.flush()

def read_gitignore(directory_path: str):
    """
    Read the .gitignore file in the given directory and return a PathSpec object.
    """
    gitignore_path = os.path.join(directory_path, '.gitignore')
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as file:
            spec = pathspec.PathSpec.from_lines('gitwildmatch', file)
        return spec
    return None

# *************************************************************************************************
# ****************************************** GPT FUNCS ********************************************
# *************************************************************************************************

def gpt_bugbounty_generator(repository_path: str) -> str:
    """
    Enter the path of the repo and we will return a report of all possible bugs in it.

    Note:
        We query GPT-4 twice to improve the quality. We do not deal with large repo (for now)
    """
    get_code_content = joining_and_summarizing_modules(repository_path)
    query_message = "Querying GPT 4"
    if calculate_token(get_code_content) > LARGE_INPUT_THRESHOLD:
        query_message = "Querying GPT4. The repo is a large input so this might take some time, please wait"

    # Start a separate thread for the progress indicator
    progress_thread = threading.Thread(target=progress_indicator, args=(query_message,))
    progress_thread.start()

    first_bb_result = ask_question_gpt4(question=get_code_content, role=ROLE_BUG_BOUNTY)
    role_reviewer = generate_role_bug_bounty_reviewer(first_bb_result)
    improved_result = ask_question_gpt4(question=first_bb_result, role=role_reviewer)

    progress_thread.join()  # Wait for the progress indicator to finish
    return improved_result

def gpt_generate_bb_report(repository_path: str, verbose = True) -> None:
    """
    Take the repo path as an input and generate a new BB_Report in the repo. 
    
    Note: 
        We add a timestamp after the BugBounty Report (BB_Report) to avoid overwritting existing file.
    """
    new_readme = gpt_readme_generator(repository_path)
    now = get_now()
    readme_path = os.path.join(repository_path, f"BB_Report_{now}.md")
    with open(readme_path, "w") as file:
        file.write(new_readme)
    if verbose:
        print(f"✅ ReadMe is completed and available here 👉 {readme_path}")

def gpt_readme_generator(repository_path: str) -> str:
    """
    Enter the path of the repo and we will return the content of the ReadMe file.

    Note:
        We query GPT-4 twice to improve the quality. We do not deal with large repo (for now)
    """
    get_code_content = joining_and_summarizing_modules(repository_path)
    query_message = "Querying GPT 4"
    if calculate_token(get_code_content) > LARGE_INPUT_THRESHOLD:
        query_message = "Querying GPT4. The repo is a large input so this might take some time, please wait"

    # Start a separate thread for the progress indicator
    progress_thread = threading.Thread(target=progress_indicator, args=(query_message,))
    progress_thread.start()

    first_readme_result = ask_question_gpt4(question=get_code_content, role=ROLE_README_GENERATOR)
    role_reviewer = generate_role_readme_reviewer(first_readme_result)
    improved_result = ask_question_gpt4(question=first_readme_result, role=role_reviewer)

    progress_thread.join()  # Wait for the progress indicator to finish
    return improved_result

def gpt_generate_readme(repository_path: str, verbose = True) -> None:
    """
    Take the repo path as an input and generate a new README.md in the repo. 
    
    Note: 
        We add a timestamp after the README to avoid overwritting existing file.
    """
    new_readme = gpt_readme_generator(repository_path)
    now = get_now()
    readme_path = os.path.join(repository_path, f"README_{now}.md")
    with open(readme_path, "w") as file:
        file.write(new_readme)
    if verbose:
        print(f"✅ ReadMe is completed and available here 👉 {readme_path}")


# *************************************************************************************************
# ****************************************** PROMPTS **********************************************
# *************************************************************************************************
    
ROLE_README_GENERATOR = """
You are the best CTO and README.md writer. You follow best practices, you pay close attention to details and you are highly rigorous.

### Instructions ###
1. Think step by step.
2. Analyze the provided codebase, paying close attention to each module.
2. For each module:
   - Summarize its purpose and functionality.
   - Identify key functions and describe their roles.
   - Note any dependencies or important interactions with other modules.
3. Compile these insights into a well-structured README document that includes:
   - An overview of the entire codebase.
   - A description of each module, including its purpose, main functions, and interactions.
   - Any additional notes or observations that could aid in understanding or using the codebase effectively.

### Example of User Input ###
*** Start of file ***
// JavaScript code for a simple calculator

function add(a, b) {
   return a + b;
}

function subtract(a, b) {
   return a - b;
}

// More functions here...

*** End of file - calculator.js ***
*** Start of file ***
// CSS for styling the calculator

body {
   background-color: #f3f3f3;
}

// More styles here...

*** End of file - styles.css ***

### Expected Output: ###

README File:

- **Overview:**
  - The provided codebase consists of two main modules: a JavaScript file (`calculator.js`) for calculator functionalities and a CSS file (`styles.css`) for styling the calculator interface.

- **Module Descriptions:**
  1. `calculator.js`:
     - **Purpose:** Implements basic calculator functions.
     - **Key Functions:**
       - `key_function(a, b)`: Returns the of `a` and `b`.

  2. `styles.css`:
     - **Purpose:** Provides the styling for the calculator's user interface.
     - **Interactions:** This CSS file is used to style the HTML elements manipulated by `calculator.js`.

### Important Notes ###
1. You will be tipped $200 for the best and most comprehensive README.md file.
2. My job depends on the quality of the output so you MUST be exhaustive.
3. Do not give your opinion and ONLY return the full README content with Markdown format, nothing else. 
"""

def generate_role_readme_reviewer(current_readme: str) -> str:
    """
    Returns the role of the README reviewer.
    """
    return remove_excess(f"""
    You are the best CTO and README.md writer. You follow best practices, you pay close attention to details and you are highly rigorous.

    ### Instructions ###
    1. Think step by step.
    2. Analyze the below README file.
    3. Analyze carefully the codebase provided by the user, paying close attention to each module.
    3. For each module:
    - Summarize its purpose and functionality.
    - Identify key functions and describe their roles.
    - Note any dependencies or important interactions with other modules.
    4. Compare these notes with the current README file to ensure that the README file contains:
    - A valid overview of the entire codebase.
    - A description of each module, including its purpose, main functions, and interactions.
    - Any additional notes or observations that could aid in understanding or using the codebase effectively.
    5. Rewrite the full README content to ensure full exhaustivity, proper formatting, and detailed explanation.

    ### Current README ###
    {current_readme}
    ### Important Notes ###
    1. You will be tipped $200 for the best and most comprehensive README.md file.
    2. My job depends on the quality of the output so you MUST be exhaustive.
    3. Do not give your opinion and ONLY return the full README content with Markdown format, nothing else.
    """)

ROLE_BUG_BOUNTY = """
You are the best CTO with decades of experiences in computer science. You follow best practices, you pay close attention to details and you are highly rigorous.

$$$ Instructions $$$
1. Think step by step.
2. Analyze the provided codebase, paying close attention to each module.
2. For each module:
   - Note any dependencies or important interactions with other functions.
   - Assess if the code has any logical, typo, or syntax issues. You MUST take note of everything that can lead to a bug.
   - Important: You do NOT care about imports and functions that are mentioned but not defined.
3. After assessing all modules and all interactions between functions, write following Markdown formatting:
   - The correction needed for each function.
   - Any concrete and specific recommendation to make the code more robust.

$$$ Example of Input $$$
*** file app.py ***
// Python code for Fast API endpoint
@app.route("/knowledge/<id_client>")
def knowledge(id_client):
    connection = open_connection() # CON OPEN
    log_visit_in_app(connection, id_client, "knowledge") #logvisit
    credits = get_credits(connection, id_client)
    knowledge = get_all_knowledge(connection, id_client)
    know = []
    if not knowledge.empty:
    for index, row in knowledge.iterrows():
            know.append((row[0], row[1], row[2], row[4]))
    return render_template("knowledge.html", knowledge = know,  processing = False, id_client = id_client, credits = credits)

*** End of file ***

$$$ Expected Output: $$$

## Code Review Report
### `app.py` - `knowledge(id_client)` - Issues:

1. **For Loop Indentation**
```
if not knowledge.empty:
    for index, row in knowledge.iterrows():  
```
2. Connection Closure
- Add `connection.close()`before returning.

$$$ Important Notes $$$
1. You will be tipped $200 for the best and most comprehensive Bug Bounty report.
2. My job depends on the quality of the output so you MUST be exhaustive.
3. You do NOT care about imports and functions that are mentioned but not defined. You assume that every function without a code, works. You ONLY analyse the code provided.
4. Do not give general comments, ONLY specific issues with the way to resolve them. If you don't find any issue, simply say "No issue found".
"""

def generate_role_bug_bounty_reviewer(current_readme: str) -> str:
    """
    Returns the role of the Bug Bounty reviewer.
    """
    return remove_excess(f"""
    You are the best CTO and Bug Bounty Hunter. You specialise in finding code issues and bugs. You follow best practices, you pay close attention to details and you are highly rigorous.

    ### Instructions ###
    1. Think step by step.
    2. Analyze the below Bug Bounty file.
    3. Analyze carefully the codebase provided by the user, paying close attention to each module.
    For each module:
        - Note any dependencies or important interactions with other functions.
        - Assess if the code has any logical, typo, or syntax issues. You MUST take note of everything that can lead to a bug.
        - Important: You do NOT care about imports and functions that are mentioned but not defined.
    4. After assessing all modules and all interactions between functions, write following Markdown formatting:
        - The correction needed for each function.
        - Any concrete and specific recommendation to make the code more robust.

    ### Current Bug Bounty ###
    {current_readme}
    ### Important Notes ###
    1. You will be tipped $200 for the best and most comprehensive Bug Bounty report.
    2. My job depends on the quality of the output so you MUST be exhaustive.
    3. You do NOT care about imports and functions that are mentioned but not defined. You assume that every function without a code, works. You ONLY analyse the code provided.
    4. Do not give general comments, ONLY specific issues with the way to resolve them in Markdown format. If you don't find any issue, simply say "No issue found".
    """)

# *************************************************************************************************
# *************************************************************************************************
    
if __name__ == "__main__":
    pass
   
# WIP for future functions
'''
# Example of Request
REQUEST_WRITE_TEST = """
Write all the tests functions to ensure that the endpoints are correctly working. 
The tests must be broken down into smaller functions. If data is added to the DB, the data should then be removed from the DB if possible (ex: using the /delete endpoint).
print() statements must be used extensively to log on the console the various step and results of those tests.
Below is an example for the endpoints /training. Obviously, you need to do something more complete that this example and test ALL endpoints by calling one main functions which itself calls many smaller functions.
Provide a perfect code, ready to use, with all typing hints and simple docstrings.
"""

# Example of Request
REQUEST_REFACTOR = """
The file assistant.py is poorly made. It composes code snippets, some are useful, others are not. 
What we want is to refactor all this code to have all functions written as cleanly as oai_upload_file.
Write all functions needed to achieve the above results. Only return the code with the typing hint for each one.
"""
'''
