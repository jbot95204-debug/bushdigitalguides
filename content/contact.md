---
title: "Contact Bush Digital Guides"
description: "Contact Bush Digital Guides by email about growth and operations systems for trade and service businesses across regional South Australia."
keywords: ["contact Bush Digital Guides", "email enquiry trade business", "regional SA business systems"]
layout: content-page
---

<section class="bdg-section bdg-section-tight">
  <div class="container bdg-form-grid">
    <div>
      <div class="section-label">Contact</div>
      <h1>Email is the normal way to start.</h1>
      <p>Send a short enquiry and describe where work is getting stuck. You do not need to know which technology or service you need—email is the preferred first step, and we will help identify the sensible next step.</p>
      <div class="bdg-review-points">
        <div><strong>Preferred path</strong><span>Most suitable businesses start with a short email enquiry.</span></div>
        <div><strong>How this form works</strong><span>There is no hidden database or third-party form endpoint on this page. When you press the button, your own email app opens with a draft to <a href="mailto:hello@bushdigitalguides.com.au">hello@bushdigitalguides.com.au</a>. Review it, then send if you are happy with the content.</span></div>
        <div><strong>Safe enquiries</strong><span>Please do not send passwords, card details, bank details, login links, private customer lists, or urgent legal/compliance matters.</span></div>
      </div>
    </div>
    <div class="bdg-form-card" id="enquiry-form">
      <h2>Send an enquiry</h2>
      <p>Fill in the basics. When you press the button, your email app opens with the message ready to review.</p>
      <form class="bdg-safe-contact-form" id="bdg-contact-form" novalidate>
        <input type="text" name="company_website" class="bdg-hidden-field" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="form-group">
          <label for="business-name">Business name</label>
          <input id="business-name" name="business" type="text" autocomplete="organization" required>
        </div>
        <div class="form-group">
          <label for="contact-name">Your name</label>
          <input id="contact-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="form-group">
          <label for="contact-email">Email</label>
          <input id="contact-email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="form-group">
          <label for="business-link">Website or Google Profile link</label>
          <input id="business-link" name="link" type="url" inputmode="url" placeholder="https://">
        </div>
        <div class="form-group">
          <label for="help-needed">What is getting stuck?</label>
          <select id="help-needed" name="help" required>
            <option value="">Choose one</option>
            <option>Missed enquiries or slow response</option>
            <option>Website or brand first impression</option>
            <option>Quote or lead follow-up</option>
            <option>Disconnected tools and handovers</option>
            <option>Too much owner-led admin coordination</option>
            <option>Not sure yet — want to talk it through</option>
          </select>
        </div>
        <div class="form-group">
          <label for="message">Short note</label>
          <textarea id="message" name="message" rows="4" placeholder="Example: We are a trade business with regular enquiries and follow-up is still sitting with the owner."></textarea>
        </div>
        <p class="bdg-safe-form-warning">Do not include passwords, card or bank details, login links, private customer lists, or urgent legal/compliance matters.</p>
        <button type="submit" class="btn btn-primary">Open email to send enquiry →</button>
        <p class="bdg-form-status" id="bdg-form-status" aria-live="polite"></p>
      </form>
      <div class="bdg-stacked-actions">
        <a href="mailto:hello@bushdigitalguides.com.au?subject=Bush%20Digital%20Guides%20enquiry&body=Business%20name:%0AYour%20name:%0AEmail:%0AWebsite%20or%20Google%20Profile:%0AWhat%20is%20getting%20stuck:%0A%0APlease%20do%20not%20include%20passwords%2C%20card%20or%20bank%20details%2C%20login%20links%2C%20private%20customer%20lists%2C%20or%20urgent%20legal%2Fcompliance%20matters%20in%20this%20email.%0A" class="btn btn-outline">Email hello@ directly</a>
      </div>
      <p class="bdg-form-note">Spam-resistant by design: no public upload, no hidden database, a bot honeypot field, and a short time check before the email draft opens. Your enquiry is only sent after you press send in your email app.</p>
    </div>
  </div>
</section>

<section class="bdg-section bdg-muted-section">
  <div class="container">
    <div class="bdg-section-heading">
      <div class="section-label">What happens next</div>
      <h2>A clear reply, not an automated sales funnel.</h2>
    </div>
    <div class="bdg-process-line three">
      <div><span>01</span><h3>We read the enquiry</h3><p>We check the public link and your notes before replying, so the first response is useful.</p></div>
      <div><span>02</span><h3>We confirm the next step</h3><p>We determine whether a practical recommendation, a scoped project or another provider is the best next step.</p></div>
      <div><span>03</span><h3>You approve any work</h3><p>No work begins until the scope, investment and responsibilities are agreed.</p></div>
    </div>
  </div>
</section>

<script>
(function(){
  var form = document.getElementById('bdg-contact-form');
  var status = document.getElementById('bdg-form-status');
  if (!form || !status) return;
  var started = Date.now();

  form.addEventListener('submit', function(event){
    event.preventDefault();
    status.textContent = '';
    var data = new FormData(form);
    if ((data.get('company_website') || '').trim()) {
      status.textContent = 'Thanks. Please email hello@bushdigitalguides.com.au directly if the form does not open.';
      return;
    }
    if (Date.now() - started < 2500) {
      status.textContent = 'Please check the details, then press send again.';
      started = Date.now() - 2500;
      return;
    }
    var required = ['business','name','email','help'];
    for (var i = 0; i < required.length; i++) {
      if (!String(data.get(required[i]) || '').trim()) {
        status.textContent = 'Please fill in the required fields first.';
        return;
      }
    }
    var subject = 'Bush Digital Guides enquiry — ' + String(data.get('business') || '').trim();
    var body = [
      'Business name: ' + String(data.get('business') || '').trim(),
      'Your name: ' + String(data.get('name') || '').trim(),
      'Email: ' + String(data.get('email') || '').trim(),
      'Website or Google Profile: ' + String(data.get('link') || '').trim(),
      'What is getting stuck: ' + String(data.get('help') || '').trim(),

      '',
      'Short note:',
      String(data.get('message') || '').trim(),
      '',
      'Safety reminder: I have not included passwords, card or bank details, login links, private customer lists, or urgent legal/compliance matters.'
    ].join('\n');
    window.location.href = 'mailto:hello@bushdigitalguides.com.au?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    status.textContent = 'Your email app should open now. Review the message, then press send.';
  });
})();
</script>
