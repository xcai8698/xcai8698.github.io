(() => {
  "use strict";

  const STORAGE_KEY = "co-notes-theme";
  const themeColor = {
    light: "#f7f7f4",
    dark: "#171b19"
  };

  function readSavedTheme() {
    try {
      const saved = window.localStorage.getItem(STORAGE_KEY);
      return saved === "light" || saved === "dark" ? saved : null;
    } catch {
      return null;
    }
  }

  function preferredTheme() {
    const saved = readSavedTheme();
    if (saved) return saved;
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function renderToggle(theme) {
    const button = document.querySelector("[data-theme-toggle]");
    if (!button) return;

    const isDark = theme === "dark";
    button.setAttribute("aria-pressed", String(isDark));
    button.setAttribute("aria-label", isDark ? "切换到白天模式" : "切换到黑夜模式");
    button.setAttribute("title", isDark ? "切换到白天模式" : "切换到黑夜模式");

    const icon = button.querySelector(".theme-toggle-icon");
    const label = button.querySelector(".theme-toggle-label");
    if (icon) icon.textContent = isDark ? "☼" : "☾";
    if (label) label.textContent = isDark ? "白天模式" : "黑夜模式";
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", themeColor[theme]);
    renderToggle(theme);
  }

  const initialTheme = preferredTheme();
  applyTheme(initialTheme);

  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector("[data-theme-toggle]");
    renderToggle(document.documentElement.dataset.theme || initialTheme);

    if (button) {
      button.addEventListener("click", () => {
        const nextTheme =
          document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        applyTheme(nextTheme);
        try {
          window.localStorage.setItem(STORAGE_KEY, nextTheme);
        } catch {
          // The theme still works for this page when storage is unavailable.
        }
      });
    }

    const mediaQuery = window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)");
    if (mediaQuery) {
      const syncWithSystem = (event) => {
        if (!readSavedTheme()) applyTheme(event.matches ? "dark" : "light");
      };
      if (typeof mediaQuery.addEventListener === "function") {
        mediaQuery.addEventListener("change", syncWithSystem);
      } else if (typeof mediaQuery.addListener === "function") {
        mediaQuery.addListener(syncWithSystem);
      }
    }
  });
})();
