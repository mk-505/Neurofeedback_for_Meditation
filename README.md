# 🧘‍♂️ Neurofeedback Meditation Tracker

This project uses **real-time EEG data** from a Ganglion board (via BrainFlow SDK) to provide **neurofeedback** during meditation. It monitors the user's brainwave activity across five frequency bands and visualizes how much time was spent in each mental state, helping users build mindfulness and self-awareness over time.

---

## 📡 How It Works

- Connects to the **Ganglion EEG board** via BrainFlow
- Collects EEG data from a single channel in real time
- Analyzes brainwave power across the following bands:
  - **Gamma** – Focus/Concentration
  - **Beta** – Active/Normal
  - **Alpha** – Calm Wakefulness
  - **Theta** – Deep Meditation
  - **Delta** – Deep Sleep
- Tracks how long the user stays in each state during the session
- Displays a bar chart summary at the end

---

## 🛠️ Technologies

- Python  
- [BrainFlow](https://brainflow.org/) (EEG data acquisition and signal processing)  
- Matplotlib (session summary visualization)  
- Keyboard (for session termination)

---

## ▶️ How to Use

1. Connect your **Ganglion board** (update the correct serial port if needed)
2. Run the script:
   ```bash
   python meditation_neurofeedback.py
   ```
3. Begin meditating — the system logs your dominant brain state every 5 seconds
4. Press the **spacebar** to stop the session
5. Review the session summary and visualization

---

## 📈 Sample Output

- Printed summary of time spent in each brainwave state (in minutes and %)
- Matplotlib bar chart showing duration across brainwave categories

---

## 🧠 Applications

- Meditation training
- Focus and mental state awareness
- Brain-computer interface exploration
