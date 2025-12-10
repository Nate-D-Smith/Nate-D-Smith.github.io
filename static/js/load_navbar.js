document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");

  // Split the path to detect repo-based or root-based GitHub Pages
  const pathParts = window.location.pathname.split("/").filter(p => p.length > 0);

  let navbarPath;

  if (window.location.hostname === "localhost" || window.location.protocol === "file:") {
    // Local development
    navbarPath = "../../navbar.html";

  } else if (pathParts.length > 1) {
    // Repo-based GitHub Pages:  username.github.io/repoName/...
    const repoName = pathParts[0];
    navbarPath = `/${repoName}/navbar.html`;

  } else {
    // User-level GitHub Pages: username.github.io/...
    navbarPath = `/navbar.html`;
  }

  fetch(navbarPath)
    .then(response => response.text())
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
});
