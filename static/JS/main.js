let result = document.querySelector(".result")
const form  = document.getElementById('detect-form');
let resultText = document.querySelector(".result-card h1")

document.addEventListener("click", function (e) {
    if (e.target.classList.contains("start-btn")) {
        location.assign('/insert-data')
    }
})

const myTimeout = setTimeout(myGreeting, 10000);

function myGreeting() {
    resultText.innerHTML=""
}
