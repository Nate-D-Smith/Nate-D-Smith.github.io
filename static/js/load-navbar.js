document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");

  const pathParts = window.location.pathname.split("/").filter(p => p.length > 0);

  let navbarPath;

  if (window.location.hostname === "localhost" || window.location.protocol === "file:") {

    navbarPath = "../../navbar.html";

  } else if (pathParts.length > 1) {
    const repoName = pathParts[0];
    navbarPath = `/${repoName}/navbar.html`;

  } else {
    navbarPath = `/navbar.html`;
  }

  fetch(navbarPath)
    .then(response => response.text())
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
});
