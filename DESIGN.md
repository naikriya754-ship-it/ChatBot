---
name: Harmonic Assistant
colors:
  surface: '#f9f9fb'
  surface-dim: '#d9dadc'
  surface-bright: '#f9f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f5'
  surface-container: '#edeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e4'
  on-surface: '#1a1c1d'
  on-surface-variant: '#474552'
  inverse-surface: '#2f3132'
  inverse-on-surface: '#f0f0f2'
  outline: '#787583'
  outline-variant: '#c9c4d4'
  surface-tint: '#5c50b2'
  primary: '#342588'
  on-primary: '#ffffff'
  primary-container: '#4b3fa0'
  on-primary-container: '#bfb7ff'
  inverse-primary: '#c7bfff'
  secondary: '#605d62'
  on-secondary: '#ffffff'
  secondary-container: '#e6e1e7'
  on-secondary-container: '#666368'
  tertiary: '#512c39'
  on-tertiary: '#ffffff'
  tertiary-container: '#6b4250'
  on-tertiary-container: '#e7b1c1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4dfff'
  primary-fixed-dim: '#c7bfff'
  on-primary-fixed: '#170065'
  on-primary-fixed-variant: '#443798'
  secondary-fixed: '#e6e1e7'
  secondary-fixed-dim: '#cac5cb'
  on-secondary-fixed: '#1c1b1f'
  on-secondary-fixed-variant: '#48464a'
  tertiary-fixed: '#ffd9e3'
  tertiary-fixed-dim: '#eeb8c8'
  on-tertiary-fixed: '#31111d'
  on-tertiary-fixed-variant: '#633b48'
  background: '#f9f9fb'
  on-background: '#1a1c1d'
  surface-variant: '#e2e2e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.1px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-margin: 1rem
  stack-gap: 0.75rem
  inline-gutter: 0.5rem
  input-padding: 1rem
  bubble-padding: 0.75rem
---

## Brand & Style

The design system is centered on a **Modern Corporate** aesthetic that blends the systematic rigor of Material Design 3 with the refined elegance of Apple’s Human Interface Guidelines. The personality is "The Sophisticated Curator"—intelligent, unobtrusive, and deeply focused on the auditory experience. 

The visual style prioritizes **Deference**, ensuring the interface recedes to allow music metadata, album art, and artist information to remain the focal point. By utilizing high clarity, ample whitespace, and subtle depth transitions, the design system evokes a sense of calm and precision, mimicking the experience of high-end audio hardware in a digital environment.

## Colors

The palette is anchored by **Deep Indigo**, a color that suggests depth and late-night listening sessions. This primary hue is used sparingly for interactive states, key actions, and active identifiers to maintain high signal-to-noise ratios.

The background uses a specific **Neutral Off-White** (#F9F9FB) to reduce glare and differentiate from the pure white (#FFFFFF) used for elevated surfaces like chat bubbles and cards. Text colors follow a strict hierarchy of legibility, using deep grays rather than pure black to soften the reading experience during extended interactions.

## Typography

The design system utilizes **Inter** for its exceptional legibility and neutral characteristics. This choice reflects the "Gemini" style—efficient and utilitarian yet modern. 

Typography is used to create clear information architecture:
- **Headlines** use tighter letter-spacing and heavier weights to anchor the page.
- **Body Text** is optimized for conversational flow with a generous 1.5x line height.
- **Labels** are utilized for metadata (BPM, Genre, Duration) to provide technical detail without cluttering the primary conversation.

## Layout & Spacing

This is a **Mobile-First Fluid Grid** system. The layout relies on a strict 8px (0.5rem) base unit to ensure consistent vertical rhythm. 

- **Horizontal Margins:** A fixed 16px (1rem) margin is maintained on the left and right edges of the viewport.
- **Chat Flow:** Messages are stacked vertically with a 12px gap. 
- **Sticky Input:** The bottom bar is anchored with a background blur effect (backdrop-filter) to allow content to scroll behind it, maintaining the illusion of depth.

## Elevation & Depth

Elevation is communicated through **MD3 Tonal Layers** and **Ambient Shadows**. Surfaces are not just white; they are layered to indicate importance.

- **Level 0 (Background):** Neutral Off-White, flat.
- **Level 1 (Chat Bubbles/Chips):** White surface with a very soft, diffused shadow (0px 1px 3px rgba(0,0,0,0.08)).
- **Level 2 (Sticky Input Bar):** White surface with a more pronounced elevation shadow to indicate it sits above the scrolling content.
- **Level 3 (Modals/Overlays):** High diffusion shadows to draw focus during track selection or playlist editing.

## Shapes

The shape language is defined by **High Rounding** to create an approachable, "organic" feel consistent with modern mobile OS patterns. 

- **Chat Bubbles:** Use a 16px radius. User bubbles are anchored to the right, while assistant bubbles are anchored to the left.
- **Suggestion Chips:** Follow a pill-shape (stadium) geometry to distinguish them from actionable buttons or cards.
- **Input Field:** Features fully rounded ends to mirror the "pill" style of the suggestion chips, creating a cohesive bottom-of-screen identity.

## Components

### Chat Bubbles
The core interaction element. Bubbles use 12dp (0.75rem) internal padding. Assistant bubbles use a subtle gray outline or a Level 1 elevation, while User bubbles use the Primary Deep Indigo with white text for high contrast.

### Suggestion Chips
MD3-style outlined chips. These have a 1px border using the `on_surface_variant` color at low opacity. They are designed for quick-tap replies like "Play more like this" or "Who is the drummer?".

### Sticky Input Bar
A fixed container at the bottom of the viewport. It features a text input field, a "plus" icon for attachments (music links/files), and a dedicated "Send" button that only highlights in Primary Indigo when text is present.

### Music Cards
Specialized assistant responses that display album art, track title, and artist. These are presented as Level 1 elevated surfaces with a 12px radius, featuring a play/pause toggle in the primary color.

### Checkboxes & Radios
Used in "Filter" or "Settings" menus. These follow MD3 standards: a 2px stroke that fills in with the Primary Indigo color upon selection.