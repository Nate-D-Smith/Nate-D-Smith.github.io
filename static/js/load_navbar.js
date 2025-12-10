document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");

  fetch("/templates/navbar.html")
    .then(response => response.text())
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
});
