let result = document.querySelector(".result")
document.addEventListener("click", function (e) {
    if (e.target.classList.contains("start-btn")) {
        location.assign('/login')
    }
    if (e.target.classList.contains("back-btn")) {
        location.assign('/login')
    }
})
const form  = document.getElementById('detect-form');
form.addEventListener('submit', (e) => {
    result.style.display = "block"
});



