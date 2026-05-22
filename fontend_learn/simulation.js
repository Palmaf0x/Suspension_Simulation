// creation of the function to get my datas
async function get_data() {
    let res = await fetch("http://127.0.0.1:8000/get_data")
    let result = await res.json()

    let x = result.x_values
    let y = result.y_values

    console.log(x, y)

    createChart(x, y)
}
// function to mahe the graph
function createChart(x, y) {
    const graph = document.getElementById("myChart")

    new Chart(graph, {
        type: "line",
        data: {
            labels: x,
            datasets: [{
                label: "Simulation",
                data: y,
                borderWidth: 2
            }]
        }
    })
}

// call the function ones my page load
get_data()

// get the download button
let btn = document.getElementById("btn-download")

function csv_dowload(){
    window.location.href = "http://127.0.0.1:8000/download_csv"
}

btn.addEventListener("click", csv_dowload)