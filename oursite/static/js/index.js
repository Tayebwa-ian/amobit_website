
$(document).ready(function(){
    $('div#search').hide();
    $('#search-button').click(function(){
        console.log('>>>>>>>>>>>>>>>>>>>>')
        $('div#search').show({})

    })
})

$(document).ready(function(){
    
    $('#start-search').click(function(){
        $('#search').hide();
    });
});


$('#main-slider').owlCarousel({
    items:1,
    nav:true,
    dots: true,
    autoplay: true,
    autoplayHoverPause: true,
    dotsSpeed: 400,
});



/*
**
sticky navbar
**/

window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;


function myFunction() {
  console.log(window.pageYOffset)
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
