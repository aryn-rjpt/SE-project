// Initialize Swiper 

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 4,
    centeredSlides: true,
    spaceBetween: 30,
    grabCursor: true,
    autoplay: {
        delay: 1000,
        pauseOnMouseEnter: true,
    }
});


// Loader
let loader = document.getElementById('myLoader')
window.addEventListener('load', function(){
    loader.style.display = 'none';
})