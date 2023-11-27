const sliderLine = document.querySelector(".slider-line");
// const sliderLineText = document.querySelector(".slider-line-text");

const nextButton = document.querySelector(".button-next");
const prevButton = document.querySelector(".button-prev");
const dots = document.querySelectorAll(".dot");
// const links = document.querySelectorAll(".link");

let position = 0;
let positionText = 0;
let dotIndex = 0;
let linkIndex = dotIndex;

const nextSlide = () => {
  if (position < (11 - 1) * 398) {
    position += 398;
  } else {
    position = 0;
  }
  sliderLine.style.left = -position + "px";
};

const nextSlideText = () => {
  if (positionText < 880) {
    positionText += 440;
    dotIndex++;
    linkIndex++;
  } else {
    positionText = 0;
    dotIndex = 0;
    linkIndex = 0;
  }
  sliderLineText.style.left = -positionText + "px";
  thisSlide(dotIndex);
  thisLink(linkIndex);
};

const prevSlide = () => {
  if (position > 0) {
    position -= 398;
  } else {
    position = (11 - 1) * 398;
  }
  sliderLine.style.left = -position + "px";
  thisSlide(dotIndex);
  thisLink(linkIndex);
};

const prevSlideText = () => {
  if (positionText > 0) {
    positionText -= 440;
    dotIndex--;
    linkIndex--;
  } else {
    positionText = 880;
    dotIndex = dots.length - 1;
    linkIndex = links.length - 1;
  }
  sliderLineText.style.left = -positionText + "px";
  thisSlide(dotIndex);
  thisLink(linkIndex);
};

const thisSlide = (index) => {
  for (let dot of dots) {
    dot.classList.remove("active-dot");
  }
  dots[index].classList.add("active-dot");
};

const thisLink = (index) => {
  for (let link of links) {
    link.classList.remove("active-link");
  }
  links[index].classList.add("active-link");
};

nextButton.addEventListener("click", nextSlide);
nextButton.addEventListener("click", nextSlideText);

prevButton.addEventListener("click", prevSlide);
prevButton.addEventListener("click", prevSlideText);

// слайдер для страницы О нас, версия tablet
const sliderLineTablet = document.querySelector(".slider-line-tablet");

const nextButtonTablet = document.querySelector(".button-next-tablet");
const prevButtonTablet = document.querySelector(".button-prev-tablet");
const dotsTablet = document.querySelectorAll(".dot-tablet");

let positionTablet = 0;
let positionTextTablet = 0;
let dotIndexTablet = 0;
let linkIndexTablet = dotIndexTablet;

const nextSlideTablet = () => {
  if (position < (11 - 1) * 229) {
    position += 229;
  } else {
    position = 0;
  }
  sliderLineTablet.style.left = -position + "px";
};

const nextSlideTextTablet = () => {
  if (positionTextTablet < 880) {
    positionTextTablet += 440;
    dotIndexTablet++;
    linkIndexTablet++;
  } else {
    positionTextTablet = 0;
    dotIndexTablet = 0;
    linkIndexTablet = 0;
  }
  sliderLineTextTablet.style.left = -positionText + "px";
  thisSlide(dotIndexTablet);
  thisLink(linkIndexTablet);
};

const prevSlideTablet = () => {
  if (position > 0) {
    position -= 229;
  } else {
    position = (11 - 1) * 229;
  }
  sliderLineTablet.style.left = -position + "px";
  thisSlide(dotIndexTablet);
  thisLink(linkIndexTablet);
};

const prevSlideTextTablet = () => {
  if (positionText > 0) {
    positionText -= 440;
    dotIndexTablet--;
    linkIndexTablet--;
  } else {
    positionTextTablet = 880;
    dotIndexTablet = dotsTablet.length - 1;
    linkIndexTablet = links.length - 1;
  }
  sliderLineText.style.left = -positionText + "px";
  thisSlide(dotIndex);
  thisLink(linkIndex);
};

const thisSlideTablet = (index) => {
  for (let dotTablet of dotsTablet) {
    dotTablet.classList.remove("active-dot");
  }
  dotsTablet[index].classList.add("active-dot");
};

// const thisLink = (index) => {
//   for (let link of links) {
//     link.classList.remove("active-link");
//   }
//   links[index].classList.add("active-link");
// };

nextButtonTablet.addEventListener("click", nextSlideTablet);
nextButtonTablet.addEventListener("click", nextSlideTextTablet);

prevButtonTablet.addEventListener("click", prevSlideTablet);
prevButtonTablet.addEventListener("click", prevSlideTextTablet);

/*Кастомный селект*/

// const element = document.querySelector(".main-select");
// const choices = new Choices(element, {
//   searchEnabled: false,
//   itemSelectText: "",
//   noResultsText: "По Вашему запросу ничего не найдено",
// });

/*Show-hidden mainForm*/
const showButtonHeader = document.querySelector(".header-nav__button");
const closeButton = document.querySelector(".application-close");
const applicationForm = document.querySelector(".application-form");
const body = document.querySelector("body");
const header = document.querySelector("#header-section");

showButtonHeader.addEventListener("click", showForm);

function showForm() {
  header.style.position = "relative";
  header.style.backgroundColor = "rgba(0, 0, 0, 0.01)";
  body.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
  applicationForm.style.display = "flex";
}

closeButton.addEventListener("click", hiddenForm);

function hiddenForm() {
  header.style.position = "sticky";
  header.style.backgroundColor = "#FFF";
  body.style.backgroundColor = "#FFF";
  applicationForm.style.display = "none";
}

/*Show-hidden cityForm*/
const showExpand = document.querySelector(".header-expandMore");
const showCity = document.querySelector(".header-city");
const actualCity = document.querySelector(".actual-city");
const trueButton = document.querySelector(".actual-city__button--yellow");
const falseButton = document.querySelector(".actual-city__button--white");

showExpand.addEventListener("click", showSlectCity);
showCity.addEventListener("click", showSlectCity);

function showSlectCity() {
  actualCity.style.display = "flex";
}

trueButton.addEventListener("click", closeSlectCity);
falseButton.addEventListener("click", closeSlectCity);
falseButton.addEventListener("click", showPopUp);

function closeSlectCity() {
  actualCity.style.display = "none";
}

/*Show-hidden popUp*/
const popUp = document.querySelector(".popUp");

function showPopUp() {
  popUp.style.display = "block";
  header.style.position = "relative";
  header.style.backgroundColor = "rgba(0, 0, 0, 0.01)";
  body.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
}

const popUpClose = document.querySelector(".popUp-close");

popUpClose.addEventListener("click", closePopUp);

function closePopUp() {
  popUp.style.display = "none";
  header.style.position = "sticky";
  header.style.backgroundColor = "#FFF";
  body.style.backgroundColor = "#FFF";
}

/*Извлечение города в popUp*/
// const popUpCity = document.querySelector(".popUp-city");
// const popUpList = document
//   .querySelector(".popUp-list")
//   .addEventListener("click", (e) => {
//     let content = e.target.innerHTML;
//     popUpCity.value = content;
//   });

/*Скрытие кнопки*/
/*
const activeVideoAboutUs = document.querySelector(".video-aboutUs");
const btnPlay = document.querySelector(".btn-play");

activeVideoAboutUs.addEventListener("click", toggleStateVideo)

function toggleStateVideo() {
  btnPlay.style.display = btnPlay.style.display === 'none' ? 'block' : 'none';
}
*/

/*burger-menu*/
const headerLogo = document.querySelector('.header-logo');
const headerDescription = document.querySelector('.header-description');
const headerSection = document.querySelector('#header-section');
const mainSection = document.querySelector('#main-section');
const footer = document.querySelector('.footer');

const burgerOpen = document.querySelector('.burger-open');
const burgerClose = document.querySelector('.burger-close');
const burgerList= document.querySelector('.menu-burger__list');

/*Переход по ссылкам-якорям из формы*/
const menuBurgerItems = document.querySelector('.menu-burger__items');
menuBurgerItems.addEventListener('click', closeBurgerMenu);

burgerOpen.addEventListener("click",openBurgerMenu);
burgerClose.addEventListener("click",closeBurgerMenu);

function openBurgerMenu() {
  burgerOpen.style.display = 'none';
  burgerClose.style.display = 'block';
  burgerList.style.display = 'block';

  headerLogo.style.display = 'none';
  headerDescription.style.display = 'none';
  headerSection.style.borderBottom = "none";
  mainSection.style.display = 'none';
  footer.style.display = 'none';
}

function closeBurgerMenu() {
  burgerOpen.style.display = 'block';
  burgerClose.style.display = 'none';
  burgerList.style.display = 'none';

  headerLogo.style.display = 'block';
  headerDescription.style.display = 'block';
  headerSection.style.borderBottom = "1px solid #CBCCCE";
  mainSection.style.display = 'block';
  footer.style.display = 'block';
}

// const showButtonBurger = document.querySelector(".burger-nav__button");
// const applicationFormBurger = document.querySelector('.application-formBurger');

// showButtonBurger.addEventListener("click", showFormBurger)

// function showFormBurger() {
//   burgerOpen.style.display = 'none';
//   burgerClose.style.display = 'none';
//   burgerList.style.display = 'none';
//   applicationFormBurger.style.display = 'flex';
// }

// const applicationCloseBurger = document.querySelector(".application-closeBurger");

// applicationCloseBurger.addEventListener("click", hiddenForm)
// applicationCloseBurger.addEventListener("click", closeBurgerMenu)

const dropDownOpenMainBurger = document.querySelector(".dropDown-main-img-downBurger");
const dropDownCloseMainBurger = document.querySelector(".dropDown-main-img-upBurger");
const dropDownListMainBurger = document.querySelector(".dropDown-main-listBurger");
const applicationButtonBurger = document.querySelector(".application-button-burger");
const applicationCheckboxBurger = document.querySelector(".application-checkboxBurger");

dropDownOpenMainBurger.addEventListener("click",openDropDownBurger);

function openDropDownBurger() {
  applicationButtonBurger.style.display = "none";
  applicationCheckboxBurger.style.display = "none";
  dropDownOpenMainBurger.style.display = "none";
  dropDownCloseMainBurger.style.display = "block";
  dropDownListMainBurger.style.display = "block";
}

dropDownCloseMainBurger.addEventListener("click",closeDropDownBurger);

function closeDropDownBurger() {
  applicationButtonBurger.style.display = "block";
  applicationCheckboxBurger.style.display = "block";
  dropDownCloseMainBurger.style.display = "none";
  dropDownOpenMainBurger.style.display = "block";
  dropDownListMainBurger.style.display = "none";
}

