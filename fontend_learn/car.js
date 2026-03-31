function taskA () {
    return Promise.resolve("Task A done")
}

function taskB () {
    return Promise.resolve("Task B done")
}

function taskC () {
    return Promise.resolve("Task C done")
}

async function task_done() {
    let x =  taskA()
    let y =  taskB()
    let z =  taskC()
    let array = await Promise.all([x,y,z])
   console.log(array)
}

task_done()