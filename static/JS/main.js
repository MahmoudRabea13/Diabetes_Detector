let result = document.querySelector(".result")
const form  = document.getElementById('detect-form');
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("start-btn")) {
        location.assign('/login')
    }
    if (e.target.classList.contains("back-btn")) {
        location.assign('/login')
    }
})
form.addEventListener('submit', (e) => {
    result.style.display = "block"
});


