// getting the text and function make

let button = document.getElementById("button");
let email = document.getElementById("email");

async function sendEmail() {
    let response = await fetch("http://127.0.0.1:8000/receive")
    let data = await response.json()
    console.log(data)
    email.value = data.email
}

button.addEventListener("click", sendEmail);