#!/usr/bin/env python3
"""BDG state-of-the-art frontend design gate.

A hard, reusable review contract for a human/model art director. It intentionally
combines non-negotiable measurable checks with a visual-review rubric; passing
static checks alone is never a design pass.
"""
from __future__ import annotations

from dataclasses import dataclass

VIEWPORTS = (320, 360, 390, 430, 768, 1024, 1440)

@dataclass(frozen=True)
class Gate:
    name: str
    requirement: str
    evidence: str
    severity: str

GATES = (
    Gate('Mobile thesis', 'At 320–430px the header, H1, first paragraph and primary CTA form an immediate, calm first-screen story. The CTA is visible or reached without a visually exhausting wall of text.', 'Exact viewport screenshots plus element bounds.', 'P0'),
    Gate('Typography craft', 'No headline orphan, poor wrap, cramped line-height, overlong mobile line, weak contrast or desktop font merely scaled down. Type scale, rhythm and labels look intentional at every viewport.', 'Screenshot review plus computed font/line-height report.', 'P0'),
    Gate('Composition and rhythm', 'Every section has a purpose, consistent gutters, deliberate entry/exit spacing and an alternate visual rhythm. No accidental gaps, repetitive card wall or density spikes.', 'Full-page screenshots at 390 and 1440px.', 'P0'),
    Gate('Controls', 'All interactive controls have a 44px minimum touch target, visible keyboard focus, coherent active/hover treatment and unambiguous CTA hierarchy.', 'Computed bounding boxes and keyboard walkthrough.', 'P0'),
    Gate('Menu and focus', 'Mobile menu has modal semantics, focus containment, Escape close, return focus, no background interaction and no page-scroll leak.', 'Keyboard interaction recording/checklist.', 'P0'),
    Gate('Illustration integrity', 'Illustrative operational UI is clearly labelled, semantic and static; reject client names, live-looking KPIs, fake results, status events, stock imagery and laptop mockups.', 'Exact mobile/desktop screenshots plus DOM review.', 'P0'),
    Gate('Responsive integrity', 'scrollWidth never exceeds innerWidth; no clipped controls; no overlap from header/sticky elements; no layout shift caused by media.', 'DOM metrics at every required viewport.', 'P0'),
    Gate('Accessibility restraint', 'Readable contrast, reduced-motion respect, semantic heading order and no colour-only meaning.', 'Contrast/DOM audit plus reduced-motion screenshot.', 'P1'),
    Gate('Desktop preservation', '1024/1440 retains or improves the approved desktop hierarchy and does not become a compromised enlarged-mobile layout.', 'Before/after desktop comparison.', 'P0'),
    Gate('Bespoke BDG character', 'Deep-green/mineral/eucalyptus/ochre system feels calm, premium and practical for regional trade businesses; permit restrained grid and radial atmosphere plus explicitly illustrative operational UI, while rejecting blue SaaS, glassmorphism, fake proof and generic template decoration.', 'Art-direction review against actual rendered pages.', 'P0'),
)

if __name__ == '__main__':
    print('BDG STATE-OF-THE-ART FRONTEND DESIGN GATE')
    print('Required viewports:', ', '.join(f'{w}px' for w in VIEWPORTS))
    for gate in GATES:
        print(f'[{gate.severity}] {gate.name}: {gate.requirement}\n  Evidence: {gate.evidence}')
    print('\nPASS RULE: no P0 failures; P1 failures require explicit owner decision or correction.')
