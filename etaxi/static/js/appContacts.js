// /*Кастомный селект*/
// const element = document.querySelector(".main-select");
// const choices = new Choices(element, {
//     searchEnabled: false,
//     itemSelectText: "",
//     noResultsText: 'По Вашему запросу ничего не найдено',
// })

/*Show-hidden mainForm*/
const showButtonHeader = document.querySelector(".header-nav__button");
const closeButton = document.querySelector(".application-close");
const applicationForm = document.querySelector(".application-form");
const body = document.querySelector("body");
const header = document.querySelector("#header-section");

showButtonHeader.addEventListener("click", showForm)

function showForm() {
  header.style.position = "relative";
  header.style.backgroundColor =  'rgba(0, 0, 0, 0.01)';
  body.style.backgroundColor =  'rgba(0, 0, 0, 0.1)';
  applicationForm.style.display = "flex";
}

closeButton.addEventListener("click", hiddenForm)

function hiddenForm() {
  header.style.position = "sticky";
  header.style.backgroundColor =  '#FFF';
  body.style.backgroundColor =  '#FFF';
  applicationForm.style.display = "none";
}


/*Show-hidden cityForm*/
const showExpand = document.querySelector(".header-expandMore");
const showCity = document.querySelector(".header-city");
const actualCity = document.querySelector(".actual-city");
const trueButton = document.querySelector(".actual-city__button--yellow");
const falseButton = document.querySelector(".actual-city__button--white");

showExpand.addEventListener("click",showSlectCity)
showCity.addEventListener("click",showSlectCity)

function showSlectCity() {
    actualCity.style.display = "flex";
}

trueButton.addEventListener("click",closeSlectCity)
falseButton.addEventListener("click",closeSlectCity)
falseButton.addEventListener("click",showPopUp)

function closeSlectCity() {
  actualCity.style.display = "none";
}

/*Show city on page contacts*/
// const showExpandAbout = document.querySelector(".header-cityAbout");
// const showCityAbout = document.querySelector(".header-expandMoreAbout");

// showExpandAbout.addEventListener("click",showPopUp)
// showCityAbout.addEventListener("click",showPopUp)



/*Show-hidden popUp*/
const popUp = document.querySelector(".popUp");

function showPopUp() {
  popUp.style.display = "block";
  header.style.position = "relative";
  header.style.backgroundColor =  'rgba(0, 0, 0, 0.01)';
  body.style.backgroundColor =  'rgba(0, 0, 0, 0.1)';
}

const popUpClose = document.querySelector(".popUp-close");

popUpClose.addEventListener("click",closePopUp)

function closePopUp() {
  popUp.style.display = "none";
  header.style.position = "sticky";
  header.style.backgroundColor =  '#FFF';
  body.style.backgroundColor =  '#FFF';
}


/*Извлечение города в popUp*/
// const popUpCity = document.querySelector('.popUp-city')
// const popUpList = document.querySelector('.popUp-list').addEventListener('click', e => {
// let content = e.target.innerHTML;
// popUpCity.value = content;
// });

const dropDownOpenContacts = document.querySelector(".dropDown-contacts-img-down");
const dropDownCloseContacts = document.querySelector(".dropDown-contacts-img-up");
const dropDownListContacts = document.querySelector(".dropDown-contacts-list");

dropDownOpenContacts.addEventListener("click",openDropDown)

function openDropDown() {
  // body.style.overflow =  'hidden';
  dropDownOpenContacts.style.display = "none";
  dropDownCloseContacts.style.display = "block";
  dropDownListContacts.style.display = "block";
}

dropDownCloseContacts.addEventListener("click",closeDropDown)

function closeDropDown() {
  // body.style.overflow =  'auto';
  dropDownCloseContacts.style.display = "none";
  dropDownOpenContacts.style.display = "block";
  dropDownListContacts.style.display = "none";
}


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