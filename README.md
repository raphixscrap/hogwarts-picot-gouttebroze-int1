# Project: Welcome to Hogwarts

## 1. General Presentation

### Project Title
**Welcome to Hogwarts**

### Brief Description
This project is an interactive text-based adventure game developed in Python, inspired by the *Harry Potter* universe. It allows a player to create a wizard character, explore the magical world, be sorted into a Hogwarts House, learn spells, and participate in a Quidditch match.

The game manages data using Python structures (dictionaries, lists) and external JSON files for persistence (inventory, spells, houses, quizzes).

### Contributors
* **Raphaël PICOT** ([@raphixscrap)](https://github.com/raphixscrap))
* **Lazare GOUTTEBROZE** ([@guimauve39631](https://github.com/Guimauve39631))
* **Group:** P1 - INT1

**Repository Link:** [https://github.com/raphixscrap/hogwarts-picot-gouttebroze-int1](https://github.com/raphixscrap/hogwarts-picot-gouttebroze-int1)

---

## 2. Installation

### Prerequisites
* **Python 3.x** must be installed on your machine.
* This project uses only **native Python libraries** (`random`, `json`, `math`, etc.). 
* No external installation (`pip install`) is required.

### Installation Steps
1.  **Clone the repository:**
    Open your terminal and run the following command:
    ```bash
    git clone https://github.com/raphixscrap/hogwarts-picot-gouttebroze-int1.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd hogwarts-picot-gouttebroze-int1/hogwarts
    ```

3.  **Verify Data Files:**
    Ensure the `data/` folder contains the following JSON files required for the game to run:
    * `inventory.json`
    * `houses.json`
    * `spells.json`
    * `magic_quiz.json`
    * `teams_quidditch.json`

---

## 3. Usage

### How to Run the Application
To start the game, execute the `main.py` file from the root of the source folder:

```bash
python main.py
```

# 4. Logbook

### Task Distribution
We adopted a pair-programming approach for the core utilities, then divided the chapters to work in parallel before merging.

* **Raphaël PICOT:**
    * Lead development on `input_utils.py` and error handling.
    * Implementation of `chapter_1.py` (Diagon Alley logic) and `inventory.json`.
    * Development of the Quidditch engine in `chapter_4.py` (Team creation and match loop).

* **Lazare GOUTTEBROZE:**
    * Lead development on `universe/` modules (`character.py` and `house.py`).
    * Implementation of `chapter_2.py` (Sorting Hat logic) and `chapter_3.py` (Quiz and Spells).
    * Management of JSON data files (`houses.json`, `spells.json`, `magic_quiz.json`).

* **Collaborative Work:**
    * Designing the main menu flow in `menu.py`.
    * Debugging the Golden Snitch logic.
    * Final testing and writing the `README.md`.

---

# 5. Control, Testing, and Validation

### Input and Error Management
To ensure the game does not crash due to invalid user input, we centralized all interactions in `hogwarts/utils/input_utils.py`.

1.  **Type Validation (`ask_number`):**
    * We use a `try...except ValueError` block. If the user enters a string (e.g., "Harry") instead of a number, the function catches the error and recursively calls itself until a valid integer is entered.
2.  **Range Validation:**
    * The functions `ask_number` and `ask_choice` accept `min_val` and `max_val` arguments. If the user enters a number outside this range (e.g., choosing option 5 in a menu of 3 items), it raises a `ValueError` and prompts again.
3.  **Empty Strings (`ask_text`):**
    * We use the `.strip()` method to remove whitespace. A `while` loop prevents the user from entering an empty name or just spaces.

**Known Bugs:**
* *None.* The game runs through all 4 chapters without crashing on standard execution. JSON files must be present in the `hogwarts/data/` folder for the game to launch.

### Testing Strategies

We validated the project using two main strategies:

**1. Unit Testing (Input Utils):**
We tested the robustness of `input_utils.py` by deliberately entering incorrect data:
* *Test:* Input "abc" when asked for a menu choice.
* *Result:* The program displayed "Please enter a valid number" and did not crash.
* *Test:* Input "99" for a menu with 3 options.
* *Result:* The program requested a number between 1 and 3.

**2. Scenario Walkthroughs (Game Logic):**
We performed complete runs of the chapters to verify game logic:

* **Financial Logic Test (Chapter 1):**
    * *Action:* In `buy_supplies`, we tried to buy the "Invisibility Cloak" (100 Galleons) immediately.
    * *Result:* The system correctly calculated `100 - 100 = 0`, leaving 0 Galleons.
    * *Action:* Tried to buy a required item with 0 Galleons.
    * *Result:* The function blocked the purchase, and the "Game Over" condition was triggered correctly if requirements were not met.

* **Sorting Hat Test (Chapter 2):**
    * *Action:* We selected answers corresponding to "Ambition" and "Cunning".
    * *Result:* The `assign_house` function correctly calculated the highest score for Slytherin and assigned the character to that house.

* **Quidditch Match Test (Chapter 4):**
    * *Action:* We ran the match multiple times to verify the random "Golden Snitch" appearance.
    * *Result:* In some games, the match ended at Turn 20. In others, the Snitch was caught early (e.g., Turn 12), immediately ending the loop and awarding 150 points, confirming the `break` statement in the loop works.