/* ClimaP1 – main.js  */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Search form: show spinner on submit ── */
  const form   = document.getElementById('search-form');
  const btn    = document.getElementById('search-btn');
  const input  = document.getElementById('city-input');

  if (form && btn) {
    form.addEventListener('submit', (e) => {
      const city = input ? input.value.trim() : '';
      if (!city) { e.preventDefault(); return; }
      btn.classList.add('loading');
      btn.disabled = true;
    });
  }

  /* ── Stat cards: staggered fade-in entrance ── */
  const cards = document.querySelectorAll('.stat-card');
  cards.forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(16px)';
    card.style.transition = `opacity 0.4s ease ${i * 0.07}s, transform 0.4s ease ${i * 0.07}s`;
    // Trigger reflow then animate
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      });
    });
  });

  /* ── Back button: keyboard shortcut (Escape) ── */
  const backBtn = document.getElementById('back-btn');
  if (backBtn) {
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') backBtn.click();
    });
  }

  /* ── Input: clear on Escape if on index page ── */
  if (input) {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') input.value = '';
    });
  }
});
