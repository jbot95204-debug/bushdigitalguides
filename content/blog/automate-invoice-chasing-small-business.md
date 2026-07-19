---
title: "How to Automate Invoice Chasing for Small Businesses in Australia"
date: 2026-02-11
description: "A practical guide to invoice follow-up systems for Australian small businesses, tradies, and regional service businesses using Xero, MYOB, reminders, and simple workflows."
tags: ["invoice follow-up", "business automation", "tradie admin", "cash flow", "Xero", "MYOB", "regional business"]
categories: ["Digital Systems", "Business Automation"]
book: "Automate Everything"
bookLink: "/books/automate-everything/"
draft: false
---

Let's be real for a second. Repeatedly checking overdue invoices and writing follow-up messages can be an awkward part of running a business. Late payments can also make cash-flow planning and supplier commitments harder.

You can support invoice chasing with scheduled reminders and review tasks. This guide walks through the practical setup — from built-in tools in Xero and MYOB through to workflows using Zapier and Make.

## Why Late Payments Need a Clear Process

Before we get into the how, let's talk about why this matters beyond the obvious "I want my money."

### Cash Flow Is Everything

When customers pay late, the timing mismatch can affect supplier payments, purchasing decisions, and the ability to plan upcoming work. A documented process identifies overdue states, reminder stages, exceptions, and the point where a person must step in.

### The Hidden Time Cost

Here's the one nobody talks about. Every time you:

- Open your accounting software to check who hasn't paid
- Draft a polite-but-firm reminder email
- Make a follow-up phone call
- Send a second reminder
- Have the awkward conversation

...that adds repeated admin to the week. Measure the follow-up work in your own business rather than relying on a general estimate; invoice volume, payment terms, customer mix, and existing systems all affect it.

### The Emotional Tax

Chasing money can also be uncomfortable. Automation can send configured routine reminders, while disputes, hardship, payment plans, and escalation should still be handled by a person.

## Level 1: Built-In Invoice Reminders (Xero & MYOB)

If you're already using Xero or MYOB, review the reminder features available on your current plan and confirm how they are configured before enabling them.

### Xero Invoice Reminders

Xero's built-in reminder system is decent for basic chasing. Here's how to set it up:

1. Go to **Settings → Invoice Reminders**
2. You get three reminder stages — configure each one:
   - **Reminder 1:** 7 days after due date
   - **Reminder 2:** 14 days after due date
   - **Reminder 3:** 21 days after due date
3. Customise the email template for each stage (more on tone below)
4. Toggle on for each contact or set as default for all

**What Xero does well:**
- Automatic sending — once configured, it just runs
- Personalised with invoice details
- Includes a payment link (if you're using Xero payments)
- Shows reminder history on each invoice

**What Xero doesn't do:**
- No SMS reminders (email only)
- Can't trigger actions in other systems
- Limited to three reminder stages
- No built-in legal escalation workflow; formal collection documents should be reviewed carefully before use

### MYOB Invoice Reminders

MYOB's approach is similar but slightly different in execution:

1. Navigate to **Sales → Invoices**
2. Select overdue invoices (you can filter by days overdue)
3. Use the **Send Reminders** function
4. Customise your reminder template

MYOB's reminder system is more manual than Xero's — you need to trigger the batch send rather than having it run automatically. For fully automated reminders in MYOB, you'll want to pair it with a workflow tool (covered in Level 2).

### Crafting Clear Reminder Emails

Review the default templates in Xero and MYOB before enabling them. Here is a three-stage framework:

**Reminder 1 (7 days overdue) — The Friendly Nudge:**
> Hi [Name], just a quick heads-up that invoice #[Number] for $[Amount] was due on [Date]. Might have slipped through — no stress. You can pay directly via the link below. Cheers, [Your name]

**Reminder 2 (14 days overdue) — The Firmer Follow-Up:**
> Hi [Name], following up on invoice #[Number] for $[Amount], now 14 days past due. Could you let me know when I can expect payment? Happy to chat if there's an issue. Payment link below.

**Reminder 3 (21+ days overdue) — The Business Tone:**
> Hi [Name], invoice #[Number] for $[Amount] is now [X] days overdue. I need to resolve this to keep my accounts in order. Please arrange payment within 7 days or get in touch to discuss a payment plan. If I don't hear back, the account may move to our formal collection process.

Notice the escalation? Each reminder gets progressively more direct. The first assumes it's a mistake. The second asks for communication. The third makes it clear there are consequences. All professional, none aggressive.

## Level 2: Zapier and Make Workflows

Zapier and Make (formerly Integromat) can connect accounting software to other tools such as SMS providers, internal notifications, CRM systems, and draft-assistance tools.

### The Basic Overdue Invoice Workflow

**Trigger:** Invoice becomes overdue in Xero/MYOB
**Actions:**
1. Send automated email reminder (Day 1)
2. Wait 7 days → Send SMS reminder (Day 7)
3. Wait 7 more days → Send second email with firmer tone (Day 14)
4. Wait 7 more days → Create task for personal phone call (Day 21)
5. Day 30+ → Create a draft escalation task for owner review


{{< book-cta book="Automate Everything" >}}
### Setting Up a Zapier Workflow (Xero Example)

Here's a practical walkthrough for a basic Zapier automation:

**Step 1: Create a new Zap**
- Trigger app: **Xero**
- Trigger event: **New Invoice** (you'll filter for overdue status)

**Step 2: Add a Filter**
- Only continue if: Invoice Due Date is before today AND Invoice Status is "Authorised" (meaning unpaid)

**Step 3: Add a Delay**
- Wait 7 days after due date

**Step 4: Send Email via Gmail/Outlook**
- To: Contact email from Xero
- Subject: "Friendly reminder: Invoice #{{Invoice Number}} is overdue"
- Body: Your Reminder 1 template with dynamic fields

**Step 5: Add SMS Follow-Up (via Twilio or BurstSMS)**
- Wait additional 7 days
- Send SMS: "Hi {{Contact Name}}, invoice #{{Invoice Number}} for ${{Amount}} is 14 days overdue. Can you arrange payment? Pay here: {{Payment Link}}"

### Make (Integromat) Alternative

Make works similarly and supports branching logic. Compare current plans, operation limits, integrations, and support with the workflow you need.

The key advantage of Make over Zapier for invoice chasing is **branching logic**. You can build scenarios like:

- If invoice is under $500 → email reminder only
- If invoice is $500-$5,000 → email + SMS
- If invoice is over $5,000 → email + SMS + Slack notification to you + calendar block for phone call

That conditional logic assigns a communication channel and review task according to the invoice amount.

### SMS Follow-Ups: Additional Considerations

SMS can provide another reminder channel, but it is not automatically the right choice for every customer or invoice. Consider consent and legal requirements, sender identification, message costs, accessibility, customer preferences, and how replies will be monitored. Keep a human review step for disputes, hardship, or escalation.

**Australian SMS providers worth looking at:**
- **BurstSMS** — Australian provider with API options
- **Twilio** — global platform, more technical but very flexible
- **MessageMedia** — another solid Australian option

**Important:** payment reminders are usually treated differently from marketing messages, but the details matter. Keep reminders factual, identify the business clearly, avoid adding promotions, and get legal advice if you are unsure about consent, wording, or escalation rules.

## Level 3: Payment-Term Configuration

Payment terms and reminder rules should refer to the same due dates, exceptions, and escalation process.

### Early-Payment Terms

An early-payment term is one option a business can assess with its accountant. A clearly documented term should specify the amount, qualifying payment date, tax treatment, and what happens after that date. Model the cost before offering it and confirm the terms are appropriate for your business.

Use wording approved for the business rather than copying shorthand that customers may not understand.

### Progress Payments

For larger jobs (common in trades, consulting, and project work), don't wait until the end to invoice. Structure payments as:

- Agreed deposit before work starts
- Progress payments at milestones
- Agreed balance on completion

This structure allocates payment across the job rather than leaving the full invoice until completion. Deposits and progress claims must suit the contract, industry rules, tax treatment, and work actually completed.

### Late Payment Penalties

You may be able to charge interest on overdue invoices if your terms are clear, agreed upfront, and lawful. Include clear terms on your invoices:

> "Payment is due within the period stated on this invoice. Agreed overdue-account terms may apply after that date. Contact us promptly if you dispute the invoice or need to discuss the account."

Only include a late-payment term if it is lawful, agreed, and something the business is prepared to administer consistently. Get professional advice on the wording and enforcement.

### Get Paid Before You Start

For new customers, a business may consider payment upfront or a deposit where the contract and applicable rules allow it. Document the amount, due date, refund terms, payment methods, and accounting treatment.

## The Automation Stack: Putting It All Together

Here is an example of a staged accounts-receivable workflow. Treat the timing and channels as configuration examples, not a recommended result; adapt them to the business's terms, customer needs, and review requirements.

### Day 0: Invoice Sent
- Xero/MYOB generates and sends invoice with payment link
- Automation creates a "watch" for this invoice in your workflow

### Day of Due Date: Gentle Pre-Reminder
- Automated email: "Just a heads-up — invoice #123 is due today. Pay here: [link]"
- Use only if it fits the agreed payment terms and communication approach

### Day 7 Overdue: First Reminder
- Automated email with friendly tone
- Invoice details and payment link included

### Day 14 Overdue: SMS + Email
- SMS to customer's mobile
- Follow-up email with firmer tone
- Slack/Teams notification to you: "Invoice #123 is 14 days overdue — $X,XXX"

### Day 21 Overdue: Personal Touch Required
- Automated task created in your task manager
- Calendar block for a phone call
- Email with formal tone sent automatically

### Day 30+ Overdue: Escalation
- Draft escalation task created for owner review
- Account flagged in Xero/MYOB
- Future work for this customer requires upfront payment

### Later Overdue Stage: Formal Collection Review
- Handoff to debt collection agency or small claims process
- All communication history documented automatically

In a configured workflow, routine stages can run automatically and create a task when personal review is required. Monitor delivery failures and replies throughout; automation does not remove responsibility for the account or customer relationship.

## Common Concerns to Consider

**"My customers will think it's impersonal."**
Clear wording, accurate invoice details, an identifiable sender, and an easy way to raise a dispute can make an automated reminder easier to understand. Test the message and tone with the customer relationship in mind.

**"I don't want to upset good customers."**
Set rules so reminders are suppressed for disputed invoices, agreed extensions, hardship arrangements, or payments that have not yet reconciled. Provide a monitored reply path.

**"It's too complicated to set up."**
Start with the built-in reminder settings and review recipients, timing, templates, payment status, exceptions, and reply handling before switching them on.

**"I don't have enough invoices to justify automation."**
Use your own invoice volume and follow-up history to decide whether automation is worthwhile. A simple built-in reminder may be enough at a small scale.

## Initial Configuration Checklist

For an initial review, use these three items:

1. **Review Xero/MYOB invoice reminder settings.** Check the recipients, timing, templates, payment status, and exceptions before enabling them.
2. **Add a payment link to every invoice.** Xero and MYOB both support online payments. Make it stupidly easy to pay you.
3. **Update your payment terms.** Put them on your invoices, your quotes, and your website. Clear terms set clear expectations.

## Make the system safe before it runs

Invoice reminders touch customer relationships and money. Before turning on any automated follow-up, check:

- the customer data source is accurate and only the right team members can access it
- reminders are sent from a verified business email or SMS sender
- templates are polite, factual, and free from promotions or pressure
- payment links go to the correct account or payment provider
- sensitive disputes, complaints, payment plans, and hardship cases are handed to a person
- escalation steps create draft tasks for owner review rather than sending harsh messages automatically

This is the same practical digital safety principle BDG uses for websites and enquiry systems: define routine follow-up steps, but keep sensitive decisions approval-gated.

## Going Further

This guide covers the practical basics of automating invoice chasing. If you want to go deeper — building multi-step workflows, integrating with CRM systems, or connecting quotes through to payment follow-up — [*Automate Everything*](/books/automate-everything/) walks through broader setup options for Australian small businesses.

If invoices are only one part of a bigger enquiry and follow-up leak, start with a [Free Local Growth Review](/free-review/). Bush Digital Guides can check the path from website enquiry to quote, reminder, review request, and owner handoff, then suggest a simple system you can approve before anything goes live.

Set up the system carefully, define the routine reminders, and route disputes, hardship, replies, and escalation to a named person.
