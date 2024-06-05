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

document.addEventListener("DOMContentLoaded", function () {
    const searchMenu = document.getElementById('search-menu');
    const toggleSearchButton = document.getElementById('search-bar'); // replace with the actual ID of your button or link

    document.addEventListener('click', function (event) {
        if (!searchMenu.contains(event.target) && !toggleSearchButton.contains(event.target)) {
            searchMenu.style.display = 'none';
        }
    });
});

function toggleSearchMenu() {
    var searchMenu = document.getElementById('search-menu');
    if (searchMenu.style.display === 'none') {
        searchMenu.style.display = 'block';
    } else {
        searchMenu.style.display = 'none';
    }
}