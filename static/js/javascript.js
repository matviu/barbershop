/*--main-nav open---*/
(function(){

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

})();

/*--slider-advantages--*/
(function(){

  if(! (document.querySelector('body').classList.contains("body-index")) )  return ;


    var AdvantagesSlides = document.querySelectorAll('.advantages__item');
    var AdvantagesToggles = document.querySelectorAll('.slider__toggle-visible');

    var slideIndex = 1;
    showSlide(slideIndex);
    activateToggle(slideIndex);

    AdvantagesToggles[0].onclick = function() {
      showSlide(1);
      activateToggle(1);
    };

    AdvantagesToggles[1].onclick = function() {
      showSlide(2);
      activateToggle(2);
    };

    AdvantagesToggles[2].onclick = function() {
      showSlide(3);
      activateToggle(3);
    };

    function showSlide(slideIndex) {

      for (i = 0; i < AdvantagesSlides.length; i++) {
        AdvantagesSlides[i].classList.add("hidden");
      }

      AdvantagesSlides[slideIndex-1].classList.remove("hidden");

    };

    function activateToggle(slideIndex) {

      for (i = 0; i < AdvantagesToggles.length; i++) {
        AdvantagesToggles[i].style.backgroundColor = 'transparent';
      }

      AdvantagesToggles[slideIndex-1].style.backgroundColor = '#ffffff';
    }

})();

/*--slider-responses--*/
(function(){

  if(document.querySelector('body').classList.contains("body-index")) {

    var responsesList = document.querySelector('.responses-list');
    var responsesPrev = document.querySelector('.responses__prev');
    var responsesNext = document.querySelector('.responses__next');
    var dots = document.querySelectorAll('.res-slider__toggle-visible')

    responsesList.classList.remove('responses-list_nojs');

    var slideIndex = 1;
    showSlide(slideIndex);

    responsesPrev.onclick = function() {
      showSlide(slideIndex -= 1)
    }
    responsesNext.onclick = function() {
      showSlide(slideIndex += 1)
    }

    dots[0].onclick = function() {
      showSlide(slideIndex = 1)
    }
    dots[1].onclick = function() {
      showSlide(slideIndex = 2)
    }
    dots[2].onclick = function() {
      showSlide(slideIndex = 3)
    }

    function currentSlide(n) {
      showSlide(slideIndex = n);
    }


    function showSlide(n) {
      var i;
      var slides = document.querySelectorAll('.responses-item');

      if(n < 1) {slideIndex = slides.length}
      if(n > slides.length) {slideIndex = 1}

      for(i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      for(i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(' res-slider__toggle-visible_active', '')
      }

      slides[slideIndex - 1].style.display = "flex";
      dots[slideIndex - 1].className += " res-slider__toggle-visible_active";
    }
  }

})();

/*--login-popup--*/
(function(){

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

  loginPopup.onsubmit = function(event, callback) {
    if(!loginField.value || !passwordField.value) {
      event.preventDefault();
      loginPopup.classList.add("login-popup_error");
    }
  }

})();

/*--appointment-form xhr--*/
(function(){



})();
