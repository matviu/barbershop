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
