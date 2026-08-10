(function () {
  "use strict";

  function enhancePage() {
    var content = document.querySelector(".md-content__inner");
    if (!content) return;

    document.body.classList.toggle("is-kb-home", Boolean(content.querySelector(".kb-home-hero")));

    var meta = content.querySelector("[data-kb-article-meta]");
    var title = content.querySelector("h1");
    if (meta && title) {
      var articleText = content.innerText || "";
      var wordCount = articleText.trim().split(/\s+/).filter(Boolean).length;
      var readingMinutes = Math.max(1, Math.ceil(wordCount / 280));
      var readingTime = meta.querySelector("[data-kb-reading-time]");
      if (readingTime) readingTime.textContent = readingMinutes + " min read";

      var lead = title.nextElementSibling;
      var anchor = lead && lead.tagName === "P" ? lead : title;
      anchor.insertAdjacentElement("afterend", meta);
      meta.hidden = false;
    }

    var searchInput = document.querySelector("[data-md-component='search-query']");
    if (searchInput) searchInput.setAttribute("placeholder", "Search notes, genes, models…");

    var isApple = /Mac|iPhone|iPad/.test(navigator.platform || "");
    document.querySelectorAll("[data-kb-shortcut]").forEach(function (key) {
      key.textContent = isApple ? "⌘ K" : "Ctrl K";
    });
  }

  function openSearch() {
    var toggle = document.getElementById("__search");
    if (!toggle) return;
    toggle.checked = true;
    toggle.dispatchEvent(new Event("change", { bubbles: true }));
    window.setTimeout(function () {
      var input = document.querySelector("[data-md-component='search-query']");
      if (input) input.focus();
    }, 80);
  }

  document.addEventListener("keydown", function (event) {
    var target = event.target;
    var isTyping = target && (target.tagName === "INPUT" || target.tagName === "TEXTAREA" || target.isContentEditable);
    var isCommandK = (event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k";
    var isSlash = event.key === "/" && !isTyping && !event.metaKey && !event.ctrlKey && !event.altKey;
    if (isCommandK || isSlash) {
      event.preventDefault();
      openSearch();
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhancePage, { once: true });
  } else {
    enhancePage();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(enhancePage);
  }
})();
