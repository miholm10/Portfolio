document.addEventListener('DOMContentLoaded', () => {
  const msg = document.getElementById('msg');
  const btn = document.getElementById('btn');

  // 1️⃣ Button click message
  if (btn && msg) {
    btn.addEventListener('click', () => {
      msg.textContent = 'Hello from Mikhail Holmes!';
    });
  }

  // 2️⃣ Handle list navigation links
  const navLinks = document.querySelectorAll('ol li a');
  navLinks.forEach(a => {
    a.addEventListener('click', e => {
      const url = a.getAttribute('data-url');
      const label = a.textContent.trim();

      // Prevent default only if there is no real URL
      if (!url) {
        e.preventDefault();
        msg.textContent = `${label} clicked`;
      } else {
        msg.textContent = `Opening ${label}...`;
        window.open(url, '_blank', 'noopener,noreferrer');
      }
    });
  });

  // 3️⃣ Auto-update footer year
  const yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});


