# 🌟 AIDeskant

Welcome to AIDeskant! This project is an advanced, multi-functional interactive assistant capable of handling a wide range of tasks including database operations, input/output handling, and internet connectivity. Below is a detailed explanation of each module, its purpose, interactions, and example usage.

## 📑 Table of Contents

1. [💬 Output Module](#output-module)
2. [🎙️ Input Module](#input-module)
3. [🌐 Internet Module](#internet-module)
4. [💾 Database Module](#database-module)
5. [🔐 User Authentication Module](#user-authentication-module)
6. [ℹ️ Assistant Info Module](#assistant-info-module)
7. [🤖 AI Module](#ai-module)
8. [🔧 Utility Module](#utility-module)
9. [❓ Question Handling Module](#question-handling-module)
10. [🔋 Battery Status Module](#battery-status-module)
11. [👋 Greeting Module](#greeting-module)
12. [📚 Store New QA Module](#store-new-qa-module)
13. [🕒 Time Module](#time-module)
14. [🌐 Web Module](#web-module)
15. [🏁 Main Module](#main-module)

## 💬 Output Module

**Filename**: `Output_module.py`

**Purpose**: Handles output operations, primarily providing responses to the user.

**Functions**:
- `output(text)`: Prints text to the console.

**Interactions**:
- Used by almost all other modules to provide feedback and information to the user.

**Example Usage**:
- In `Greeting_Module.py`, the `output` function is used to greet the user.

## 🎙️ Input Module

**Filename**: `Input_module.py`

**Purpose**: Handles user input operations, including text input from the user.

**Functions**:
- `take_input()`: Captures and returns user input from the console.

**Interactions**:
- Used by modules that require user input, such as `Question_Handling_Module.py`.

**Example Usage**:
- In `User_Authentication_Module.py`, `take_input` is used to get the username and password from the user.

## 🌐 Internet Module

**Filename**: `Internet.py`

**Purpose**: Checks for an active internet connection and handles related tasks.

**Functions**:
- `check_internet_connection()`: Returns `True` if an internet connection is available, `False` otherwise.

**Interactions**:
- Used by modules that require internet access, such as `AI_Module.py` and `Web_Module.py`.

**Example Usage**:
- In `Store_New_QA_Module.py`, `check_internet_connection` is used before attempting to store information in the database.

## 💾 Database Module

**Filename**: `Database.py`

**Purpose**: Handles database operations, including creating tables, inserting data, and querying data.

**Functions**:
- `create_database()`: Creates the necessary tables in the database.
- `insert_data(table, data)`: Inserts data into the specified table.
- `query_data(query)`: Executes a query and returns the result.

**Interactions**:
- Used by modules that need to store or retrieve persistent data, such as `User_Authentication_Module.py` and `Store_New_QA_Module.py`.

**Example Usage**:
- In `User_Authentication_Module.py`, `insert_data` is used to store new user information.

## 🔐 User Authentication Module

**Filename**: `User_Authentication_Module.py`

**Purpose**: Handles user authentication, including checking for existing users and registering new users.

**Functions**:
- `login()`: Prompts the user for their username and password and checks if they are in the database.
- `register()`: Prompts the user to create a new username and password and stores them in the database.

**Interactions**:
- Uses `Input_module.py` to get user input and `Database.py` to store/retrieve user data.
- Uses `Output_module.py` to provide feedback to the user.

**Example Usage**:
- In the main program, `login` and `register` are called to manage user access.

## ℹ️ Assistant Info Module

**Filename**: `Assistant_Info_Module.py`

**Purpose**: Retrieves information about the assistant, such as the assistant's name and version.

**Functions**:
- `get_assistant_name()`: Returns the assistant's name.
- `get_version()`: Returns the assistant's version.

**Interactions**:
- Used by modules that need to reference the assistant's details, such as `Greeting_Module.py`.

**Example Usage**:
- In `Greeting_Module.py`, `get_assistant_name` is used to include the assistant's name in the greeting.

## 🤖 AI Module

**Filename**: `AI_Module.py`

**Purpose**: Contains functions for handling AI-related tasks, including generating responses using an AI model.

**Functions**:
- `generate_response(prompt)`: Uses an AI model to generate a response to the given prompt.

**Interactions**:
- Uses `Internet.py` to ensure there is an internet connection before generating a response.
- Provides AI-driven responses to the user, which can be used by various modules.

**Example Usage**:
- In `Question_Handling_Module.py`, `generate_response` is used to provide answers to user questions that are not in the database.

## 🔧 Utility Module

**Filename**: `Utility_Module.py`

**Purpose**: Provides utility functions, such as checking for the presence of a USB drive.

**Functions**:
- `check_usb_drive()`: Checks if a USB drive is connected to the system.

**Interactions**:
- Can be used by other modules that need to perform utility tasks.

**Example Usage**:
- In a hypothetical backup module, `check_usb_drive` could be used to ensure a USB drive is connected before attempting to back up data.

## ❓ Question Handling Module

**Filename**: `Question_Handling_Module.py`

**Purpose**: Handles asking the user questions and processing their answers.

**Functions**:
- `ask_question(question)`: Asks the user a question and processes their response.

**Interactions**:
- Uses `Input_module.py` to get user input and `Output_module.py` to display questions.
- Can use `AI_Module.py` to generate answers if the question is not in the database.

**Example Usage**:
- In `Main_Module.py`, `ask_question` could be used to interactively query the user.

## 🔋 Battery Status Module

**Filename**: `Battery_Status_Module.py`

**Purpose**: Checks and reports the battery status of the system.

**Functions**:
- `get_battery_status()`: Returns the current battery status.

**Interactions**:
- Uses `Output_module.py` to report battery status to the user.

**Example Usage**:
- In `Main_Module.py`, `get_battery_status` could be used to periodically check and report the battery status.

## 👋 Greeting Module

**Filename**: `Greeting_Module.py`

**Purpose**: Handles greeting the user and providing a friendly user experience.

**Functions**:
- `greet_user()`: Greets the user based on the time of day.

**Interactions**:
- Uses `Output_module.py` to display the greeting.
- Uses `Assistant_Info_Module.py` to include the assistant's name in the greeting.
- Uses `Time_Module.py` to determine the time of day for an appropriate greeting.

**Example Usage**:
- In `Main_Module.py`, `greet_user` is called when the assistant starts up.

## 📚 Store New QA Module

**Filename**: `Store_New_QA_Module.py`

**Purpose**: Handles storing new questions and answers into the database.

**Functions**:
- `store_question(question, conn=sqlite3.connect("memory.db"))`: Prompts the user to look up an answer in the database and store new questions and answers if not found.
- `direct_store_new_question()`: Allows users to directly store new questions and answers via terminal prompts.

**Interactions**:
- Uses `Input_module.py` to get user input and `Output_module.py` to provide feedback.
- Uses `Database.py` to store and retrieve questions and answers.

**Example Usage**:
- In `Main_Module.py`, `store_question` can be called to allow the user to add new information to the assistant's database.

## 🕒 Time Module

**Filename**: `Time_Module.py`

**Purpose**: Provides functions to get the current time and date.

**Functions**:
- `get_time()`: Returns the current time.
- `get_hours()`: Returns the current hour as a string.
- `get_date()`: Returns the current date as a string.

**Interactions**:
- Used by modules that need to reference the current time or date, such as `Greeting_Module.py`.

**Example Usage**:
- In `Greeting_Module.py`, `get_time` and `get_hours` are used to determine the appropriate greeting.

## 🌐 Web Module

**Filename**: `Web_Module.py`

**Purpose**: Handles opening and closing web browsers, as well as performing YouTube searches.

**Functions**:
- `open_browser()`: Opens the default browser.
- `close_browser()`: Closes the default browser.
- `open_chrome()`: Opens Google Chrome.
- `close_chrome()`: Closes Google Chrome.
- `open_firefox()`: Opens Firefox.
- `close_firefox()`: Closes Firefox.
- `youtube_search()`: Prompts the user for a YouTube search query and opens the results in the browser.

**Interactions**:
- Uses `Output_module.py` to provide feedback and `Input_module.py` to get user input.
- Uses `Assistant_Info_Module.py` to customize YouTube searches.

**Example Usage**:
- In `Main_Module.py`, `youtube_search` can be called to perform a YouTube search based on user input.

## 🏁 Main Module

**Filename**: `Main_Module.py`

**Purpose**: The main entry point of OmniAssist, coordinating all other modules and managing the main interaction loop.

**Functions**:
- `main()`: Runs the assistant, managing interactions and calling functions from other modules.

**Interactions**:
- Calls functions from all other modules to perform tasks based on user input.

**Example Usage**:
- When the assistant starts, `main` is called to begin interacting with the user, greet them, authenticate them, and process their requests.

## Data Flow and Module Interactions

1. **🚀 Startup**: `Main_Module.py` is executed, calling the `main()` function.
   - The assistant greets the user using `Greeting_Module.py`.
   - User authentication is handled by `User_Authentication_Module.py`.
   
2. **🗣️ User Interaction**: 
   - The assistant listens for user input using `Input_module.py`.
   - Based on the input, the appropriate module is called (e.g., `Question_Handling_Module.py` for questions, `Web_Module.py` for web tasks).

3. **⚙️ Task Execution**:
   - Modules like `AI_Module.py` may be called to generate responses.
   - Database operations are performed using `Database.py` to store or retrieve information.
   - Internet checks are done using `Internet.py` before performing tasks that require connectivity.

4. **🔄 Feedback**:
   - Responses and feedback are provided to the user using `Output_module.py`.

5. **💾 Data Storage**:
   - New questions and answers are stored using `Store_New_QA_Module.py`.

By separating concerns into different modules, OmniAssist is both modular and scalable, allowing for easy updates and maintenance. Each module has a specific role, interacting with others to create a seamless user experience.
