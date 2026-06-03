// Redwood Aviation Group — landing page interactions

// Current year in footer
document.getElementById("year").textContent = new Date().getFullYear();

// Contact form handling.
//
// This static site has no backend, so by default the form composes an email to
// Redwood Aviation Group using the visitor's mail client (mailto). This works
// immediately on any static host (e.g. GitHub Pages) with no signup.
//
// To capture leads automatically instead, sign up for a form endpoint (e.g.
// Formspree at https://formspree.io) and set FORM_ENDPOINT below to your URL.
// When set, submissions are POSTed there and the page shows a success message.
const FORM_ENDPOINT = ""; // e.g. "https://formspree.io/f/your-id"
const CONTACT_EMAIL = "redwoodav8@gmail.com";

const form = document.getElementById("contact-form");
const note = document.getElementById("form-note");

function setNote(message, type) {
  note.textContent = message;
  note.className = "form-note" + (type ? " " + type : "");
}

function getValues() {
  const data = new FormData(form);
  return {
    name: (data.get("name") || "").toString().trim(),
    organization: (data.get("organization") || "").toString().trim(),
    email: (data.get("email") || "").toString().trim(),
    phone: (data.get("phone") || "").toString().trim(),
    interest: (data.get("interest") || "").toString().trim(),
    message: (data.get("message") || "").toString().trim(),
  };
}

function validate(v) {
  if (!v.name) return "Please enter your name.";
  if (!v.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.email))
    return "Please enter a valid email address.";
  if (!v.message) return "Please add a short message.";
  return null;
}

function buildEmailBody(v) {
  return [
    `Name: ${v.name}`,
    `Flight school / operation: ${v.organization || "—"}`,
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
  const v = getValues();

  const error = validate(v);
  if (error) {
    setNote(error, "error");
    return;
  }

  // Preferred path: POST to a configured form endpoint.
  if (FORM_ENDPOINT) {
    try {
      setNote("Sending…", "");
      const res = await fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form),
      });
      if (!res.ok) throw new Error("Request failed");
      form.reset();
      setNote("Thanks — your inquiry is on its way. We'll be in touch shortly.", "success");
    } catch (err) {
      setNote(
        "Something went wrong sending the form. Please email us directly at " +
          CONTACT_EMAIL + ".",
        "error"
      );
    }
    return;
  }

  // Fallback: open the visitor's email client with a prefilled message.
  const subject = `Leaseback inquiry — ${v.name}${
    v.organization ? " (" + v.organization + ")" : ""
  }`;
  const mailto =
    `mailto:${CONTACT_EMAIL}` +
    `?subject=${encodeURIComponent(subject)}` +
    `&body=${encodeURIComponent(buildEmailBody(v))}`;
  window.location.href = mailto;
  setNote(
    "Opening your email app to send the inquiry. If nothing happens, email us at " +
      CONTACT_EMAIL + ".",
    "success"
  );
});
