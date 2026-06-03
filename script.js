document.getElementById("year").textContent = new Date().getFullYear();

const FORM_ENDPOINT = "";
const CONTACT_EMAIL = "rob@redwoodaviationgroup.com";

const form = document.getElementById("contact-form");
const status = document.getElementById("form-status");

function setStatus(msg, type) {
  status.textContent = msg;
  status.className = "form__status" + (type ? " " + type : "");
}

function vals() {
  const d = new FormData(form);
  return {
    name:         (d.get("name") || "").toString().trim(),
    organization: (d.get("organization") || "").toString().trim(),
    email:        (d.get("email") || "").toString().trim(),
    phone:        (d.get("phone") || "").toString().trim(),
    interest:     (d.get("interest") || "").toString().trim(),
    message:      (d.get("message") || "").toString().trim(),
  };
}

function validate(v) {
  if (!v.name) return "Please enter your name.";
  if (!v.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.email))
    return "Please enter a valid email address.";
  if (!v.message) return "Please add a short message.";
  return null;
}

function buildBody(v) {
  return [
    `Name: ${v.name}`,
    `Organization: ${v.organization || "—"}`,
    `Email: ${v.email}`,
    `Phone: ${v.phone || "—"}`,
    `Interest: ${v.interest}`,
    "",
    "Message:",
    v.message,
  ].join("\n");
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const v = vals();
  const err = validate(v);
  if (err) { setStatus(err, "error"); return; }

  if (FORM_ENDPOINT) {
    try {
      setStatus("Sending…", "");
      const res = await fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form),
      });
      if (!res.ok) throw new Error();
      form.reset();
      setStatus("Thanks — your inquiry is on its way. We'll be in touch shortly.", "success");
    } catch {
      setStatus("Something went wrong. Please email us directly at " + CONTACT_EMAIL + ".", "error");
    }
    return;
  }

  const subject = `Leaseback inquiry — ${v.name}${v.organization ? " (" + v.organization + ")" : ""}`;
  window.location.href =
    `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(buildBody(v))}`;
  setStatus("Opening your email app with the inquiry prefilled.", "success");
});
