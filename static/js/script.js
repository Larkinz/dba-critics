// enable strict mode
'use strict';

// album rating range type input slider element selectors
const RANGE_INPUT_ALBUM_001 = document.querySelector("#slider-album-001");
let rangeOutputAlbum001 = document.querySelector("#your-album-001-rating");
let album001SubmitBtn = document.querySelector("#album-001-submit-btn");
const RANGE_INPUT_ALBUM_002 = document.querySelector("#slider-album-002");
let rangeOutputAlbum002 = document.querySelector("#your-album-002-rating");
let album002SubmitBtn = document.querySelector("#album-002-submit-btn");
const RANGE_INPUT_ALBUM_003 = document.querySelector("#slider-album-003");
let rangeOutputAlbum003 = document.querySelector("#your-album-003-rating");
let album003SubmitBtn = document.querySelector("#album-003-submit-btn");
const RANGE_INPUT_ALBUM_004 = document.querySelector("#slider-album-004");
let rangeOutputAlbum004 = document.querySelector("#your-album-004-rating");
let album004SubmitBtn = document.querySelector("#album-004-submit-btn");

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

window.onload = function () {
    // album 001 range input slider functionality
    /* credits #5 (see README.md credits section) */
    if (RANGE_INPUT_ALBUM_001 != null) {
        RANGE_INPUT_ALBUM_001.oninput = function () {
            rangeOutputAlbum001.innerHTML = this.value;
            /* credits #6 (see README.md credits section) */
            album001SubmitBtn.removeAttribute('disabled');
        };
    }

    // album 002 range input slider functionality
    /* credits #5 (see README.md credits section) */
    if (RANGE_INPUT_ALBUM_002 != null) {
        RANGE_INPUT_ALBUM_002.oninput = function () {
            rangeOutputAlbum002.innerHTML = this.value;
            /* credits #6 (see README.md credits section) */
            album002SubmitBtn.removeAttribute('disabled');
        };
    }

    // album 003 range input slider functionality
    /* credits #5 (see README.md credits section) */
    if (RANGE_INPUT_ALBUM_003 != null) {
        RANGE_INPUT_ALBUM_003.oninput = function () {
            rangeOutputAlbum003.innerHTML = this.value;
            /* credits #6 (see README.md credits section) */
            album003SubmitBtn.removeAttribute('disabled');
        };
    }

    // album 004 range input slider functionality
    /* credits #5 (see README.md credits section) */
    if (RANGE_INPUT_ALBUM_004 != null) {
        RANGE_INPUT_ALBUM_004.oninput = function () {
            rangeOutputAlbum004.innerHTML = this.value;
            /* credits #6 (see README.md credits section) */
            album004SubmitBtn.removeAttribute('disabled');
        };
    }
};
