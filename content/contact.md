---
title: "Contact Bush Digital Guides"
description: "Contact Bush Digital Guides for practical local growth support for regional Australian small businesses."
keywords: ["contact Bush Digital Guides", "local growth support Australia", "regional business website help"]
layout: contact
---

<section class="bdg-section bdg-section-tight">
  <div class="container bdg-form-grid">
    <div>
      <div class="section-label">Contact</div>
      <h1>Tell us what you want fixed.</h1>
      <p>Use the short form or email directly. The form is deliberately simple and safe: it opens your own email app, so there is no hidden database, no public upload box, and no unverified form service collecting details.</p>
      <div class="bdg-review-points">
        <div><strong>Best first step</strong><span>Most businesses should start with the Free Local Growth Review.</span></div>
        <div><strong>Call option</strong><span>Call <a href="tel:+61899320067">(08) 9932 0067</a> or <a href="tel:+61899320067">+61 8 9932 0067</a>. If unavailable, calls may be answered by the BDG missed-call assistant. Please do not share passwords, card details, or bank details by phone.</span></div>
        <div><strong>What we help with</strong><span>Getting found, looking trustworthy, making contact easy, following up properly, and keeping basics safer.</span></div>
        <div><strong>Approval first</strong><span>No website changes, customer contact, Google updates, review requests, automation, or publishing happen without approval.</span></div>
        <div><strong>Safe enquiries</strong><span>Please do not send passwords, card details, bank details, login links, private customer lists, or urgent legal/compliance matters.</span></div>
      </div>
    </div>
    <div class="bdg-form-card">
      <h3>Quick enquiry form</h3>
      <p>Fill in the basics. When you press send, your email app opens with the message ready to review.</p>
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
          <label for="contact-phone">Phone <span>(optional)</span></label>
          <input id="contact-phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="form-group">
          <label for="business-link">Website or Google Profile link</label>
          <input id="business-link" name="link" type="url" inputmode="url" placeholder="https://">
        </div>
        <div class="form-group">
          <label for="help-needed">What do you want improved?</label>
          <select id="help-needed" name="help" required>
            <option value="">Choose one</option>
            <option>More local enquiries</option>
            <option>Clearer website / contact path</option>
            <option>Google profile / local visibility</option>
            <option>Reviews and trust signals</option>
            <option>Missed calls or follow-up</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <div class="form-group">
          <label for="message">Short note</label>
          <textarea id="message" name="message" rows="4" placeholder="Example: We are a local plumbing business around Victor Harbor and want more quote enquiries."></textarea>
        </div>
        <p class="bdg-safe-form-warning">Do not include passwords, card or bank details, login links, private customer lists, or urgent legal/compliance matters.</p>
        <button type="submit" class="btn btn-primary">Open email to send →</button>
        <p class="bdg-form-status" id="bdg-form-status" aria-live="polite"></p>
      </form>
      <div class="bdg-stacked-actions">
        <a href="tel:+61899320067" class="btn btn-outline">Call (08) 9932 0067</a>
        <a href="/free-review/" class="btn btn-outline">Get a Free Local Growth Review</a>
        <a href="mailto:hello@bushdigitalguides.com.au?subject=Bush%20Digital%20Guides%20enquiry&body=Business%20name:%0AWebsite%20or%20Google%20Profile:%0AMain%20service%20area:%0AWhat%20I%20want%20improved:%0ABest%20way%20to%20reply:%0A%0APlease%20do%20not%20include%20passwords%2C%20card%20or%20bank%20details%2C%20login%20links%2C%20private%20customer%20lists%2C%20or%20urgent%20legal%2Fcompliance%20matters%20in%20this%20email.%0A" class="btn btn-outline">Email hello@ directly</a>
      </div>
      <p class="bdg-form-note">Spam-resistant by design: no public upload, no hidden database, a bot honeypot field, and a short time check before the email draft opens.</p>
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
      <div><span>02</span><h3>We confirm the next step</h3><p>Most enquiries start with the Free Local Growth Review. If another step makes more sense, we explain why.</p></div>
      <div><span>03</span><h3>You approve any work</h3><p>Nothing is changed, sent, published, automated, or customer-contacted unless you approve it first.</p></div>
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
      'Phone: ' + String(data.get('phone') || '').trim(),
      'Website or Google Profile: ' + String(data.get('link') || '').trim(),
      'What I want improved: ' + String(data.get('help') || '').trim(),
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
