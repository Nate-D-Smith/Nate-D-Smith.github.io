document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("navbar-container");

  // Detect if we're on GitHub Pages
  const pathParts = window.location.pathname.split("/");


  //
  // pathParts = ["", "repo", "templates", "groups", "jnim.html"]

  const repoName = pathParts[1];  // <-- your repo folder name on GitHub Pages

  let navbarPath;

  if (window.location.hostname === "localhost" || window.location.protocol === "file:") {
    // Local development
    navbarPath = "../../navbar.html";
  } else {
    // GitHub Pages (must include repo name!)
    navbarPath = `/${repoName}/navbar.html`;
  }

  fetch(navbarPath)
    .then(response => response.text())
    .then(html => {
      container.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
});

