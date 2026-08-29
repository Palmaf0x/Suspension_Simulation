# Apex Dynamics: Vehicle Suspension Simulator & Parameter Optimizer

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

An interactive full-stack telemetry and simulation engine engineered to model quarter-car suspension dynamics, search for valid physical parameters across underdamped, critically damped, and overdamped regimes, and export numerical analyses to CSV.

---

## 📸 Interface & Previews

<div align="center">
  <img src="assets/configs.png" alt="Configuration Interface" width="48%" />
  <img src="assets/Exel_file.png" alt="Plot and Excel Export Data" width="48%" />
</div>

---

## 🚀 Key Features

* **Dynamic Parameter Solver:** Leaves missing physical parameters (mass $m$, stiffness $k$, damping $c$) unspecified and automatically searches configured ranges for valid regime configurations.
* **Physics Simulation Engine:** Solves second-order linear differential equations modeling spring-damper dynamics across three regimes:
    * `sous` (Underdamped)
    * `critique` (Critically Damped)
    * `sur` (Overdamped)
* **Real-Time Data Visualization:** Serves computed time-domain displacement and velocity vectors directly to a dynamic browser-based UI.
* **Analytical CSV Export:** Calculates damping amplitudes and settle times across parameter combinations for offline processing.

---

## 🛠️ System Architecture & Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript (Fetch API, Chart.js)
* **Backend:** FastAPI, Pydantic, Uvicorn
* **Data Processing:** NumPy, SciPy, Pandas

---

## 💻 Local Setup & Execution

### Prerequisites
* Python 3.10+ installed

### 1. Clone & Set Up Environment

```bash
git clone [https://github.com/Palmaf0x/Suspension_Simulation.git](https://github.com/Palmaf0x/Suspension_Simulation.git)
cd Suspension_Simulation

# Create and activate virtual environment
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1