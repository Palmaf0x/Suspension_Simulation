const API_BASE = "";
const mass = document.getElementById("mass");
const friction = document.getElementById("friction");
const raideur = document.getElementById("raideur");
const sendBtn = document.getElementById("send_btn");
const initSpeed = document.getElementById("init_speed");
const initPosition = document.getElementById("init_pos");
const regime = document.getElementById("regime");

function toNumberOrNull(value) {
  if (value.trim() === "") return null;
  const number = Number(value);
  return Number.isFinite(number) ? number : null;
}

async function sendData(payload) {
  const response = await fetch(`${API_BASE}/send_data`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const body = await response.json();
  if (!response.ok) throw new Error(body.detail || "Simulation failed.");
  return body;
}

async function checkAll(event) {
  event.preventDefault();
  const parameters = [mass, raideur, friction].map((input) => toNumberOrNull(input.value));
  if (parameters.every((value) => value === null)) {
    alert("Define at least one physical parameter.");
    return;
  }
  if (toNumberOrNull(initPosition.value) === null && toNumberOrNull(initSpeed.value) === null) {
    alert("Define an initial position or initial speed.");
    return;
  }
  if (!regime.value) {
    alert("Choose the requested damping regime.");
    return;
  }

  sendBtn.disabled = true;
  try {
    await sendData({
      parameters,
      initial_speed: toNumberOrNull(initSpeed.value),
      initial_position: toNumberOrNull(initPosition.value),
      regime_wanted: regime.value,
    });
    window.location.href = "simulation.html";
  } catch (error) {
    alert(error.message);
  } finally {
    sendBtn.disabled = false;
  }
}

sendBtn.addEventListener("click", checkAll);

