// Button_1 = document.querySelector('.menu-btn')
// Menu_1 = document.querySelector('.menu')
// Button_1.onclick = function(evnt){
//     evnt.preventDefault();
//   ('.menu').toggleClass('menu_active');
//  ('.content').toggleClass('content_active');
// }

$('.menu-btn').on('click', function(e) {
  e.preventDefault();
  $('.menu').toggleClass('menu_active');
  $('.content').toggleClass('content_active');
})