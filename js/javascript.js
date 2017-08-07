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
  var ResAdvantagesSlideBtn1 = document.querySelector('.res-slider__toggle-visible-1');
  var ResAdvantagesSlideBtn2 = document.querySelector('.res-slider__toggle-visible-2');
  var ResAdvantagesSlideBtn3 = document.querySelector('.res-slider__toggle-visible-3');
  var ResSliderAdvantagesSlide1 = document.querySelector('.res-slider__slide-1');
  var ResSliderAdvantagesSlide2 = document.querySelector('.res-slider__slide-2');
  var ResSliderAdvantagesSlide3 = document.querySelector('.res-slider__slide-3');

  ResAdvantagesSlideBtn1.onclick = function() {
    ResSliderAdvantagesSlide1.classList.add("res-slider__slide_show");
    ResSliderAdvantagesSlide2.classList.remove("res-slider__slide_show");
    ResSliderAdvantagesSlide3.classList.remove("res-slider__slide_show");
  }

  ResAdvantagesSlideBtn2.onclick = function() {
    ResSliderAdvantagesSlide2.classList.add("res-slider__slide_show");
    ResSliderAdvantagesSlide1.classList.remove("res-slider__slide_show");
    ResSliderAdvantagesSlide3.classList.remove("res-slider__slide_show");
  }

  ResAdvantagesSlideBtn3.onclick = function() {
    ResSliderAdvantagesSlide3.classList.add("res-slider__slide_show");
    ResSliderAdvantagesSlide1.classList.remove("res-slider__slide_show");
    ResSliderAdvantagesSlide2.classList.remove("res-slider__slide_show");
  }
}


/*------------------responses-buttons----------------------*/
if(document.querySelector('body').classList.contains("body-index")) {
  var responsesPrev = document.querySelector('.responses__prev');
  var responsesNext = document.querySelector('.responses__next');
  var responses = document.querySelectorAll('.responses-item');

  var i = 0;

  responsesNext.onclick = function() {
    responses[i].classList.remove("res-slider__slide_show");
    i++;
    if(i > responses.length - 1) {
      i = 0
    }
    responses[i].classList.add("res-slider__slide_show");
  }

  responsesPrev.onclick = function() {
    if(responses[i].classList.contains("res-slider__slide_show")) {
      responses[i].classList.remove("res-slider__slide_show");
      i--;
      if(i < 0) {
        i = responses.length - 1
      }
        responses[i].classList.add("res-slider__slide_show");
    }
  }
}

/*------------------login-popup------------------------*/

var loginPopupOpen = document.querySelector('.login-button');
var loginPopup = document.querySelector('.login-popup');
var loginPopupClose = document.querySelector('.login-popup__close');

loginPopupOpen.onclick = function() {
  loginPopup.classList.add("login-popup_show");
}

loginPopupClose.onclick = function() {
  loginPopup.classList.remove("login-popup_show");
}
