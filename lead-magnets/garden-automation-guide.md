# 🌿 Bush Digital Guides

---

# 5-Minute Garden Automation Setup Guide

**Smart irrigation for complete beginners — what to buy, where to buy it, and how to set it up**

---

*Extracted from "Set and Forget: The Aussie Guide to Automated Gardening." This guide gets you from hand-watering to smart-watering in one trip to Bunnings.*

---

## The Goal

Stop standing around with a hose every evening. Set up a system that waters your garden automatically, knows when it's going to rain, and lets you check on it from your phone.

**Total cost:** $110–$330 depending on how smart you want to go.
**Time to install:** 30 minutes to 2 hours.
**Skills needed:** Can you screw a fitting onto a tap? You're qualified.

---

## Option A: The Bunnings Quick Start (~$110)

**Best for:** Renters, small gardens, "just make it work" people.

### Shopping List — One Trip to Bunnings

| Item | Price |
|------|-------|
| Holman Electronic 2-Dial Tap Timer | $41.55 |
| Holman 13mm × 25m Black Poly Pipe | $14.58 |
| Holman 13mm Pressure Reducer & Filter Assembly | $16.62 |
| Pope 13mm Nut and Tail (tap connector) | $3.03 |
| Pope 13mm Barbed Tee — 10 Pack | $10.40 |
| K-Rain 4mm Adjustable Dripper — 10 Pack | $4.73 |
| K-Rain 13mm Barbed End Plug — 10 Pack | $4.50 |
| Pope 13mm Locking Clamp — 25 Pack | $7.09 |
| **TOTAL** | **~$110** |

### Setup Steps

1. **Screw the nut and tail onto your garden tap.** Hand-tight is fine.
2. **Attach the pressure reducer/filter.** This stops your drippers blowing off — Aussie mains pressure (300–500 kPa) will destroy drip fittings without it.
3. **Connect the tap timer** to the reducer outlet.
4. **Lay your poly pipe** along the garden bed edges. Tip: leave it in the sun for 20 minutes first — it'll soften and be much easier to work with.
5. **Add fittings:** Tees for branches, end plugs to cap each run. Push in firmly, secure with clamps.
6. **Punch holes and insert drippers** at each plant. Use a 4mm hole punch ($3) or a nail. Twist the dripper cap to adjust flow — more for tomatoes, less for herbs.
7. **Program the timer:** Early morning (5–6am), 15–20 minutes, every second day.
8. **Bury under mulch.** Aussie UV will make exposed poly pipe brittle within a year.

**Done.** Your garden waters itself.

---

## Option B: The Smart Garden (~$260–$330)

**Best for:** Suburban homes, people who want app control and rain-skipping.

This is where it gets clever. Your phone controls the watering, a sensor tells the system when the soil is actually dry, and it checks the weather forecast before deciding to water.

### Shopping List

| Item | Where | Price |
|------|-------|-------|
| Orbit B-Hyve 6-Station WiFi Controller | Bunnings | $259 |
| Holman 13mm Techline PC Drip Tube — 50m | Bunnings | $53.30 |
| Holman 13mm Pressure Reducer & Filter Assembly | Bunnings | $16.62 |
| Assorted 13mm fittings (tees, elbows, end plugs, clamps) | Bunnings | ~$30 |
| **TOTAL** | | **~$360** |

**Or for a simpler setup:**

| Item | Where | Price |
|------|-------|-------|
| Orbit B-Hyve XD Tap Timer | Bunnings | ~$100 |
| Drip irrigation kit + fittings | Bunnings | ~$60–80 |
| **TOTAL** | | **~$160–180** |

---

## Recommended Smart Controllers — Honest Comparison

### 🏆 Orbit B-Hyve — The One We Recommend for Most People

**Price:** $259 (6-station) or ~$100 (XD tap timer)
**Where:** Bunnings

- No subscription fees, ever
- Weather-based scheduling using your postcode
- Alexa and Google Home compatible ("Hey Google, water Zone 3")
- Clean app that doesn't need a PhD
- Returnable to Bunnings if it's rubbish

**The honest take:** The weather algorithm isn't as sophisticated as the Hydrawise, but for a home garden it's genuinely good enough. Some people disable the smart watering and just use it as a WiFi-controlled timer — and that's perfectly fine too.

### Hunter Hydrawise Pro-HC — The Professional's Pick

**Price:** $350–$750 (6/12/24 zones)
**Where:** SunshowerOnline, Smart Water, irrigation specialists (NOT Bunnings)

- Best weather intelligence of any consumer controller in Australia
- "Predictive Watering" — tells you *why* it did or didn't water each day
- Optional flow meter detects burst pipes and stuck valves
- Professional-grade hardware

**The honest take:** Cloud-dependent — loses smart features during internet outages. WiFi chip can be flaky if the controller is far from your router. Overkill for most suburban gardens, brilliant for larger properties.

### OpenSprinkler — The Tinkerer's Dream

**Price:** $250–$359
**Where:** opensprinkler.com.au (Australian reseller with local stock)

- Open source, runs locally — no cloud dependency
- Excellent Home Assistant integration
- Works perfectly without internet
- One reviewer ran theirs for 11 years before replacing

**The honest take:** Requires more technical skill. If "REST API" makes you break out in hives, look elsewhere. If you run Home Assistant, this is your controller.

### Quick Decision Guide

| You are... | Buy this |
|-----------|---------|
| "Just make it work" | Orbit B-Hyve ($259 at Bunnings) |
| Willing to pay for the best | Hunter Hydrawise Pro-HC ($500+) |
| A Home Assistant nerd | OpenSprinkler ($250–$359) |
| A renter / one tap only | Orbit B-Hyve XD tap timer (~$100) |
| On the tightest budget | $30 mechanical timer from Bunnings |

---

## Adding a Soil Moisture Sensor

A sensor stops your system watering when the ground is already wet. Over an Aussie summer, this can cut water use by 30–50%.

### Best Options

| Sensor | Price | Where | Works With |
|--------|-------|-------|-----------|
| Ecowitt WH51 | ~$30 | Amazon AU | Ecowitt gateway → Home Assistant |
| ThirdReality Zigbee Sensor | ~$30 | Amazon AU | Home Assistant (via Zigbee) |
| Holman Smart Moisture Sensor | $54 | Bunnings | Holman WX system only |

**Our pick for beginners:** The Holman sensor if you're using the Holman WX system (all Bunnings, one ecosystem). The Ecowitt WH51 if you want the best value and don't mind Amazon.

**Pro tip:** Don't buy the $4 sensors from AliExpress. They corrode in weeks. Don't buy the 3-in-1 soil testers from Bunnings either — they're about as accurate as a coin flip.

---

## Home Assistant Basics (For the Curious)

Home Assistant is a free, open-source home automation platform that runs on a small computer in your house. It connects your sensors, controllers, weather data, and valves into one intelligent system.

### Why Bother?

- **Local control** — works without internet
- **Combines everything** — BOM weather + soil sensors + irrigation controller + water restrictions
- **Automations like:** "Only water at sunrise if soil moisture is below 40% AND no rain is forecast today"

### What You Need to Get Started

| Item | Price | Notes |
|------|-------|-------|
| Raspberry Pi 4 (4GB) or old mini PC | $80–$120 | The brain |
| Home Assistant OS | Free | homeassistant.io |
| Zigbee coordinator (Sonoff ZBDongle-E) | $35 | For Zigbee sensors/valves |
| Ecowitt GW2000 gateway | $50–$80 | For Ecowitt sensors |

### Key Integrations for Garden Automation

- **Bureau of Meteorology** — Free weather data, rain forecasts, temperature
- **Irrigation Unlimited** (HACS) — Multi-zone scheduling with water restriction compliance. Built by an Aussie.
- **Smart Irrigation** (HACS) — Evapotranspiration-based "should I water today?" calculations
- **ESPHome** — Build your own sensors for ~$20 each

### The Honest Bit

Home Assistant has a learning curve that's less "curve" and more "cliff face with handholds." It'll take several weekends to set up properly. Things will break. But the community is enormous and genuinely helpful — and once it's running, it's the most powerful garden automation platform available.

**If this sounds like too much:** Just buy the B-Hyve from Bunnings. It'll do 90% of what you need with 10% of the effort. No shame in that.

---

## Water Restriction Compliance

Most Australian states have permanent or seasonal watering schedules. Smart controllers handle this automatically, but make sure you configure them:

| State | General Rules |
|-------|--------------|
| **SA** | Sprinklers before 10am or after 5pm, alternate days. Drip anytime. |
| **VIC** | Permanent water-saving rules. During restrictions: alternate days, 6–10am and 6–10pm. |
| **NSW** | Before 10am or after 4pm. |
| **QLD (SEQ)** | Odd/even house numbers on alternate days. |

**Key insight: Drip irrigation is generally exempt from most restriction levels.** Even when sprinklers are banned, drip usually remains permitted. Design your system around drip and you're restriction-proof.

---

## Your Weekend Action Plan

### Saturday Morning (1–2 hours)

1. Walk your garden. Decide what needs water and how often.
2. Drive to Bunnings. Buy the B-Hyve (or your chosen controller) + drip irrigation supplies.
3. Install the controller. Mount near a power outlet with WiFi signal.
4. Run your drip lines. Lay Techline PC tube along garden beds, connect with tees and elbows, cap with end plugs.
5. Download the app. Set up zones and schedules.

### Saturday Arvo (30 minutes)

6. Test every zone. Walk around checking for leaks and dry spots.
7. Set your schedule: 6am, 15–20 minutes per zone, every second day.
8. Enable weather-responsive mode in the app.

### Sunday (optional, for keen types)

9. Order an Ecowitt WH51 soil sensor from Amazon.
10. When it arrives, stick it in your most important bed at root depth (100–150mm).
11. Set a moisture threshold so the system skips watering when the soil's already wet.

**That's it.** Your garden now waters itself, checks the weather, and knows when the soil is dry. Go sit on the couch.

---

## Common Mistakes to Avoid

❌ **Skipping the pressure reducer** — Aussie mains pressure will blow drip fittings apart. Always use one.

❌ **Leaving poly pipe in direct sun** — UV destroys it within a season. Bury under mulch.

❌ **Forgetting the inline filter** — Sediment blocks drippers. Clean the filter screen every few months.

❌ **Overwatering** — More plants die from overwatering than underwatering. Start with less and increase if plants look stressed.

❌ **Dead batteries in tap timers** — Set a calendar reminder every 3–4 months. Dead batteries = dead garden (valve fails closed).

❌ **Buying the cheapest WiFi timer** — The $99 Holman WX1 has consistent reliability complaints. Spend the extra $160 on the B-Hyve and save yourself the headache.

---

## 📖 Get the Full Guide

This guide gets you started, but the full book covers everything — soil moisture sensors (which ones actually last), automated fertigation, Home Assistant deep-dives, greenhouse automation, rainwater tank integration, and three complete build guides from $100 to $1,000.

**[Read "Set and Forget: The Aussie Guide to Automated Gardening" →](/books/set-and-forget/)**

The complete guide to automating your garden — from a $30 tap timer to a fully sensor-driven smart irrigation system.

---

*© Bush Digital Guides — bushdigitalguides.com.au*
*Updated February 2026. Prices from Bunnings and Amazon AU — check current availability.*
