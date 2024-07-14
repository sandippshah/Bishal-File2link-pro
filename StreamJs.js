//jaldi yeha se hato
// (c) lord krishna (c) biisal

// StreamJs.js

document.addEventListener("DOMContentLoaded", function () {
    const uncopyableElement = document.querySelector(".uncopyable");

    uncopyableElement.addEventListener("selectstart", function (event) {
        event.preventDefault();
    });

    // Function to fetch IMDb information
    function fetchIMDbInfo(movieName) {
        const apiKey = '7998b36c'; // Replace with your OMDb API key
        const apiUrl = `https://www.omdbapi.com/?t=${encodeURIComponent(movieName)}&apikey=${apiKey}`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.Response === "True") {
                    document.getElementById('imdbPoster').src = data.Poster;
                    document.getElementById('imdbTitle').textContent = data.Title;
                    document.getElementById('imdbRating').textContent = data.imdbRating;
                    document.getElementById('imdbGenres').textContent = data.Genre;
                    document.getElementById('imdbPlot').textContent = data.Plot;
                } else {
                    console.error('Error fetching IMDb data:', data.Error);
                }
            })
            .catch(error => {
                console.error('Error fetching IMDb data:', error);
            });
    }

    // Call the function with the movie name
    const movieName = "{{file_name}}"; // This should be replaced with the actual movie name from your context
    fetchIMDbInfo(movieName);
});

// Existing WOW.js initialization
new WOW().init();


async function getDets() {
    const apiKey = '7998b36c';  // Replace with your OMDb API key
    const randPage = Math.floor(1 + Math.random() * 100); // Random page number for popular movies
    const apiUrl = `http://www.omdbapi.com/?apikey=${apiKey}&s=movie&type=movie&page=${randPage}`;

    const movieCont = document.querySelector('.movieSug');
    const img = document.querySelector('.movieimg img');
    const movieDets = document.querySelector('.movieDets');
    const movieDetsMini = document.querySelector('.movieDets-mini');

    try {
        const data = await fetch(apiUrl);
        const resData = await data.json();

        if (resData.Error) {
            console.error('Error fetching movie data:', resData.Error);
            return;
        }

        const ranIndex = Math.floor(Math.random() * resData.Search.length);
        const movie = resData.Search[ranIndex];

        const movieDetailsUrl = `http://www.omdbapi.com/?apikey=${apiKey}&i=${movie.imdbID}`;

        const movieData = await fetch(movieDetailsUrl);
        const movieDetails = await movieData.json();

        movieDets.innerHTML = `
            <h3>Must-see blockbuster film!</h3>
            <h4><span>Title:</span> ${movieDetails.Title}</h4>
            <h4><span>Overview:</span> ${movieDetails.Plot || 'No overview available.'}</h4>
            <h4><span>Release Date:</span> ${movieDetails.Released}</h4>
            <h4><span>Vote Average:</span> ${movieDetails.imdbRating}</h4>
        `;

        movieDetsMini.innerHTML = `
            <h3><span>Title:</span> ${movieDetails.Title}</h3>
            <h3><span>Release Date:</span> ${movieDetails.Released}</h3>
            <h3><span>Vote Average:</span> ${movieDetails.imdbRating}</h3>
        `;

        img.src = movieDetails.Poster !== 'N/A' ? movieDetails.Poster : 'placeholder.jpg';
        movieCont.style.backgroundImage = `url(${movieDetails.Poster !== 'N/A' ? movieDetails.Poster : 'placeholder.jpg'})`;
    } catch (error) {
        console.error('Error fetching movie data:', error);
    }
}

window.addEventListener('load', getDets);





let homeBtn = document.querySelector(".home-btn")
let abtBtn = document.querySelector(".about-btn")
let dldBtn_outer = document.querySelector(".downloadBtn")
let file_name = document.querySelector(".file-name")
let about_nav = document.querySelector(".about-nav")
let bot_btn = document.querySelector('.bot-btn')
let contact_btn = document.querySelector('.contact-btn')
let links = document.querySelectorAll('.links a')
let bot_links = document.querySelectorAll('.bot-link a')
let chnl_link = document.querySelectorAll('.chnl-link a')
let abt_chnl = document.querySelector('.abt-chnl')
let contact = document.querySelectorAll('.contact a')
let footer = document.querySelector('footer')

let timer = 0

if (document.getElementById("heading").classList.contains("title")) {
    document.querySelector(".title").textContent = 'Pikashow Movies'
}

// adding under in home btn at first 
homeBtn.classList.add('active');

// when clicking about
abtBtn.addEventListener("click", () => {
    dldBtn_outer.style.display = "none";
    file_name.style.display = "none";
    footer.style.display = "none";
    about_nav.style.display = "block"
    about_nav.style.display = "block"
    about_nav.style.animation = "strtLoad 1s ease 0s forwards"



})
// when clicking home
homeBtn.addEventListener("click", () => {
    dldBtn_outer.style.display = "flex";
    file_name.style.display = "block";
    footer.style.display = "block";
    window.location.href = "#main";
    about_nav.style.animation = "strtLoad 1s ease 0s forwards"
    about_nav.style.display = "none"

})

abt_chnl.addEventListener("click", () => {
    timer = 1
    chnl_link.forEach((i) => {
        i.style.animation = `strtLoad 1s ease ${timer}s forwards, linksBtnAn 2s ease ${timer}s infinite `
        timer += 0.3;
    });
    timer = 0
});
function bot_btn_clicked() {
    var about_btn = document.querySelector(".about-btn")
    timer = 1;
    bot_links.forEach((i) => {
        i.style.animation = `linksBtnAn 2s ease ${timer}s infinite ,strtLoad 1s ease ${timer}s forwards`;
        timer += 0.3;
    });
    timer = 0;
    dldBtn_outer.style.display = "none";
    file_name.style.display = "none";
    footer.style.display = "none";
    about_nav.style.display = "block"
    about_nav.style.display = "block"
    about_nav.style.animation = "strtLoad 1s ease 0s forwards"
    var links = document.querySelectorAll('.nryt a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    about_btn.classList.add('active');
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    let wlcm = document.querySelector(".wlcm")
    wlcm.classList.add('active');
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    bot_btn.classList.add('active');
};
footer_bisal_btn_clicked = () => {
    timer = 1;
    contact.forEach((i) => {
        i.style.animation = `linksBtnAn 2s ease ${timer}s infinite ,strtLoad 1s ease ${timer}s forwards`;
        timer += 0.3;
    });

    timer = 0;
    var about_btn = document.querySelector(".about-btn")
    timer = 1;
    bot_links.forEach((i) => {
        i.style.animation = `linksBtnAn 2s ease ${timer}s infinite ,strtLoad 1s ease ${timer}s forwards`;
        timer += 0.3;
    });
    timer = 0;
    dldBtn_outer.style.display = "none";
    file_name.style.display = "none";
    footer.style.display = "none";
    about_nav.style.display = "block"
    about_nav.style.display = "block"
    about_nav.style.animation = "strtLoad 1s ease 0s forwards"
    var links = document.querySelectorAll('.nryt a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    about_btn.classList.add('active');
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    let wlcm = document.querySelector(".wlcm")
    wlcm.classList.add('active');
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    contact_btn.classList.add('active');
}

contact_btn.addEventListener("click", () => {
    timer = 1;
    contact.forEach((i) => {
        i.style.animation = `linksBtnAn 2s ease ${timer}s infinite ,strtLoad 1s ease ${timer}s forwards`;
        timer += 0.3;
    });

    timer = 0;
})

// btn animations 
let dldBtn = document.querySelectorAll('.downloadBtn button')
dldBtn.forEach((i) => {
    i.style.animation = `strtLoad 1s ease ${timer}s forwards, linksBtnAn 2s ease ${timer}s infinite`
    timer += 0.3;
    i.style.setProperty("--beforestyl", `button_shine ${2 + Math.random() * 7}s ease  ${Math.random() * 10}s infinite`);

})

timer = 0
links.forEach((i) => {
    i.style.animation = `linksBtnAn 2s ease ${timer}s infinite`
    timer += 0.3
    i.style.setProperty("--beforestyl", `button_shine ${2 + Math.random() * 7}s ease ${Math.random() * 10}s infinite`);

})
timer = 0
timer = 0

function toggleWidth(element) {
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });

    element.classList.add('active');
}
function toggleWidthnav(element) {
    var links = document.querySelectorAll('.nryt a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });

    element.classList.add('active');
    var links = document.querySelectorAll('.about-nav a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });
    let wlcm = document.querySelector(".wlcm")
    wlcm.classList.add('active');
}

if (!(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent))) {
    Shery.mouseFollower();
    Shery.makeMagnet(".magnet");
}


// file name showing 
var div = document.getElementById('myDiv');
var text = div.textContent;
if (text.length > 300) {
    div.textContent = text.slice(0, 300) + "....";
}

// video player 
const controls = [
    'play-large',
    'rewind', 'play',
    'fast-forward',
    'progress',
    'current-time',
    'duration',
    // 'mute',
    // 'volume',
    'captions',
    'settings',
    'pip',
    'airplay',
    'download',
    'fullscreen'
];
document.addEventListener('DOMContentLoaded', () => {
    const player = Plyr.setup('.player', { controls });
});

// disabling right click
document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
});
document.addEventListener('keydown', function (e) {
    if (
        e.key === 'F12' ||
        (e.ctrlKey && e.shiftKey && e.key === 'I') ||
        (e.ctrlKey && e.key === 'u') ||
        e.ctrlKey ||
        e.shiftKey ||
        e.altKey
    ) {
        e.preventDefault();
    }
});


const videolink = window.location.href;
const bisallink = videolink.replace("/watch/", "/");

function vlc_player() {
    const openbisallink = bisallink;
    const openVlc = `vlc://${openbisallink}`;
    window.location.href = openVlc;
}

function mx_player() {
    const openbisallink = bisallink;
    const openMx = `intent:${openbisallink}#Intent;package=com.mxtech.videoplayer.ad;end`;
    window.location.href = openMx;
}

function playit_player() {
    const openbisallink = bisallink;
    const openPlayit = `playit://playerv2/video?url=${openbisallink}`;
    window.location.href = openPlayit;
}

function s_player() {
    const openbisallink = bisallink;
    const openSplayer = `intent:${openbisallink}#Intent;action=com.young.simple.player.playback_online;package=com.young.simple.player;end`;
    window.location.href = openSplayer;
}

function km_player() {
    const openbisallink = bisallink;
    const openKmplayer = `intent:${openbisallink}#Intent;package=com.kmplayer;end`;
    window.location.href = openKmplayer;
}

function hd_player() {
    const openbisallink = bisallink;
    const openHDplayer = `intent:${openbisallink}#Intent;package=uplayer.video.player;end`;
    window.location.href = openHDplayer;
}

function bisalDownload() {
    const openbisallink = bisallink;
    window.location.href = openbisallink;
}
