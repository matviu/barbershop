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

/*---------------slider-responses--------------------*/
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


/*------------------responses-buttons----------------------*/

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
  responses[i].classList.remove("res-slider__slide_show");
  i--;
  if(i < 0) {
    i = responses.length - 1
  }
    responses[i].classList.add("res-slider__slide_show");
}
