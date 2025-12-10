document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");

  // Detect GitHub Pages repo root
  const repoName = window.location.pathname.split("/")[1];

  // Build correct path
  const basePath = window.location.hostname === "localhost"
    ? "../../navbar.html"
    : `/${repoName}/navbar.html`;

  fetch(basePath)
    .then(response => response.text())
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
});
