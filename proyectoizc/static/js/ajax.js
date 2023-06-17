var links = document.querySelectorAll('nav a');

for (var i = 0; i < links.length; i++) {
  links[i].addEventListener('click', scrollToSection);
}

function scrollToSection(event) {
  event.preventDefault();
  
  var targetId = event.currentTarget.getAttribute('href');
  var targetElement = document.querySelector(targetId);
  var targetOffsetTop = targetElement.offsetTop;
  
  window.scrollTo({
    top: targetOffsetTop,
    behavior: 'smooth'
  });
}
