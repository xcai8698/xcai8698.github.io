(() => {
  "use strict";
  const endpoint = (window.XCAI_ANALYTICS_ENDPOINT || "").trim().replace(/\/$/, "");
  if (!endpoint || !/^https:\/\/[a-z0-9-]+\.goatcounter\.com\/count$/i.test(endpoint)) return;
  const counterBase = endpoint.replace(/\/count$/, "");
  const script = document.createElement("script");
  script.async = true;
  script.src = "https://gc.zgo.at/count.js";
  script.dataset.goatcounter = endpoint;
  document.head.appendChild(script);

  function showCount(target, path, label) {
    fetch(counterBase + "/counter/" + encodeURIComponent(path) + ".json", { credentials: "omit" })
      .then(response => response.ok ? response.json() : null)
      .then(data => {
        if (!data || typeof data.count !== "string" || !target.isConnected) return;
        target.textContent = label + data.count;
        target.hidden = false;
      }).catch(() => {});
  }

  document.addEventListener("DOMContentLoaded", () => {
    const articleMeta = document.querySelector(".article-meta");
    if (articleMeta) {
      const item = document.createElement("span");
      item.className = "analytics-pageviews";
      item.hidden = true;
      item.setAttribute("aria-live", "polite");
      articleMeta.appendChild(item);
      showCount(item, window.location.pathname, "访问 ");
    }
    const footer = document.querySelector(".site-footer");
    if (footer) {
      const total = document.createElement("span");
      total.className = "analytics-total";
      total.hidden = true;
      total.setAttribute("aria-live", "polite");
      footer.insertBefore(total, footer.lastElementChild);
      showCount(total, "TOTAL", "全站访问 ");
    }
  });
})();
