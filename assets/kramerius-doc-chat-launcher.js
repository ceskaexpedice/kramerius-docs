(() => {
  "use strict";

  const chatElementName = "kramerius-doc-chat";
  const chatApiUrl = "https://ai-api.inovatika.dev/kramerius-doc-api/";
  const chatStateChangeEventName = "kramerius-doc-chat-state-change";
  const scrollLockClassName = "doc-chat-open";
  const launcherScript = document.currentScript;

  if (!(launcherScript instanceof HTMLScriptElement) || !launcherScript.src) {
    throw new Error("Nelze zjistit URL skriptu launcheru AI asistenta.");
  }

  if (document.querySelector(".doc-chat-launcher")) {
    throw new Error("Launcher AI asistenta je na strance vlozen vicekrat.");
  }

  if (document.querySelector(chatElementName)) {
    throw new Error("Chatovaci komponenta je na strance vlozena vicekrat.");
  }

  const launcher = document.createElement("aside");
  launcher.className = "doc-chat-launcher";
  launcher.setAttribute("aria-label", "AI asistent dokumentace");

  const launcherButton = document.createElement("button");
  launcherButton.className = "doc-chat-launcher__button";
  launcherButton.type = "button";
  launcherButton.disabled = true;
  launcherButton.setAttribute("aria-busy", "true");
  launcherButton.setAttribute("aria-label", "Otevřít chat s AI asistentem");
  launcherButton.innerHTML = `
    <svg class="doc-chat-launcher__icon" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M4 4h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H8l-5 3V6a2 2 0 0 1 2-2Zm1 2v12.5L7.4 17H20V6H5Zm3 3h8v2H8V9Zm0 4h5v2H8v-2Z"></path>
    </svg>
    <span>Zeptat se AI</span>
  `;

  launcher.append(launcherButton);

  const chatElement = document.createElement(chatElementName);
  chatElement.setAttribute("api-url", chatApiUrl);
  chatElement.setAttribute(
    "logo-url",
    new URL("img/kramerius_logo.png", launcherScript.src).href,
  );
  chatElement.setAttribute("use-mock-response", "false");
  chatElement.setAttribute("use-placeholder-response", "true");

  document.body.append(launcher, chatElement);

  let chatApi = null;

  const requireChatApi = () => {
    if (
      chatApi === null ||
      typeof chatApi.open !== "function" ||
      typeof chatApi.isOpen !== "function"
    ) {
      throw new Error("API chatovaci komponenty neni pripraveno.");
    }

    return chatApi;
  };

  const applyChatState = (isChatOpen) => {
    if (typeof isChatOpen !== "boolean") {
      throw new Error("Komponenta ohlasila neplatny stav chatu.");
    }

    const wasChatOpen = launcher.hidden;
    launcher.hidden = isChatOpen;
    document.documentElement.classList.toggle(scrollLockClassName, isChatOpen);

    if (wasChatOpen && !isChatOpen) {
      launcherButton.focus({ preventScroll: true });
    }
  };

  chatElement.addEventListener(chatStateChangeEventName, (event) => {
    if (
      !(event instanceof CustomEvent) ||
      typeof event.detail?.isOpen !== "boolean"
    ) {
      throw new Error(
        "Komponenta ohlasila neplatnou udalost zmeny stavu chatu.",
      );
    }

    applyChatState(event.detail.isOpen);
  });

  launcherButton.addEventListener("click", () => {
    const readyChatApi = requireChatApi();
    readyChatApi.open();

    if (!readyChatApi.isOpen()) {
      throw new Error("Chatovaci komponenta se po prikazu open neotevrela.");
    }

    if (!launcher.hidden) {
      throw new Error("Komponenta po otevreni neohlasila zmenu stavu chatu.");
    }
  });

  const componentScript = document.createElement("script");
  componentScript.type = "module";
  componentScript.src = new URL(
    "kramerius-doc-chat-ui/doc-chat-ui.js",
    launcherScript.src,
  ).href;
  componentScript.addEventListener(
    "error",
    () => {
      throw new Error("Nepodarilo se nacist chatovaci komponentu.");
    },
    { once: true },
  );
  document.head.append(componentScript);

  customElements.whenDefined(chatElementName).then(() => {
    chatApi = window.krameriusDocChat ?? null;
    applyChatState(requireChatApi().isOpen());
    launcherButton.disabled = false;
    launcherButton.removeAttribute("aria-busy");
  });
})();
