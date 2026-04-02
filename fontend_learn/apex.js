// get the document variables
let mass = document.getElementById("mass");
let friction = document.getElementById("friction");
let raideur = document.getElementById("raideur");
let send_btn = document.getElementById("send_btn");
let init_speed = document.getElementById("init_speed");
let init_position = document.getElementById("init_pos");
let regime = document.getElementById("regime");
// creation of the functions
function toNumberOrNull(value) {
  if (value === "") return null;

  const num = parseFloat(value);
  return isNaN(num) ? null : num;
}
// function to send data via API
async function send_data() {
    let data = await fetch("http://127.0.0.1:8000/send_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            parameters: [toNumberOrNull(mass.value), toNumberOrNull(friction.value), toNumberOrNull(raideur.value)],
            initial_speed: toNumberOrNull(init_speed.value),
            initial_position: toNumberOrNull(init_position.value),
            regime_wanted: regime.value
        }),
    })
    let response = await data.json()
    return response;
}

// function to check for error
async function CheckAll(event) {
    event.preventDefault();

    if (mass.value === "" && raideur.value === "" && send_btn.value === "") {
        alert("You must define at least one parameters");
    }
    else if (init_position.value === "" && init_speed.value === "") {
        alert("You must define the initial position and initial speed")
    }
    else if(regime.value === "") {
        alert("You must choose your regime wanted")
    }
    else {
        let response = await send_data()
        let x_values = response["x_values"];
        let y_values = response["y_values"];
        window.location.href = "simulation.html"
        return {
            x_values: x_values,
            y_values: y_values,
        };
    }
}

// add the event listener
send_btn.addEventListener("click", CheckAll);

