/*-----------------main-nav open-----------------------*/
var mainNavToggle = document.querySelector('.main-nav__toggle');
var mainNav = document.querySelector('.main-nav');

mainNav.classList.remove("main-nav_nojs");

mainNavToggle.onclick = function() {

  if(mainNav.classList.contains("main-nav_closed")) {
    mainNav.classList.remove("main-nav_closed");
    mainNav.classList.add("main-nav_opened");
  } else {
    mainNav.classList.remove("main-nav_opened");
    mainNav.classList.add("main-nav_closed");
  }
}


/*---------------slider-advantages--------------------*/
if(document.querySelector('body').classList.contains("body-index")) {
  var AdvantagesSlideBtn1 = document.querySelector('.slider__toggle-visible-1');
  var AdvantagesSlideBtn2 = document.querySelector('.slider__toggle-visible-2');
  var AdvantagesSlideBtn3 = document.querySelector('.slider__toggle-visible-3');
  var sliderAdvantagesSlide1 = document.querySelector('.slider__slide-1');
  var sliderAdvantagesSlide2 = document.querySelector('.slider__slide-2');
  var sliderAdvantagesSlide3 = document.querySelector('.slider__slide-3');

  AdvantagesSlideBtn1.onclick = function() {
    sliderAdvantagesSlide1.classList.add("slider__slide_show");
    sliderAdvantagesSlide2.classList.remove("slider__slide_show");
    sliderAdvantagesSlide3.classList.remove("slider__slide_show");
  }

  AdvantagesSlideBtn2.onclick = function() {
    sliderAdvantagesSlide2.classList.add("slider__slide_show");
    sliderAdvantagesSlide1.classList.remove("slider__slide_show");
    sliderAdvantagesSlide3.classList.remove("slider__slide_show");
  }

  AdvantagesSlideBtn3.onclick = function() {
    sliderAdvantagesSlide3.classList.add("slider__slide_show");
    sliderAdvantagesSlide1.classList.remove("slider__slide_show");
    sliderAdvantagesSlide2.classList.remove("slider__slide_show");
  }
}

/*---------------slider-responses--------------------*/
if(document.querySelector('body').classList.contains("body-index")) {

  var slideIndex = 1;
  showSlide(slideIndex);

  function plusSlide(n) {
    showSlide(slideIndex += n)
  }

  function currentSlide(n) {
    showSlide(slideIndex = n);
  }


  function showSlide(n) {
    var i;
    var slides = document.querySelectorAll('.responses-item');
    var dots = document.querySelectorAll('.res-slider__toggle-visible')

    if(n < 1) {slideIndex = slides.length}
    if(n > slides.length) {slideIndex = 1}

    for(i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for(i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(' res-slider__toggle-visible_active', '')
    }

    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " res-slider__toggle-visible_active";
  }
}

/*------------------login-popup------------------------*/

var loginPopupOpen = document.querySelector('.login-button');
var loginPopup = document.querySelector('.login-popup');
var loginPopupClose = document.querySelector('.login-popup__close');
var loginField = document.querySelector('.login-popup__login-field');
var passwordField = document.querySelector('.login-popup__password-field');

loginPopupOpen.onclick = function() {
  loginPopup.classList.add("login-popup_show");
  loginField.focus();
}

loginPopupClose.onclick = function() {
  loginPopup.classList.remove("login-popup_show");
  loginPopup.classList.remove("login-popup_error");
}

window.onkeydown = function(event) {
  if(event.keyCode == 27 && loginPopup.classList.contains("login-popup_show")) {
    loginPopup.classList.remove("login-popup_show");
    loginPopup.classList.remove("login-popup_error");
  }
}

loginPopup.onsubmit = function(event) {
  if(!loginField.value || !passwordField.value) {
    event.preventDefault();
    loginPopup.classList.add("login-popup_error");
  }
}
