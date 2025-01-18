// Toggle class active hamburger menu

const navbarNav = document.querySelector(' .navbar-nav');

// ketika humburger menu di click
document.querySelector('#hamburger-menu').
onclick = (e) => {
navbarNav.classList.toggle('active');
e.preventDefault();
};

// Toggle class active untuk search form
const searchForm = document.querySelector('.search-form');
const searchBox = document.querySelector('#search-box');

document.querySelector('#search').onclick = (e) => {
    searchForm.classList.toggle('active');
    searchBox.focus();
    e.preventDefault();
};

// klik di luar sidebar untuk menghilangkan nav dan search box

const hm = document.querySelector('#hamburger-menu');
const sb = document.querySelector("#search");

document.addEventListener('click', function(e) {
    if(!hm.contains(e.target) && !navbarNav.contains(e.target)) {
        navbarNav.classList.remove('active');
    }

    if(!sb.contains(e.target) && !searchForm.contains(e.target)) {
        searchForm.classList.remove("active");
    }
});

