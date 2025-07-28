document.addEventListener("DOMContentLoaded", () => {
  const launcher = document.getElementById("nova-launcher");
  const popup = document.getElementById("chat-popup");
  const sendBtn = document.getElementById("send-btn");
  const closeBtn = document.getElementById("close-btn");
  const input = document.getElementById("user-input");
  const messages = document.getElementById("chat-messages");

  // Auto show welcome message only
  setTimeout(() => {
    popup.style.display = "flex";
    launcher.style.display = "none";
    appendMessage("bot", "Hi, I’m Nova. How can I help you?");
  }, 1000);

  // Close popup
  closeBtn.addEventListener("click", () => {
    popup.style.display = "none";
    launcher.style.display = "block";
  });

  // Open chat again
  launcher.addEventListener("click", () => {
    popup.style.display = "flex";
    launcher.style.display = "none";
  });

  // Send message on button click or Enter
  sendBtn.addEventListener("click", sendMessage);
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    appendMessage("user", message);
    input.value = "";

    fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
      appendMessage("bot", data.response);
    })
    .catch(err => {
      console.error("Error:", err);
      appendMessage("bot", "Something went wrong. Please try again.");
    });
  }

  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    const icon = sender === "user" ? "🧑" : "🤖";
    msg.innerHTML = `<span class="icon">${icon}</span> <div class="markdown">${marked.parse(text)}</div>`;
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
  }
});