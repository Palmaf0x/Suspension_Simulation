// creation of the functions
async function get_data() {
    let res = await fetch("http://127.0.0.1:8000/send_data")
    let result = await res.json()
    console.log(result)
}

get_data()