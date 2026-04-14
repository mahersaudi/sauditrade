// Main JavaScript for Saudi Export & Trade Council

document.addEventListener('DOMContentLoaded', function() {

    // ===== SCROLL TOP BUTTON =====
    const scrollBtn = document.createElement('button');
    scrollBtn.id = 'scrollTop';
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(scrollBtn);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 400) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    scrollBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ===== COUNTER ANIMATION =====
    const counters = document.querySelectorAll('.counter-num');
    const observerOptions = { threshold: 0.5 };

    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target') || entry.target.innerText);
                const duration = 1800;
                const step = target / (duration / 16);
                let current = 0;
                const timer = setInterval(() => {
                    current += step;
                    if (current >= target) {
                        entry.target.innerText = target.toLocaleString();
                        clearInterval(timer);
                    } else {
                        entry.target.innerText = Math.floor(current).toLocaleString();
                    }
                }, 16);
                counterObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    counters.forEach(counter => counterObserver.observe(counter));

    // ===== FADE IN ANIMATION =====
    const fadeEls = document.querySelectorAll('.product-card, .category-card, .how-card, .cta-card, .factory-list-card, .value-card');
    const fadeObserver = new IntersectionObserver(function(entries) {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, i * 80);
                fadeObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    fadeEls.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(25px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        fadeObserver.observe(el);
    });

    // ===== SEARCH INPUT AUTO SUBMIT =====
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        const searchInput = searchForm.querySelector('input[name="q"]');
        if (searchInput) {
            searchInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    searchForm.submit();
                }
            });
        }
    }

    // ===== NAVBAR SCROLL EFFECT =====
    const navbar = document.querySelector('.main-navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.15)';
            } else {
                navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.08)';
            }
        });
    }

    // ===== AUTO DISMISS ALERTS =====
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    // ===== FORM VALIDATION STYLING =====
    const forms = document.querySelectorAll('form.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // ===== WHATSAPP BUTTON =====
    const waBtn = document.createElement('a');
    waBtn.href = 'https://wa.me/966110000000';
    waBtn.target = '_blank';
    waBtn.className = 'whatsapp-btn';
    waBtn.innerHTML = '<i class="fab fa-whatsapp"></i>';
    waBtn.title = 'WhatsApp';
    document.body.appendChild(waBtn);

});

