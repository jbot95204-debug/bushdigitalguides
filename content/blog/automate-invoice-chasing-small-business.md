---
title: "How to Automate Invoice Chasing for Your Small Business in Australia"
date: 2026-02-11
description: "Stop manually chasing invoices. Set up automated payment reminders in Xero, MYOB, Zapier & Make for your Australian small business."
tags: ["invoice automation", "small business Australia", "Xero", "MYOB", "accounts receivable", "Zapier"]
categories: ["Business Automation"]
book: "Automate Everything"
bookLink: "/books/automate-everything/"
draft: false
---

Let's be real for a second. You didn't start a business to spend your evenings sending awkward "just following up on that invoice" emails. Nobody did. Yet here we are — the Australian Small Business and Family Enterprise Ombudsman reports that late payments cost Australian small businesses over **$115 billion** in outstanding invoices at any given time. The average payment time for small business invoices in Australia sits around **30-35 days** beyond the due date.

That's not a rounding error. That's your cash flow getting absolutely smashed because you're too busy actually doing the work to chase people who owe you money.

The good news? You can **automate invoice chasing** for your small business, and it's not as complicated as you think. This guide walks you through the practical setup — from built-in tools in Xero and MYOB through to more powerful workflows using Zapier and Make.

## The Real Cost of Late Payments

Before we get into the how, let's talk about why this matters beyond the obvious "I want my money."

### Cash Flow Is Everything

A 2024 report from CreditorWatch found that **more than 50% of Australian small businesses** experience cash flow issues directly related to late payments. When your customers pay late, you can't pay your suppliers on time, which damages your trade references, increases your costs (late payment penalties flow both ways), and limits your ability to take on new work.

### The Hidden Time Cost

Here's the one nobody talks about. Every time you:

- Open your accounting software to check who hasn't paid
- Draft a polite-but-firm reminder email
- Make a follow-up phone call
- Send a second reminder
- Have the awkward conversation

...that's time you're not spending on billable work or growing your business. Most tradies and small business owners I talk to reckon they spend **2-5 hours per week** on payment follow-ups. At even $80/hour, that's $8,000-$20,000 a year in lost productive time.

### The Emotional Tax

And let's not pretend there isn't an emotional cost. Chasing money is uncomfortable. Plenty of business owners let invoices slide simply because they don't want the confrontation. Automation removes the emotion entirely — it's just a system doing its job.

## Level 1: Built-In Invoice Reminders (Xero & MYOB)

If you're already using Xero or MYOB (and most Australian small businesses use one or the other), you've got automated reminders built in. Most people just haven't turned them on.

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
- No escalation beyond email (can't auto-generate a formal letter of demand)

### MYOB Invoice Reminders

MYOB's approach is similar but slightly different in execution:

1. Navigate to **Sales → Invoices**
2. Select overdue invoices (you can filter by days overdue)
3. Use the **Send Reminders** function
4. Customise your reminder template

MYOB's reminder system is more manual than Xero's — you need to trigger the batch send rather than having it run automatically. For fully automated reminders in MYOB, you'll want to pair it with a workflow tool (covered in Level 2).

### Crafting Reminder Emails That Actually Work

The default templates in both Xero and MYOB are... fine. But you can do better. Here's a framework:

**Reminder 1 (7 days overdue) — The Friendly Nudge:**
> Hi [Name], just a quick heads-up that invoice #[Number] for $[Amount] was due on [Date]. Might have slipped through — no stress. You can pay directly via the link below. Cheers, [Your name]

**Reminder 2 (14 days overdue) — The Firmer Follow-Up:**
> Hi [Name], following up on invoice #[Number] for $[Amount], now 14 days past due. Could you let me know when I can expect payment? Happy to chat if there's an issue. Payment link below.

**Reminder 3 (21+ days overdue) — The Business Tone:**
> Hi [Name], invoice #[Number] for $[Amount] is now [X] days overdue. I need to resolve this to keep my accounts in order. Please arrange payment within 7 days or get in touch to discuss a payment plan. If I don't hear back, I'll need to consider my options for debt recovery.

Notice the escalation? Each reminder gets progressively more direct. The first assumes it's a mistake. The second asks for communication. The third makes it clear there are consequences. All professional, none aggressive.

## Level 2: Zapier and Make Workflows

This is where it gets properly powerful. Zapier and Make (formerly Integromat) let you build workflows that connect your accounting software to other tools — SMS, Slack, CRM systems, even AI-powered follow-ups.

### The Basic Overdue Invoice Workflow

**Trigger:** Invoice becomes overdue in Xero/MYOB
**Actions:**
1. Send automated email reminder (Day 1)
2. Wait 7 days → Send SMS reminder (Day 7)
3. Wait 7 more days → Send second email with firmer tone (Day 14)
4. Wait 7 more days → Create task for personal phone call (Day 21)
5. Day 30+ → Generate formal letter of demand from template

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

**Estimated cost:** Zapier Starter plan ($29.99 USD/month) + BurstSMS credits (roughly $0.08-0.09 per SMS)

### Make (Integromat) Alternative

Make works similarly but offers more complex logic at a lower price point. If you're sending fewer than 1,000 operations per month, Make's free plan might cover you.

The key advantage of Make over Zapier for invoice chasing is **branching logic**. You can build scenarios like:

- If invoice is under $500 → email reminder only
- If invoice is $500-$5,000 → email + SMS
- If invoice is over $5,000 → email + SMS + Slack notification to you + calendar block for phone call

That kind of conditional logic helps you focus your personal attention on the invoices that actually matter.

### SMS Follow-Ups: The Secret Weapon

Email reminders are good. SMS follow-ups are better. Here's why:

- **SMS open rates in Australia sit around 95%** (compared to ~20-30% for email)
- People read texts within minutes, not hours
- A text feels more personal and harder to ignore
- Payment links in SMS get clicked at a much higher rate than email links

**Australian SMS providers worth looking at:**
- **BurstSMS** — Australian-owned, great API, competitive pricing (~8-9c per SMS)
- **Twilio** — global platform, more technical but very flexible
- **MessageMedia** — another solid Australian option

**Important:** Under Australian law (Spam Act 2003), you can send transactional messages (including payment reminders) to customers without explicit marketing consent, as long as you have an existing business relationship. Invoice reminders fall squarely into the transactional category.

## Level 3: Payment Terms That Prevent Late Payments

Automation handles the chasing, but smart payment terms reduce the need for chasing in the first place.

### Early Payment Discounts

Offer a 2% discount for payment within 7 days. Sounds small, but it works. A $5,000 invoice with a 2% early payment discount means your customer saves $100. Many will take it, especially larger businesses with accounts departments looking to optimise.

Format it on your invoices as: **2/7 Net 30** (2% discount if paid within 7 days, otherwise full amount due in 30 days)

### Progress Payments

For larger jobs (common in trades, consulting, and project work), don't wait until the end to invoice. Structure payments as:

- 30-50% deposit upfront
- Progress payments at milestones
- 10-20% on completion

This dramatically reduces your exposure. If someone doesn't pay the final 10%, you've already collected 80-90% of the job value.

### Late Payment Penalties

You absolutely can charge interest on overdue invoices in Australia. Include clear terms on your invoices:

> "Payment due within 14 days. Accounts overdue beyond 30 days may incur interest at 2% per month on the outstanding balance."

Will you actually enforce it every time? Probably not. But having it there creates urgency and gives you leverage in conversations.

### Get Paid Before You Start

For new customers without an established relationship, there's nothing wrong with requiring payment upfront or a substantial deposit. Payment platforms like Square, Stripe, and even direct bank transfer make this friction-free.

## The Automation Stack: Putting It All Together

Here's what a fully automated accounts receivable system looks like for a typical Australian small business:

### Day 0: Invoice Sent
- Xero/MYOB generates and sends invoice with payment link
- Automation creates a "watch" for this invoice in your workflow

### Day of Due Date: Gentle Pre-Reminder
- Automated email: "Just a heads-up — invoice #123 is due today. Pay here: [link]"
- (Many businesses skip this, but it works surprisingly well)

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
- Formal letter of demand auto-generated from template
- Account flagged in Xero/MYOB
- Future work for this customer requires upfront payment

### Day 60+ Overdue: Debt Recovery
- Handoff to debt collection agency or small claims process
- All communication history documented automatically

The beauty of this system is that **you don't think about it until Day 21.** The first three weeks handle themselves. You only get personally involved when it's genuinely needed.

## Common Objections (And Why They're Wrong)

**"My customers will think it's impersonal."**
Your customers get automated reminders from their phone company, electricity provider, and Netflix. Nobody thinks less of those companies. Professional reminders signal that you run a professional business.

**"I don't want to upset good customers."**
Good customers pay on time and won't receive reminders. And the ones who occasionally forget? They'll appreciate the nudge rather than an awkward phone call three weeks later.

**"It's too complicated to set up."**
Xero's built-in reminders take about 15 minutes to configure. That's it. You can get fancier later, but start with the basics.

**"I don't have enough invoices to justify automation."**
If you send even 10 invoices a month and 3-4 go overdue, that's potentially hours of chasing per month. The maths works at almost any scale.

## Quick Wins: Start Today

If you do nothing else after reading this, do these three things:

1. **Turn on Xero/MYOB invoice reminders right now.** Fifteen minutes. Default templates. Just switch them on.
2. **Add a payment link to every invoice.** Xero and MYOB both support online payments. Make it stupidly easy to pay you.
3. **Update your payment terms.** Put them on your invoices, your quotes, and your website. Clear terms set clear expectations.

## Going Further

This guide covers the practical basics of automating your invoice chasing. If you want to go deeper — building multi-step workflows, integrating with CRM systems, automating your entire admin stack from quotes through to debt recovery — [*Automate Everything*](/books/automate-everything/) walks through the complete setup for Australian small businesses. It's written for real business owners, not tech bros, and covers Xero, MYOB, Zapier, Make, and a dozen other tools you probably didn't know you needed.

Stop chasing invoices manually. Set up the system, let it run, and spend your time on the work that actually makes you money.
