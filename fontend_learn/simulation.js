async function getData() {
  const response = await fetch("/get_data");
  const result = await response.json();
  if (!response.ok) throw new Error(result.detail || "No simulation data available.");
  createChart(result.x_values, result.y_values);
}

function createChart(x, y) {
  const graph = document.getElementById("myChart");
  new Chart(graph, {
    type: "line",
    data: {
      labels: x,
      datasets: [{
        label: "Displacement",
        data: y,
        borderWidth: 2,
        pointRadius: 0,
        borderColor: "#2563eb",
        tension: 0.15,
      }],
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: "Time (s)" } },
        y: { title: { display: true, text: "Displacement" } },
      },
    },
  });
}

const downloadButton = document.getElementById("btn-download");
downloadButton?.addEventListener("click", () => {
  window.location.href = "/download_csv";
});

getData().catch((error) => {
  const message = document.createElement("p");
  message.textContent = error.message;
  message.className = "error-message";
  document.querySelector("main")?.prepend(message);
});