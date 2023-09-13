document.getElementById("roller").addEventListener("click", rollD20);

function rollD20() {
    var number = document.getElementById("result");
    var result = Math.floor(Math.random() * 20) + 1;
    if (result == 20) {
        number.textContent = ("Congrats! You rolled a nat20!");
    } else if (result == 1) {
        number.textContent = ("Oh, no! You rolled a nat1!");
    } else {
        number.textContent = ("You rolled a " + result);
    }
}