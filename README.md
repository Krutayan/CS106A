# CS106A: Programming Methodology (Stanford University)

Welcome to my repository containing solutions and independent projects built while working through Stanford University's foundational computer science curriculum, **CS106A** (via Code in Place). 

As an incoming 1st-year BTech student, I am using this rigorous curriculum to master algorithmic problem-solving, structural design patterns, and clean code habits before starting my formal college courses.

---

## 🛠️ Core Engineering Concepts Covered

* **Problem Decomposition:** Breaking down large procedural problems into small, single-responsibility helper functions.
* **Algorithmic Optimization ($O(N)$):** Reducing logical redundancies to write fast, memory-efficient code.
* **Edge-Case Matrix Scaling:** Designing flexible logic that dynamically scales to survive variable grid sizes and extreme environments without crashing.
* **Rigorous Documentation:** Implementing and enforcing strict `Pre-conditions` and `Post-conditions` to maintain predictable program behavior.

---

## 📂 Repository Structure

The code is strictly categorized into explicit domains to maintain clean portfolio architecture:

| Folder | Purpose | Highlights / Key Files |
| :--- | :--- | :--- |
| **`Assignments/`** | Milestone programs requiring complex, end-to-end algorithmic logic from scratch. | `Zebra_Crossing.py` (Scales dynamically to any $(5a+2) \times N$ matrix), `Rhoombha.py`, `zig_zag.py`, `Stone_Mason_Karel.py` |
| **`Solved_Examples/`** | A sandbox containing guided textbook exercises, lecture warmups, and core syntax checks. | `piles.py`, `put_n_beepers.py`, `puzzle_peice.py` |
| **`Own_Projects/`** | Custom baseline experiments written entirely outside class parameters to test logical boundaries. | `Write_Letter_L.py` |
| **`Intro_to_Python/`** | Transition phase code from the Karel simulator to native, terminal-based Python logic. | `hello_name.py`, control flow modules, variables, and console applications. |

---

## 🚀 Key Project Spotlight

### 🧩 1. Scalable Zebra Crossing Algorithm (`Zebra_Crossing.py`)
* **Problem:** Program a robot to paint alternating stripes on a grid of unknown dimensions.
* **Solution:** Instead of hardcoding steps, I calculated the structural matrix cycle pattern mathematically. The program handles any world with dimensions $(5a + 2) \times N$ (where $a \geq 0$ and $N \geq 1$) flawlessly by linking physical boundary triggers directly to conditional loops.

### 🧹 2. Roomba Floor Sweeper (`Rhoombha.py`)
* **Problem:** Clean an unpredictable room layout of all random debris (beepers).
* **Solution:** Optimized the cleaning patterns by cleaning column by column. Used advanced decomposition to ensure no empty moves were made, maintaining a highly efficient spatial navigation runtime.

---

## 📈 My Learning Roadmap

- [x] **Phase 1:** The Karel Environment (Control flow, Loops, Conditional sensors, Decomposition)
- [x] **Phase 2:** Transition to Pure Python (Console logic, Terminal Input/Output)
- [ ] **Phase 3:** Data Structures (Lists, Slicing, Dictionary mapping)
- [ ] **Phase 4:** File I/O & Text Parsing (.txt and .csv data streams)
- [ ] **Phase 5:** Object-Oriented Programming (OOP, Custom Classes, Blueprints)

---
*“Good code is its own documentation. A clean repository structure reflects a clear engineering mind.”* **Connect with me as I progress through my BTech journey!**
