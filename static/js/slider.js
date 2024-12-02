let nextBtn = document.querySelector('.next');
let prevBtn = document.querySelector('.prev');
let dots = document.querySelectorAll('.dot');
let slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function ChangeSlide(n) {
    if (n < 0 || n >= slides.length) {
        throw new RangeError('OutOfRange');
    }

    slides.forEach((slide, i) => {
        slide.classList.remove('slide-active');
        slide.classList.add('slide-hide');
        if (i === n) {
            slide.classList.add('slide-active');
            slide.classList.remove('slide-hide');
        }
    });
}

function ChangeDot(n) {
    if (n < 0 || n >= slides.length) {
        throw new RangeError('OutOfRange');
    }
    dots.forEach((dot, i) => {
        dot.classList.remove('dot-active');
        if (i === n)
        {
            dot.classList.add('dot-active');
        }
    });
}

function NextSlide () {
    console.log('precurr: ', currentSlide);
    console.log('max: ', slides.length);
    if (currentSlide != slides.length - 1) 
    {
        currentSlide += 1;
    }
    else 
    {
        currentSlide = 0;
    }
    console.log('postcurr: ', currentSlide)
    ChangeSlide(currentSlide);
    ChangeDot(currentSlide);
}

function PrevSlide () {
    console.log('precurr: ', currentSlide);
    console.log('max: ', slides.length);
    if (currentSlide === 0) 
    {
        currentSlide = slides.length - 1;
    }
    else 
    {
        currentSlide -= 1;
    }
    console.log('postcurr: ', currentSlide)
    ChangeSlide(currentSlide);
    ChangeDot(currentSlide);
}

//setInterval(NextSlide, 2000);

try {
    nextBtn.addEventListener('click', () => {
        NextSlide();
    }); 

    prevBtn.addEventListener('click', () => {
        PrevSlide();
    });

    dots.forEach(dot => {
        dot.addEventListener('click', e => {
            let id = e.target.id;
            id = id.replace('dot_', '');
            console.log('id:', id);
            ChangeSlide(id - 1);
            ChangeDot(id - 1);
        });
    })

} catch(error) {
    console.log('???');
}
