/* =====================================================
   EcoPath AI
   Main JavaScript File
===================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initAOS();
    initEarthRotation();
    initPlanner();
    initNavbar();
    initCounters();

});


/* =====================================================
   AOS
===================================================== */

function initAOS() {

    if (typeof AOS !== "undefined") {

        AOS.init({
            duration: 700,
            once: true
        });

    }

}


/* =====================================================
   Rotating Earth Icon
===================================================== */

function initEarthRotation() {

    const earth = document.getElementById("earthIcon");

    if (!earth) return;

    const icons = [
        "fa-earth-americas",
        "fa-earth-europe",
        "fa-earth-asia"
    ];

    let current = 0;

    setInterval(() => {

        earth.classList.remove(icons[current]);

        current = (current + 1) % icons.length;

        earth.classList.add(icons[current]);

    }, 3000);

}


/* =====================================================
   Weekly Planner Progress
===================================================== */

function initPlanner() {

    const checkboxes = document.querySelectorAll(".task-check");

    if (checkboxes.length === 0) return;

    checkboxes.forEach(box => {

        box.addEventListener("change", updateProgress);

    });

    updateProgress();

}


function updateProgress() {

    const checkboxes = document.querySelectorAll(".task-check");

    if (checkboxes.length === 0) return;

    const completed =
        document.querySelectorAll(".task-check:checked").length;

    const percent =
        Math.round((completed / checkboxes.length) * 100);

    const progressBar =
        document.getElementById("progressBar");

    const progressText =
        document.getElementById("progressText");

    if (progressBar) {

        progressBar.style.width = percent + "%";
        progressBar.setAttribute("aria-valuenow", percent);

    }

    if (progressText) {

        progressText.textContent = percent + "%";

    }

}


/* =====================================================
   Navbar Shadow
===================================================== */

function initNavbar() {

    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    window.addEventListener("scroll", () => {

        if (window.scrollY > 20) {

            navbar.classList.add("shadow");

        } else {

            navbar.classList.remove("shadow");

        }

    });

}


/* =====================================================
   Animated Counters
===================================================== */

function initCounters() {

    const counters =
        document.querySelectorAll("[data-count]");

    counters.forEach(counter => {

        const target =
            parseInt(counter.dataset.count);

        let current = 0;

        const step =
            Math.ceil(target / 60);

        const timer = setInterval(() => {

            current += step;

            if (current >= target) {

                current = target;

                clearInterval(timer);

            }

            counter.innerText = current;

        }, 20);

    });

}