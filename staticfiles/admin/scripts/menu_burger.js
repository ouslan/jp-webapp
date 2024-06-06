function toggleBurgerMenu() {
    const burgerMenu = document.querySelector('.burger_menu');
    burgerMenu.classList.toggle('burger_menu-open');
}

document.addEventListener("DOMContentLoaded", function () {
    const burgerOptions = document.querySelectorAll('.burger_menu li');

    burgerOptions.forEach(option => {
        option.addEventListener('click', () => {
            const burgerMenu = document.querySelector('.burger_menu');
            burgerMenu.classList.remove('burger_menu-open');
        });
    });

    document.addEventListener('click', function (event) {
        const burger = document.querySelector('.burger');
        const burgerMenu = document.querySelector('.burger_menu');
        if (!burger.contains(event.target) && !burgerMenu.contains(event.target)) {
            burgerMenu.classList.remove('burger_menu-open');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const input = document.querySelector('.input');
    const dropdown = document.querySelector('.dropdown');

    input.addEventListener('click', function() {
        dropdown.style.display = 'block';
    });

    document.addEventListener('click', function(event) {
        if (!input.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.style.display = 'none';
        }
    });
});
