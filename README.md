# Hogwarts Project: Welcome to Hogwarts

## 1. General Presentation

### Project Title
**Hogwarts: An Interactive Python Adventure**

### Brief Description
This project is an interactive text-based adventure game developed in Python, inspired by the *Harry Potter* universe. It allows a player to create a wizard character, explore the magical world, be sorted into a Hogwarts House, learn spells, and participate in a Quidditch match.

The game manages data using Python structures (dictionaries, lists) and external JSON files for persistence (inventory, spells, houses, quizzes).

### Contributors
* **Raphaël PICOT** [@raphixscrap](https://github.com/raphixscrap)
* **Lazare Gouttebroze** [@guimauve39631](https://github.com/Guimauve39631)
* **Group:** INT1

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
