document.addEventListener('DOMContentLoaded', function() {
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const images = document.querySelectorAll('.slider-image');
    const totalImages = images.length;
    const currentCaption = document.querySelector('.current');
    const totalCaption = document.querySelector('.total');
    
    let currentIndex = 0;

    function updateSlider() {
        document.querySelector('.slider-images').style.transform = `translateX(-${currentIndex * 100}%)`;
        currentCaption.textContent = `Изображение ${currentIndex + 1}`;
    }

    function showNextImage() {
        currentIndex = (currentIndex + 1) % totalImages;
        updateSlider();
    }

    function showPrevImage() {
        currentIndex = (currentIndex - 1 + totalImages) % totalImages;
        updateSlider();
    }

    prevButton.addEventListener('click', showPrevImage);
    nextButton.addEventListener('click', showNextImage);
    totalCaption.textContent = totalImages;
    updateSlider();
});
