---
title: "Home Assistant Garden Automation: A Practical Getting-Started Guide"
date: 2026-02-11
description: "Set up Home Assistant garden automation with soil moisture sensors, automated irrigation, weather integration and ESPHome DIY sensors."
tags: ["Home Assistant", "garden automation", "smart irrigation", "ESPHome", "soil moisture sensor", "automated watering"]
categories: ["Gardening"]
book: "Set and Forget: The Aussie Guide to Automated Gardening"
bookLink: "/books/set-and-forget/"
draft: false
---

There's a certain kind of person who looks at their garden irrigation timer and thinks, "Yeah, but what if my garden could check the weather forecast, read the soil moisture, and decide for itself whether to water?" If that sounds like you, welcome to the rabbit hole. **Home Assistant garden automation** is where smart home tech meets practical horticulture, and once you start, you won't look at a dumb timer the same way again.

This guide walks you through the practical setup — from getting Home Assistant running, to building DIY soil moisture sensors with ESPHome, to creating automations that actually save water and grow better plants. It's written for people who want results, not people who want to tinker endlessly (though if you're the tinkering type, there's plenty here for you too).

## Why Home Assistant for Garden Automation?

You might be wondering why you need a whole home automation platform just to water plants. Fair question. Here's why Home Assistant beats dedicated smart irrigation controllers:

### It Connects Everything
Dedicated irrigation controllers (Hunter Hydrawise, Orbit B-Hyve, Rachio) do one thing — control zones on a schedule, maybe with a weather adjustment. Home Assistant connects your irrigation to **everything else**: soil moisture sensors, rain sensors, weather forecasts, temperature readings, tank water levels, even your home's energy system (water during off-peak solar hours, anyone?).

### It's Local
No cloud dependency. Your garden automations run on a little box in your house, not on some company's server that might go down, get hacked, or shut down their API when they pivot to a different business model. When Insteon died, their users lost everything. Your Home Assistant will still be watering your tomatoes.

### It's Free (Software-wise)
Home Assistant is open-source. Free forever. The hardware to run it costs $50-200 depending on what you use, but there are no subscriptions, no premium tiers, no "pay $5/month to unlock advanced scheduling."

### It's Ridiculously Flexible
Want to water Zone 3 only when soil moisture drops below 40%, it hasn't rained in the last 24 hours, the forecast shows no rain in the next 12 hours, and it's not currently above 38°C? That's about 10 lines of automation config. Try doing that with a $50 irrigation timer.

## Getting Started: What You Need

### The Home Assistant Hub

You need something to run Home Assistant on. Options from simplest to most flexible:

**Home Assistant Green (~$150 AUD)**
- Purpose-built hardware, plug-and-play
- Best for beginners who just want it to work
- Plenty powerful for garden automation

**Raspberry Pi 4/5 ($80-$130 AUD + SD card/SSD)**
- The classic DIY option
- Works great but SD cards can fail — use an SSD for reliability
- Massive community support

**Old PC or Intel NUC ($0-$200)**
- If you've got an old mini-PC lying around, install Home Assistant OS on it
- More powerful than you'll ever need for garden automation
- Good option if you plan to expand into full home automation

**Virtual Machine**
- If you already run a home server (Proxmox, Unraid, etc.), just spin up a VM
- Most flexible option for tech-savvy users

### Irrigation Control Hardware

You need a way for Home Assistant to actually turn water on and off. Several approaches:

**Smart Solenoid Valves (WiFi/Zigbee)**
- Replace your existing solenoid valves with smart ones
- Brands: Moes Zigbee valve, Shelly-controlled standard solenoids
- Direct Home Assistant integration

**Smart Relay Controlling Existing Solenoids**
- Keep your existing 24V AC solenoid valves
- Use a Shelly relay, Sonoff, or ESP32-based relay board to switch them
- Cheapest option if you already have solenoids installed (~$15-30 per zone)

**All-in-One Smart Irrigation Controllers**
- OpenSprinkler — open-source, excellent Home Assistant integration
- Runs its own firmware but plays nicely with HA
- ~$200 AUD for a unit that handles 8+ zones

**DIY ESP32 + Relay Board**
- Build your own multi-zone controller with an ESP32 and relay module
- Total cost: ~$20-40 for up to 8 zones
- Full ESPHome integration (covered below)
- Maximum flexibility, requires some soldering and basic electronics

### Soil Moisture Sensors

This is where garden automation gets genuinely smart. Instead of watering on a schedule, you water based on what the soil actually needs.

**Capacitive Soil Moisture Sensors + ESPHome (DIY)**
- Cost: ~$3-8 per sensor
- Requires an ESP32 board (~$10-15) to read and transmit data
- The most cost-effective option by far
- Detailed build guide below

**Xiaomi/Miflora Plant Sensors**
- ~$15-25 each
- Bluetooth — works with Home Assistant via ESPHome Bluetooth proxy or direct
- Measures moisture, temperature, light, and soil conductivity
- Decent for pot plants, less reliable for garden beds (short probe)

**Ecowitt Soil Moisture Sensors**
- ~$20-30 each
- 915MHz wireless — good range for garden setups
- Works with Ecowitt gateway → Home Assistant integration
- Reliable and weatherproof

## Building DIY Soil Moisture Sensors with ESPHome

ESPHome is a firmware framework for ESP32/ESP8266 microcontrollers that integrates natively with Home Assistant. If you're new to it — don't panic. It's way easier than it sounds.

### What You Need (Per Sensor Node)

- 1x ESP32 development board (~$10-15 from AliExpress or Core Electronics)
- 1-4x Capacitive soil moisture sensors (~$3-8 each)
- 1x Waterproof enclosure (~$5-10)
- USB power supply or 18650 battery + solar panel for wireless
- Dupont jumper wires

**Total cost per sensor node: $20-40** (can monitor 1-4 zones per node)

### ESPHome Configuration

Here's a basic ESPHome config for a soil moisture sensor:

```yaml
esphome:
  name: garden-moisture-01
  platform: ESP32
  board: esp32dev

wifi:
  ssid: "YourWiFiName"
  password: "YourWiFiPassword"

api:
  encryption:
    key: "your-generated-api-key"

ota:
  platform: esphome
  password: "your-ota-password"

sensor:
  - platform: adc
    pin: GPIO34
    name: "Veggie Bed Soil Moisture"
    update_interval: 300s
    unit_of_measurement: "%"
    attenuation: 11db
    filters:
      - calibrate_linear:
          - 2.85 -> 0.0    # Sensor in dry air
          - 1.28 -> 100.0  # Sensor in water
      - lambda: |-
          if (x < 0) return 0.0;
          if (x > 100) return 100.0;
          return x;
```

### Calibrating Your Sensors

The `calibrate_linear` values above are examples. You need to calibrate each sensor:

1. **Dry reading:** Hold the sensor in dry air and note the raw ADC value (shown in HA logs)
2. **Wet reading:** Submerge the sensor in a glass of water and note the value
3. **Update your config** with these two reference points

Capacitive sensors aren't laboratory instruments, but they're accurate enough to tell you "dry," "moist," or "wet" — which is all you need for irrigation decisions.

### Weatherproofing

Your ESP32 and connections need to survive outdoors. Here's what works:

- **Waterproof enclosure:** IP65 or better junction box from Bunnings ($8-15)
- **Cable glands:** For where wires enter the enclosure
- **Conformal coating:** Spray the ESP32 board with conformal coating for extra protection
- **Elevate the enclosure:** Mount it off the ground on a stake or fence post
- **Solar option:** A small 6V solar panel + TP4056 charge controller + 18650 battery can power a sensor node indefinitely

## Weather Integration

Home Assistant can pull weather data from multiple sources and use it in your garden automations:

### Bureau of Meteorology (BoM)
The `bom` integration gives you current conditions and forecasts from your nearest BoM weather station. This is Australian-specific data, which is far more useful than global weather services for local garden decisions.

Install via HACS (Home Assistant Community Store) — search for "Bureau of Meteorology."

### OpenWeatherMap
Free tier gives you current weather, 5-day forecast, and rain probability. Good supplement to BoM data.

### Personal Weather Stations
If you have an Ecowitt, Ambient Weather, or Davis weather station, integrate it directly. Local microclimate data from your actual property is always better than data from the nearest BoM station 20km away.

### Weather Data You Want for Garden Automation

- **Rain in last 24 hours** (don't water if it's already rained)
- **Rain forecast next 12-24 hours** (don't water if it's about to rain)
- **Current temperature** (don't water in extreme heat — water evaporates before it helps)
- **Wind speed** (sprinklers in high wind = wasted water)
- **Evapotranspiration (ET)** (advanced: adjusts watering volume based on how fast water is lost)

## Building Your Dashboard

A good garden automation dashboard gives you at-a-glance status without needing to dig through menus. Here's a practical layout:

### Section 1: Current Conditions
- Soil moisture for each zone (gauge cards — green/yellow/red)
- Last watering time and duration per zone
- Current weather conditions
- Rain forecast (next 24 hours)

### Section 2: Controls
- Manual override buttons for each irrigation zone
- Master enable/disable toggle for all automations
- "Water everything now" emergency button (for heatwave days)

### Section 3: History
- Soil moisture graphs over the past week (line chart)
- Watering history (when each zone ran and for how long)
- Rainfall history

### Example Dashboard Card (YAML)

```yaml
type: gauge
entity: sensor.veggie_bed_soil_moisture
name: Veggie Bed
min: 0
max: 100
severity:
  green: 40
  yellow: 25
  red: 0
```

## Example Automations

Here's where the magic happens. These are real automations you can adapt:

### Automation 1: Water When Dry (Basic)

```yaml
alias: "Water veggie bed when dry"
trigger:
  - platform: numeric_state
    entity_id: sensor.veggie_bed_soil_moisture
    below: 35
    for:
      minutes: 30
condition:
  - condition: time
    after: "06:00:00"
    before: "09:00:00"
  - condition: state
    entity_id: input_boolean.irrigation_enabled
    state: "on"
action:
  - service: switch.turn_on
    target:
      entity_id: switch.irrigation_zone_1
  - delay:
      minutes: 15
  - service: switch.turn_off
    target:
      entity_id: switch.irrigation_zone_1
```

This waters Zone 1 for 15 minutes when soil moisture drops below 35%, but only during the morning window and only if irrigation is globally enabled.

### Automation 2: Skip Watering if Rain Expected

```yaml
alias: "Cancel watering if rain forecast"
trigger:
  - platform: time
    at: "05:30:00"
condition:
  - condition: numeric_state
    entity_id: sensor.bom_rain_chance_today
    above: 70
  - condition: numeric_state
    entity_id: sensor.bom_rain_amount_forecast
    above: 5
action:
  - service: input_boolean.turn_off
    target:
      entity_id: input_boolean.irrigation_enabled
  - service: notify.mobile_app
    data:
      message: "Irrigation skipped — BoM forecasts >5mm rain today ({{ states('sensor.bom_rain_chance_today') }}% chance)"
```

At 5:30am each day, this checks the BoM forecast. If there's more than a 70% chance of at least 5mm of rain, it disables irrigation for the day and sends you a notification.

### Automation 3: Heatwave Protection

```yaml
alias: "Extra watering on extreme heat days"
trigger:
  - platform: numeric_state
    entity_id: sensor.outside_temperature
    above: 40
condition:
  - condition: time
    after: "05:00:00"
    before: "07:00:00"
action:
  - service: switch.turn_on
    target:
      entity_id: switch.irrigation_zone_all
  - delay:
      minutes: 20
  - service: switch.turn_off
    target:
      entity_id: switch.irrigation_zone_all
  - service: notify.mobile_app
    data:
      message: "🔥 Heatwave watering triggered — all zones for 20min ({{ states('sensor.outside_temperature') }}°C)"
```

When the temperature hits 40°C during early morning hours, hit everything with a good soak. Your plants will thank you.

### Automation 4: Tank Water Level Warning

If you're irrigating from a rainwater tank (common in Australian garden setups):

```yaml
alias: "Tank low water warning"
trigger:
  - platform: numeric_state
    entity_id: sensor.water_tank_level
    below: 20
action:
  - service: notify.mobile_app
    data:
      message: "⚠️ Water tank is at {{ states('sensor.water_tank_level') }}%. Consider switching to mains or reducing irrigation."
  - service: input_number.set_value
    target:
      entity_id: input_number.irrigation_duration_multiplier
    data:
      value: 0.5
```

When the tank drops below 20%, it alerts you and automatically halves all irrigation durations. Smart water management without lifting a finger.

## The Learning Curve: Being Honest

Let's not pretend this is plug-and-play. Home Assistant garden automation has a learning curve:

**Easy (Week 1):**
- Installing Home Assistant
- Adding a smart plug or relay to control a single irrigation zone
- Basic time-based automation ("water at 6am for 15 minutes")

**Medium (Week 2-4):**
- Setting up ESPHome sensors
- Calibrating soil moisture readings
- Weather integration
- Multi-zone scheduling with conditions

**Advanced (Month 2+):**
- Evapotranspiration-based watering calculations
- Solar-powered wireless sensor nodes
- Multi-garden-bed orchestration (water beds sequentially to maintain pressure)
- Historical data analysis to optimise watering schedules

You don't need to do it all at once. Start with one zone, one sensor, one automation. Get that working reliably, then expand.

## What It Costs: The Full Breakdown

| Component | Cost (AUD) |
|-----------|-----------|
| Home Assistant hardware (HA Green or RPi) | $80-$150 |
| ESP32 board + capacitive sensor (1 zone) | $15-25 |
| Smart relay for solenoid (1 zone) | $15-30 |
| Waterproof enclosure + sundries | $10-20 |
| **Total for 1-zone starter setup** | **$120-$225** |
| Each additional zone (sensor + relay) | $25-50 |
| **Full 4-zone setup** | **$200-$375** |

Compare that to a Hydrawise 6-zone controller at $350+ (without soil moisture sensors), and the DIY route is competitive on price while being infinitely more flexible.

## Tips From the Trenches

**Start simple.** Your first automation should be basic. Get reliable before getting clever.

**Use `input_boolean` toggles.** Always have a global "irrigation enabled" toggle. When something goes wrong (and it will, at first), you want a single switch to turn everything off.

**Monitor before automating.** Run your soil moisture sensors for 2-3 weeks before creating automations. Understand what "normal" looks like for your garden — different beds, different soil, different sun exposure will all read differently.

**Waterproof everything twice.** Australian conditions are harsh. Heat, UV, rain, and possums will all test your installations. Over-engineer the weatherproofing.

**Keep a manual backup.** Your irrigation system should still work manually if Home Assistant goes down. A physical valve or tap bypass is essential.

**Log everything.** Home Assistant's recorder and history components let you track soil moisture, watering events, and weather data over time. This data is gold for understanding your garden's needs across seasons.

## Going Further

This guide gets you from zero to a functional automated garden. But there's a lot more you can do — drip irrigation optimisation, building wicking bed auto-fill systems, integrating with rainwater harvesting, and using machine learning to predict your garden's water needs.

[*Set and Forget: The Aussie Guide to Automated Gardening*](/books/set-and-forget/) covers the complete system, from sensor selection through to advanced automations that handle an entire food production garden with minimal human intervention. If you've got the Home Assistant bug and a garden that needs looking after, it's the logical next step.

Now go build something. Your tomatoes are waiting.
