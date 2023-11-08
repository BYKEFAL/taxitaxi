const showCities = document.querySelector(".button");
const list = document.querySelectorAll("li");

function listOfCities() {
  list.forEach((i) => i.classList.toggle("hide"));
}

showCities.addEventListener("click", listOfCities);
