document.addEventListener("DOMContentLoaded", function () {
    // initialize materialize sidenav
    const SIDENAV = document.querySelectorAll(".sidenav");
    M.Sidenav.init(SIDENAV, {});

    // initialize materialize parralax
    const PARALLAX = document.querySelectorAll(".parallax");
    M.Parallax.init(PARALLAX, {});
});