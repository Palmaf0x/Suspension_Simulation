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
    console.log(response)
}
// function to check for error
async function CheckAll(event) {
    event.preventDefault();

    if (mass.value === "" && raideur.value === "" && send_btn.value === "") {
        alert("You must define at least one parameters");
    }
    else if (init_position.value === "" && init_speed.value === "" && regime.value === "") {
        alert("You must define the initial position and initial speed")
    }
    else {
        await send_data()
    }
    window.location.href = "simulation.html";
}

// add the event listener
send_btn.addEventListener("click", CheckAll);









const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Simulation Data',
                    data: [12, 19, 3, 5, 2, 3],
                    borderColor: '#408A71',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });