document.addEventListener("click", function (e) {
    if (e.target.classList.contains("start-btn")) {
        location.assign('/login')
    }
})

// const form  = document.getElementById('detect-form');
// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     console.log("GOOOOOO")
// });

// function sendUserinfo() {
//     let userpregnancies = document.getElementById('pregnancies').value
//     let userglucose = document.getElementById('glucose').value
//     let userbp = document.getElementById('bp').value
//     let userst = document.getElementById('st').value
//     let userinsulin = document.getElementById('insulin').value
//     let userbmi = document.getElementById('bmi').value
//     let userdpf = document.getElementById('dpf').value
//     let userage = document.getElementById('age').value
//     console.log(userpregnancies)
//     console.log(userglucose)
//     console.log(userbp)
//     console.log(userst)
//     console.log(userinsulin)
//     console.log(userbmi)
//     console.log(userdpf)
//     console.log(userage)
//     const request = new XMLHttpRequest()
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userpregnancies)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userglucose)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userbp)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userst)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userinsulin)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userbmi)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userdpf)}`)
//     request.send();
//     request.open(`POST`, `/ProcessuUserinfo/${JSON.stringify(userage)}`)
//     request.send();
// }