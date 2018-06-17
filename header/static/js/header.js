toggle = $('.c-hamburger');
hed_open = $('#head_block');
toggle.click(function (e) {
    e.preventDefault();
      if (toggle.hasClass("is-active") === true){
          toggle.removeClass("is-active");
          hed_open.animate({
              height: 0
          }, 200);
      }
      else{
          toggle.addClass("is-active");
          autoHeightAnimate(hed_open, 200);
      }
});

if (window.location.pathname == '/' ) $('.bg_active').addClass("offset-1");
if (window.location.pathname.indexOf("t_shirt") !== -1 ) $('.bg_active').addClass("offset-3");
if (window.location.pathname.indexOf("pullover") !== -1 ) $('.bg_active').addClass("offset-5");
if (window.location.pathname.indexOf("hoodie") !== -1 ) $('.bg_active').addClass("offset-7");

function autoHeightAnimate(element, time){
    curHeight = element.height();
    autoHeight = element.css('height', 'auto').height();
  	element.height(curHeight);
    element.stop().animate({ height: autoHeight }, time);
}