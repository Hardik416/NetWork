document.addEventListener('DOMContentLoaded', function() {
    const loaderText = document.querySelector('.loader__text');
    const loader = document.querySelector('.loader');
    const slides = [...document.querySelectorAll('.slide')];
    const btnPrev = document.querySelector('.slider--btn__prev');
    const btnNext = document.querySelector('.slider--btn__next');

    let loadedImages = 0;
    let progress = { current: 0, target: 0 };
    let autoSlideInterval;

    // Initialize slider immediately
    initializeSlider();

    // Image loading
    const images = [...document.querySelectorAll('img')];
    const totalImages = images.length;

    images.forEach(image => {
        const img = new Image();
        img.onload = () => {
            loadedImages++;
            progress.target = loadedImages / totalImages;
            updateLoader();
        };
        img.src = image.src;
    });

    let loadingInterval = setInterval(() => {
        if (progress.target >= 1) {
            clearInterval(loadingInterval);
            hideLoader();
        }
    }, 100);

    function updateLoader() {
        progress.current = lerp(progress.current, progress.target, 0.1);
        const progressPercent = Math.round(progress.current * 100);
        if (loaderText) {
            loaderText.textContent = `${progressPercent}%`;
        }

        if (progressPercent >= 100) {
            hideLoader();
        }
    }

    function hideLoader() {
        if (loader) {
            setTimeout(() => {
                loader.style.opacity = '0';
                loader.style.pointerEvents = 'none';
            }, 500);
        }
    }

    function lerp(start, end, amt) {
        return (1 - amt) * start + amt * end;
    }

    function initializeSlider() {
        if (!slides.some(slide => slide.hasAttribute('data-current'))) {
            slides[0].setAttribute('data-current', '');
        }
        updateSlidePositions();
        startAutoSlide();
    }

    function updateSlidePositions() {
        const currentIndex = slides.findIndex(slide => slide.hasAttribute('data-current'));
        if (currentIndex === -1) return;

        // Hide all slides
        slides.forEach(slide => {
            slide.style.display = 'none';
            ['current', 'next', 'next-2', 'next-3', 'next-4', 'next-5',
             'previous', 'previous-2', 'previous-3', 'previous-4', 'previous-5']
            .forEach(attr => slide.removeAttribute(`data-${attr}`));
        });

        // Show current slide
        slides[currentIndex].style.display = 'block';
        slides[currentIndex].setAttribute('data-current', '');

        // Show next slides
        for (let i = 1; i <= 2; i++) {
            const nextIndex = (currentIndex + i) % slides.length;
            slides[nextIndex].style.display = 'block';
            slides[nextIndex].setAttribute(`data-next${i > 1 ? '-' + i : ''}`, '');
        }

        // Show previous slides
        for (let i = 1; i <= 2; i++) {
            const prevIndex = (currentIndex - i + slides.length) % slides.length;
            slides[prevIndex].style.display = 'block';
            slides[prevIndex].setAttribute(`data-previous${i > 1 ? '-' + i : ''}`, '');
        }
    }

    function nextSlide() {
        const currentIndex = slides.findIndex(slide => slide.hasAttribute('data-current'));
        if (currentIndex === -1) return;
        const nextIndex = (currentIndex + 1) % slides.length;
        slides.forEach(slide => slide.removeAttribute('data-current'));
        slides[nextIndex].setAttribute('data-current', '');
        updateSlidePositions();
    }

    function prevSlide() {
        const currentIndex = slides.findIndex(slide => slide.hasAttribute('data-current'));
        if (currentIndex === -1) return;
        const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
        slides.forEach(slide => slide.removeAttribute('data-current'));
        slides[prevIndex].setAttribute('data-current', '');
        updateSlidePositions();
    }

    btnNext.addEventListener('click', () => {
        nextSlide();
        resetAutoSlide();
    });

    btnPrev.addEventListener('click', () => {
        prevSlide();
        resetAutoSlide();
    });

    function startAutoSlide() {
        if (autoSlideInterval) {
            clearInterval(autoSlideInterval);
        }
        autoSlideInterval = setInterval(() => {
            nextSlide();
        }, 2000);
    }

    function resetAutoSlide() {
        clearInterval(autoSlideInterval);
        startAutoSlide();
    }

    slides.forEach(slide => {
        slide.addEventListener('mousemove', (e) => {
            if (!slide.hasAttribute('data-current')) return;

            const rect = slide.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateY = (x - centerX) / 20;
            const rotateX = (centerY - y) / 20;

            const inner = slide.querySelector('.slide__inner');
            if (inner) {
                inner.style.setProperty('--rotX', `${rotateX}deg`);
                inner.style.setProperty('--rotY', `${rotateY}deg`);
            }
        });

        slide.addEventListener('mouseleave', () => {
            const inner = slide.querySelector('.slide__inner');
            if (inner) {
                inner.style.setProperty('--rotX', '0deg');
                inner.style.setProperty('--rotY', '0deg');
            }
        });
    });

    document.querySelectorAll('.apply-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            alert('Application submitted successfully!');
        });
    });

    function simulateLoading() {
        if (progress.target < 1) {
            progress.target += 0.1;
            updateLoader();
            setTimeout(simulateLoading, 200);
        }
    }
    simulateLoading();
});
