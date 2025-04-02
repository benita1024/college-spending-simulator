#  Markov Chain Simulator: Behavioral Modeling

This project simulates a user's journey through various **states** using a **Markov chain model**, where each action leads to probabilistic transitions. Built for academic exploration, this model offers insight into how choices over time influence state changes—financial, behavioral, emotional, or otherwise.

---

##  Objective

To model and simulate how individual decisions influence state transitions in a Markov chain over a fixed period of time (e.g., one week), based on predefined probabilities.

---

##  How It Works

- The simulation starts in an **initial** state.
- On each simulated "day" or "turn," the user selects one of several **actions**.
- The selected action determines a **set of probabilistic transitions** to other states.
- The simulation continues for a fixed number of steps or until an **absorbing state** is reached (if defined).
- The final state is displayed at the end, along with the path taken.

---

##  Features

- **Customizable states and actions**
- Probabilistic transitions driven by user choices
- Optional **absorbing states**
- **Command-line interface** for interactive play

---

##  Getting Started

### Clone the repo:
```bash
git clone https://github.com/yourusername/markov-simulator.git
cd markov-simulator
