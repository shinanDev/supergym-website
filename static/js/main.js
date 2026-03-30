/* ============================================================
   SUPERGYM — main.js
   Globale JavaScript-Logik
   ============================================================ */


/* ------------------------------------------------------------
   Mobile Navigation — Hamburger Toggle
   ------------------------------------------------------------ */
(function () {
  const toggle = document.getElementById("navToggle");
  const links  = document.getElementById("navLinks");

  if (!toggle || !links) return;

  toggle.addEventListener("click", function () {
    const isOpen = links.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    toggle.setAttribute("aria-label",    isOpen ? "Menü schließen" : "Menü öffnen");
  });

  /* Menü schließen, wenn ein Link angeklickt wird */
  links.querySelectorAll(".navbar__link").forEach(function (link) {
    link.addEventListener("click", function () {
      links.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Menü öffnen");
    });
  });
})();
