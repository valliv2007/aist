/*document.addEventListener('click', function(event) {
  let e = document.getElementById('cat_nav');
  let menu = document.getElementById('menu_header');
  if (e.contains(event.target)) {
      e.classList.toggle('open');
  } else if (menu.contains(event.target)) {
      document.getElementById('base_wrapper').classList.toggle('open');
  } else {
      e.classList.remove('open');
  }
});*/

/*
const popupButton = document.getElementById("button");

function myFunction() {
  console.log('hi')
}
*/
/*import url(../css/style.css);
import '../css/style.css';*/
import '../css/style.css';


const btn = document.querySelectorAll('services-general__card-btn')

btn.addEventListener('click', function (event) { // event доступен как параметр
    console.log(event); // его можно использовать в теле обработчика
});