const totalSlidesCount = 5;

function updateCounter(swiperInstance) {
    const currentSlide = swiperInstance.realIndex + 1;
    document.getElementById('counter').innerText = `Изображение ${currentSlide} из ${totalSlidesCount}`;
}

const swiper = new Swiper('.swiper-container', {
    loop: true,
    slidesPerView: 1,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    on: {
        slideChange: function () {
            updateCounter(this);
        }
    }
});

updateCounter(swiper);
