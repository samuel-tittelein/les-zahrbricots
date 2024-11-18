document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById("mode-toggle");
  const body = document.body;

  // Default to dark mode; check for saved preference
  if (localStorage.getItem("theme") === "light") {
    body.classList.add("light-mode");
    toggleButton.textContent = "🌙 Mode Sombre";
  }

  toggleButton.addEventListener("click", () => {
    body.classList.toggle("light-mode");

    // Update button text and save preference to localStorage
    if (body.classList.contains("light-mode")) {
      toggleButton.textContent = "🌙 Mode Sombre";
      localStorage.setItem("theme", "light");
    } else {
      toggleButton.textContent = "☀️ Mode Clair";
      localStorage.setItem("theme", "dark");
    }
  });
});
