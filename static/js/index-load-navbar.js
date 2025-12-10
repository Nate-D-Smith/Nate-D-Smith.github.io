document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");
  if (!container) return;

  fetch("navbar.html")   // same folder as index.html
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP " + response.status);
      }
      return response.text();
    })
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => {
      console.error("Navbar load error:", err);
      // Optional: show nothing instead of a 404 page
      container.innerHTML = "";
    });
});
