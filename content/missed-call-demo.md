---
title: "Missed Call Demo"
description: "A plain-English demo flow showing how a human-first missed-call assistant can answer safely, collect useful details, and hand the enquiry back to the business owner."
keywords: ["missed call demo", "AI receptionist demo", "call forwarding assistant", "local business phone assistant"]
---

This is the demo flow Bush Digital Guides uses to show the **safe version** of a missed-call assistant.

The point is not to replace the owner. The point is to catch useful details when a real customer calls and nobody can answer.

<div class="post-growth-cta">
  <p><strong>Demo status</strong></p>
  <p>This page is an illustrative demo flow, not a live public phone service or an invitation to place a call. Any client test number is created only as part of an approved implementation, after the script, privacy wording, routing, lead destination, and safety controls are agreed.</p>
  <div class="post-growth-cta-actions">
    <a href="/free-review/" class="btn btn-primary btn-sm">Start with a Free Review →</a>
    <a href="/missed-call-safety-net/" class="btn btn-outline btn-sm">View the Service</a>
  </div>
</div>

## The promise

**Your normal phone rings first. If you miss the call, the enquiry still gets captured.**

The assistant only does the safe first job:

- apologises that the call was missed
- takes a message
- asks one question at a time
- collects the details the owner actually needs
- sends a structured summary
- hands anything sensitive, urgent, pricing-related, or unusual to a person

## Sample call script

**Assistant:**

> Hi, you’ve reached the business assistant. Sorry we missed your call. I can take a few details so someone can call you back properly. What is your name?

**Caller:**

> Sarah.

**Assistant:**

> Thanks Sarah. What suburb or town is the job in?

**Caller:**

> Goolwa.

**Assistant:**

> And what do you need help with?

**Caller:**

> I need the gutters cleaned. They’re overflowing near the carport.

**Assistant:**

> Thanks. Is it urgent, or is a normal callback okay?

**Caller:**

> Normal callback is fine, ideally today.

**Assistant:**

> No worries. What is the best number and time for a callback?

**Caller:**

> 04xx xxx xxx, after 3pm.

**Assistant:**

> Thanks Sarah. I’ll pass that through so someone can follow up. Please don’t send payment details, passwords, or urgent safety information here.

## What the owner receives

This is the practical value of the safety net: the owner gets enough context to call back properly, without the assistant making commitments for the business.

```text
New missed-call enquiry
Source: missed-call assistant
Name: Sarah
Phone: 04xx xxx xxx
Suburb: Goolwa
Service: Gutter cleaning
Issue: Gutters overflowing near carport
Urgency: Normal callback, today preferred
Best callback: After 3pm
Assistant action: Intake only
Price quoted: No
Booking confirmed: No
Sensitive details collected: No
Owner review required: Yes
Suggested next action: Call Sarah after 3pm, confirm job details, and decide whether the work is suitable.
```

Before a live setup, BDG checks that summaries include the right owner handoff fields and that any request about prices, bookings, complaints, logins, payments, or urgent issues is marked for human review.

## The more advanced version

Once the safe missed-call version is tested, the assistant can be connected to an approved business gateway for harder questions.

Simple questions stay inside the voice assistant. Complex questions use a natural hold line — “No worries, let me check that for you” — then check only approved knowledge or systems before giving a customer-safe answer. If it is unsure, private, or risky, it hands the issue to a person.

See the [Operations-Aware AI Voice Assistant](/operations-aware-ai-voice-assistant/) service for the version that can check approved business information without exposing private data.

## What makes this safer than a generic “AI receptionist”

- the business phone still rings first
- the assistant does not pretend to be a person
- pricing and bookings are off unless rules are approved
- sensitive information is discouraged
- urgent/safety issues are handed to a human
- the owner can disable the forwarding path
- early calls are reviewed before adding more autonomy

## Demo scenarios we test before launch

Before any public phone routing or customer-facing use, the pilot needs **11 internal platform calls** to pass, including scenario 9A for trade safety/property-risk handoff.

The minimum proof run covers:

- normal quote request
- vague enquiry
- caller asks for price
- caller asks for a firm booking
- outside service area
- angry or confused caller
- urgent or safety-sensitive issue
- customer tries to provide payment or password details
- incomplete contact details
- scenario 9A: trade safety/property-risk handoff, where the assistant avoids diagnosis or repair advice and sends the issue to a person
- repeat caller asking for follow-up

Those test calls need to show the same owner-summary guardrails every time: `Price quoted: No`, `Booking confirmed: No`, `Sensitive details collected: No`, and `Owner review required: Yes`.

## Want this checked for your business?

Start with a [Free Local Growth Review](/free-review/) and mention “missed calls” in the email. We will look at your website, Google Profile, phone path, enquiry capture, and follow-up process before recommending any paid setup.
