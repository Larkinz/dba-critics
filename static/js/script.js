document.addEventListener("DOMContentLoaded", function () {
    // initialize materialize sidenav
    const SIDENAV = document.querySelectorAll(".sidenav");
    M.Sidenav.init(SIDENAV, {});

    // initialize materialize parralax
    const PARALLAX = document.querySelectorAll(".parallax");
    M.Parallax.init(PARALLAX, {});

    // initialize materialize slider
    const SLIDER = document.querySelectorAll(".slider");
    M.Slider.init(SLIDER, {
        indicators: false,
        interval: 8000,
    });

    // initialize materialize collapsible
    const COLLAPSIBLE = document.querySelectorAll(".collapsible.expandable");
    M.Collapsible.init(COLLAPSIBLE, {
        accordion: false
    });

    // initialize materialize modal
    const MODAL = document.querySelectorAll('.modal');
    M.Modal.init(MODAL, {
        endingTop: '25%'
    });
});