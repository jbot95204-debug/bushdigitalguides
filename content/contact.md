---
title: "Tell Us What You Want to Improve"
description: "Email Bush Digital Guides about brand, digital growth and practical business systems."
keywords: ["contact Bush Digital Guides", "email enquiry", "brand digital growth business systems"]
images: ["/images/bdg-growth-systems-hero.jpg"]
layout: content-page
---

<section class="bdg-section bdg-section-tight">
  <div class="container bdg-form-grid">
    <div>
      <div class="section-label">Contact</div>
      <h1>Tell Us What You Want to Improve</h1>
      <p>Send a short enquiry about the area you would like to improve. You do not need to know which service or system you need—email is the preferred first step.</p>
      <div class="bdg-review-points">
        <div><strong>Preferred path</strong><span>Most suitable businesses start with a short email enquiry.</span></div>
        <div><strong>How this form works</strong><span>When you press the button, your email app opens with a draft to <a href="mailto:hello@bushdigitalguides.com.au">hello@bushdigitalguides.com.au</a>. Review it, then send if you are happy with the content.</span></div>
        <div><strong>Safe enquiries</strong><span>Please do not send passwords, card details, bank details, login links, private customer lists, or urgent legal/compliance matters.</span></div>
      </div>
    </div>
    <div class="bdg-form-card" id="enquiry-form">
      <h2>Send an enquiry</h2>
      <p>Fill in the basics. When you press the button, your email app opens with the message ready to review.</p>
      <form class="bdg-safe-contact-form" id="bdg-contact-form">
        <div class="form-group">
          <label for="business-name">Business name <span>(required)</span></label>
          <input id="business-name" name="business" type="text" autocomplete="organization" required>
        </div>
        <div class="form-group">
          <label for="contact-name">Your name <span>(required)</span></label>
          <input id="contact-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="form-group">
          <label for="contact-email">Email <span>(required)</span></label>
          <input id="contact-email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="form-group">
          <label for="business-link">Website or Google Profile link <span>(optional)</span></label>
          <input id="business-link" name="link" type="url" inputmode="url" placeholder="https://">
        </div>
        <div class="form-group">
          <label for="help-needed">What would you like to improve <span>(required)</span></label>
          <select id="help-needed" name="help" required>
            <option value="">Choose one</option>
            <option>Brand or website</option>
            <option>Visibility</option>
            <option>Enquiry experience</option>
            <option>Follow-up or handover</option>
            <option>Repeated workflow</option>
            <option>Unsure</option>
          </select>
        </div>
        <div class="form-group">
          <label for="message">A short note <span>(optional)</span></label>
          <textarea id="message" name="message" rows="4" placeholder="Example: We would like our website and customer enquiries to feel clearer and more connected."></textarea>
        </div>
        <p class="bdg-safe-form-warning">Do not include passwords, card or bank details, login links, private customer lists, or urgent legal/compliance matters.</p>
        <button type="submit" class="btn btn-primary">Open email to send enquiry</button>
        <p class="bdg-form-status" id="bdg-form-status" aria-live="polite"></p>
      </form>
      <div class="bdg-stacked-actions">
        <a href="mailto:hello@bushdigitalguides.com.au?subject=Bush%20Digital%20Guides%20enquiry&body=Business%20name:%0AYour%20name:%0AEmail:%0AWebsite%20or%20Google%20Profile%20link:%0AWhat%20would%20you%20like%20to%20improve:%0A%0AA%20short%20note:%0A%0APlease%20do%20not%20include%20passwords%2C%20card%20or%20bank%20details%2C%20login%20links%2C%20private%20customer%20lists%2C%20or%20urgent%20legal%2Fcompliance%20matters%20in%20this%20email.%0A" class="btn btn-outline">Email hello@ directly</a>
      </div>
    </div>
  </div>
</section>

<section class="bdg-section bdg-muted-section">
  <div class="container">
    <div class="bdg-section-heading">
      <div class="section-label">What happens next</div>
      <h2>A considered next step, not an automated sales funnel.</h2>
    </div>
    <div class="bdg-process-line three">
      <div><span>01</span><h3>You review before sending</h3><p>Your email app gives you a final chance to check the message before you send it.</p></div>
      <div><span>02</span><h3>We consider the context</h3><p>Your notes and any public link help us understand the area you would like to improve.</p></div>
      <div><span>03</span><h3>You approve any work</h3><p>No work begins until the scope, investment and responsibilities are agreed.</p></div>
    </div>
  </div>
</section>

<script>
(function(){
  var form = document.getElementById('bdg-contact-form');
  var status = document.getElementById('bdg-form-status');
  if (!form || !status) return;

  form.addEventListener('submit', function(event){
    event.preventDefault();
    status.textContent = '';
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    var data = new FormData(form);
    var subject = 'Bush Digital Guides enquiry — ' + String(data.get('business') || '').trim();
    var body = [
      'Business name: ' + String(data.get('business') || '').trim(),
      'Your name: ' + String(data.get('name') || '').trim(),
      'Email: ' + String(data.get('email') || '').trim(),
      'Website or Google Profile link: ' + String(data.get('link') || '').trim(),
      'What would you like to improve: ' + String(data.get('help') || '').trim(),

      '',
      'A short note:',
      String(data.get('message') || '').trim(),
      '',
      'Safety reminder: I have not included passwords, card or bank details, login links, private customer lists, or urgent legal/compliance matters.'
    ].join('\n');
    window.location.href = 'mailto:hello@bushdigitalguides.com.au?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    status.textContent = 'Your email app should open now. Review the message, then press send.';
  });
})();
</script>
