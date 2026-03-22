# Gray et al. (2024) Dark Patterns Ontology

**Citation:** Gray, C. M., Santos, C., Bielova, N., & Mildner, T. (2024). An Ontology of Dark Patterns. *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*, ACM.

**Structure:** 3-level hierarchy — 5 high-level strategies, 25 meso-level angles of attack, 35 low-level means of execution (65 total).

---

## 1. OBSTRUCTION

**Level:** High | **Definition:** Making a process more difficult than it needs to be, with the intent to dissuade certain actions.

### 1.1 Roach Motel
**Level:** Meso | **Definition:** A design that makes it easy to get into a situation but difficult to get out of it.
**What to look for:** Easy signup but buried/complex cancellation; simple opt-in but multi-step opt-out; asymmetric effort between joining and leaving.

#### 1.1.1 Immortal Accounts
**Level:** Low | **Definition:** Making it impossible or extremely difficult to delete an account or terminate a service.
**Visual indicators:** No visible delete account option; delete buried deep in settings; deletion requires contacting support by phone/mail; "deactivate" offered instead of true deletion.

#### 1.1.2 Dead End
**Level:** Low | **Definition:** A path in a user flow that leads to no meaningful outcome, wasting the user's effort.
**Visual indicators:** Links that lead to unhelpful pages; "learn more" buttons that go nowhere useful; circular navigation in help/support flows.

### 1.2 Creating Barriers
**Level:** Meso | **Definition:** Introducing unnecessary steps or obstacles that prevent users from achieving their desired outcome efficiently.
**What to look for:** Extra verification steps only for undesired actions; requiring phone calls for what could be done online; unnecessary form fields.

#### 1.2.1 Price Comparison Prevention
**Level:** Low | **Definition:** Making it deliberately difficult to compare prices, whether between products on the same site or across different sites.
**Visual indicators:** Non-standard unit pricing; bundled pricing that obscures per-item cost; different pricing structures for similar products; blocking price-comparison tools.

#### 1.2.2 Intermediate Currency
**Level:** Low | **Definition:** Using a virtual currency or token system to obscure the real monetary cost of items or actions.
**Visual indicators:** Points, gems, coins, credits instead of real currency; conversion rates that are hard to calculate; purchasing virtual currency in bundles that don't align with item prices.

### 1.3 Adding Steps
**Level:** Meso | **Definition:** Injecting unnecessary additional steps to a process to discourage completion.
**What to look for:** Multi-page forms for simple actions; requiring re-entry of information already provided; extra confirmation screens only for opt-out actions.

#### 1.3.1 Privacy Maze
**Level:** Low | **Definition:** Making privacy settings or information scattered, confusing, and requiring many steps to navigate.
**Visual indicators:** Privacy controls spread across multiple settings pages; no single privacy dashboard; needing many clicks to find or change privacy preferences.

---

## 2. SNEAKING

**Level:** High | **Definition:** Attempting to hide, disguise, or delay the disclosure of information relevant to the user's decision-making.

### 2.1 Bait and Switch
**Level:** Meso | **Definition:** Presenting one option or outcome, but substituting a different, less desirable one when the user acts.
**What to look for:** Advertised product/feature differs from what's delivered; clicking one action triggers a different action; terms change after initial agreement.

#### 2.1.1 Disguised Ad
**Level:** Low | **Definition:** Advertising content disguised as navigation, content, or other non-advertising interface elements.
**Visual indicators:** "Download" buttons that are actually ads; sponsored content without clear labeling; ads styled to look like search results or articles; native ads that mimic editorial content.

### 2.2 Hiding Information
**Level:** Meso | **Definition:** Deliberately concealing or delaying the presentation of relevant information.
**What to look for:** Costs revealed late in checkout; terms hidden behind expandable sections; important conditions in fine print.

#### 2.2.1 Sneak into Basket
**Level:** Low | **Definition:** Adding extra items, services, or charges to a user's shopping cart without their explicit consent.
**Visual indicators:** Pre-added items in cart; insurance or warranties auto-added; donation or tip auto-included; additional services checked by default during checkout.

#### 2.2.2 Drip Pricing / Hidden Costs / Partitioned Pricing
**Level:** Low | **Definition:** Revealing additional mandatory fees, charges, or price components incrementally throughout the purchase process rather than upfront.
**Visual indicators:** Base price shown initially, taxes/fees/service charges added later; "from $X" pricing where final price is significantly higher; mandatory charges revealed at checkout; separate booking/processing/service fees.

#### 2.2.3 Reference Pricing
**Level:** Low | **Definition:** Displaying inflated original prices alongside discounted prices to create a misleading impression of value.
**Visual indicators:** Crossed-out "original" prices that were never charged; permanent "sale" pricing; inflated "was" prices; "compare at" prices from unknown sources.

### 2.3 (De)contextualizing Cues
**Level:** Meso | **Definition:** Presenting information in a way that strips it of relevant context or adds misleading context.
**What to look for:** Statistics without source or baseline; claims presented without qualifying conditions; information framed to mislead.

#### 2.3.1 Conflicting Information
**Level:** Low | **Definition:** Presenting contradictory information in different parts of the interface, causing confusion.
**Visual indicators:** Different prices on product page vs. cart; contradictory terms in different sections; inconsistent descriptions of features or policies.

#### 2.3.2 Information without Context
**Level:** Low | **Definition:** Presenting data or claims without the necessary context to interpret them accurately.
**Visual indicators:** "Save 50%" without stating original price; star ratings without number of reviews; "most popular" without defining the metric; claims without sources.

---

## 3. INTERFACE INTERFERENCE

**Level:** High | **Definition:** Manipulating the user interface in ways that privilege certain actions over others, thereby confusing the user or limiting discoverability of important information.

### 3.1 Manipulating Choice Architecture
**Level:** Meso | **Definition:** Structuring the presentation of choices to steer users toward a particular option.
**What to look for:** Options arranged to favor the more profitable choice; visual or spatial hierarchy that directs attention; decoy options.

#### 3.1.1 False Hierarchy
**Level:** Low | **Definition:** Using visual design to give certain options prominence over others, making the preferred option appear to be the default or best choice.
**Visual indicators:** One button large/colored and another small/grey; "Recommended" or "Best Value" labels on the most expensive option; visual emphasis (size, color, position) on the desired action.

#### 3.1.2 Visual Prominence
**Level:** Low | **Definition:** Using color, size, contrast, or positioning to make certain elements more noticeable while downplaying others.
**Visual indicators:** Accept/agree buttons in bright colors, decline in grey text; large "Subscribe" vs tiny "No thanks"; high-contrast call-to-action vs low-contrast alternative.

#### 3.1.3 Bundling
**Level:** Low | **Definition:** Grouping products or services together so users cannot select only what they want.
**Visual indicators:** Features only available in expensive tiers; required add-ons; inability to purchase individual items from a bundle; all-or-nothing packages.

#### 3.1.4 Pressured Selling
**Level:** Low | **Definition:** Aggressive promotion of upgrades, add-ons, or premium options during the user's primary task.
**Visual indicators:** Upsell screens inserted in checkout; "Are you sure?" when declining upgrades; multiple upsell attempts; premium features prominently shown during basic task flow.

### 3.2 Bad Defaults
**Level:** Meso | **Definition:** Setting default options to the choice that benefits the service rather than the user.
**What to look for:** Pre-checked consent boxes; opt-out rather than opt-in for marketing; default settings that share data; auto-enrollment in services.

### 3.3 Emotional or Sensory Manipulation
**Level:** Meso | **Definition:** Using emotional appeals, visuals, or sensory elements to influence user decisions beyond rational consideration.
**What to look for:** Guilt-inducing imagery; celebratory animations after spending; sad faces or imagery when declining; emotional language.

#### 3.3.1 Cuteness
**Level:** Low | **Definition:** Using cute or endearing visual elements (mascots, characters, animations) to manipulate user emotions and decisions.
**Visual indicators:** Sad mascot when unsubscribing; cute characters encouraging purchases; playful animations that make spending feel fun.

#### 3.3.2 Positive or Negative Framing
**Level:** Low | **Definition:** Describing the same choice in positive terms for the desired action and negative terms for the undesired action.
**Visual indicators:** "Yes, protect my order" vs "No, I don't want protection"; "Get premium features" vs "Continue with limited access"; framing decline options negatively.

### 3.4 Trick Questions
**Level:** Meso | **Definition:** Using confusing language, double negatives, or ambiguous wording to mislead users into making unintended choices.
**What to look for:** Double negatives in opt-out checkboxes; confusing phrasing where checking a box means the opposite of what's expected; questions worded so that "yes" and "no" have unintuitive meanings.

### 3.5 Choice Overload
**Level:** Meso | **Definition:** Presenting an overwhelming number of options to make decision-making difficult, often steering users toward a default or recommended option.
**What to look for:** Excessive number of similar options; complex comparison matrices; many permission toggles; settings pages with dozens of options.

### 3.6 Hidden Information
**Level:** Meso | **Definition:** Placing critical information where users are unlikely to find it.
**What to look for:** Important terms in collapsed sections; key details in footnotes or behind "more info" links; conditions in hard-to-read font sizes; information requiring scrolling past other content.

### 3.7 Language Inaccessibility
**Level:** Meso | **Definition:** Using language that is difficult for users to understand due to complexity, jargon, or wrong language choice.
**What to look for:** Legal jargon in consumer-facing text; overly technical language; unclear terms.

#### 3.7.1 Wrong Language
**Level:** Low | **Definition:** Presenting important information in a language the user does not understand or has not selected.
**Visual indicators:** Terms and conditions only in a language different from the site's main language; cookie consent in a non-local language; untranslated legal text.

#### 3.7.2 Complex Language
**Level:** Low | **Definition:** Using unnecessarily complex, technical, or legal language to make information difficult to understand.
**Visual indicators:** Dense legal jargon in privacy policies shown to general users; overly technical descriptions of data practices; run-on sentences in terms of service.

### 3.8 Feedforward Ambiguity
**Level:** Meso | **Definition:** Failing to provide clear information about what will happen when a user takes an action.
**What to look for:** Buttons with unclear labels; actions whose consequences are not explained; "Continue" buttons where it's unclear what continuing means; lack of confirmation screens for significant actions.

---

## 4. FORCED ACTION

**Level:** High | **Definition:** Requiring users to perform a specific action to access or continue to access certain functionality, often unrelated to the task at hand.

### 4.1 Nagging
**Level:** Meso | **Definition:** Repeatedly making the same request or suggestion, interrupting the user's intended task.
**What to look for:** Repeated pop-ups to upgrade/subscribe; persistent banners that reappear after dismissal; recurring prompts to enable notifications; repeated requests to rate the app.

### 4.2 Forced Continuity
**Level:** Meso | **Definition:** Silently charging users after a free trial ends or continuing a subscription without adequate notice.
**What to look for:** Free trial requiring credit card upfront; auto-renewal without clear notice; no reminder before charging; difficult-to-find cancellation before renewal date.

### 4.3 Forced Registration
**Level:** Meso | **Definition:** Requiring users to create an account to access content or complete an action that doesn't inherently require one.
**What to look for:** Mandatory account creation to view content; requiring signup to complete a purchase (no guest checkout); forcing account to access basic features.

### 4.4 Forced Communication or Disclosure
**Level:** Meso | **Definition:** Requiring users to share personal information or contact others as a condition of using a service.
**What to look for:** Requiring phone number for email service; mandatory profile completion; forcing social sharing to unlock features.

#### 4.4.1 Privacy Zuckering
**Level:** Low | **Definition:** Tricking users into sharing more personal information than they intend to.
**Visual indicators:** Confusing privacy settings that default to public; settings that reset after updates; sharing toggles that are hard to find; opt-out language for data sharing.

#### 4.4.2 Friend Spam
**Level:** Low | **Definition:** Sending messages or invitations to a user's contacts under the guise of being from the user, without clear consent.
**Visual indicators:** "Invite friends" flows that send messages without clear preview; importing contacts and auto-messaging; unclear consent for who gets contacted.

#### 4.4.3 Address Book Leeching
**Level:** Low | **Definition:** Accessing and storing a user's contacts without clear consent or beyond what is necessary.
**Visual indicators:** Requesting contact access for unrelated features; storing contacts after one-time use; unclear scope of contact data usage.

#### 4.4.4 Social Pyramid
**Level:** Low | **Definition:** Requiring users to recruit others to unlock features or receive benefits.
**Visual indicators:** "Refer 3 friends to unlock"; gated features requiring social sharing; multi-level referral programs; rewards only achievable through recruitment.

### 4.5 Gamification
**Level:** Meso | **Definition:** Using game-like mechanics to drive engagement or spending beyond the user's original intent.
**What to look for:** Streaks, rewards, badges designed to create habit loops; progress bars that encourage continued engagement; loss aversion mechanics.

#### 4.5.1 Pay-to-Play
**Level:** Low | **Definition:** Creating artificial barriers that can only be overcome through payment.
**Visual indicators:** Energy/lives systems requiring payment to continue; paywalled content after investment of time; artificial wait times removable by payment.

#### 4.5.2 Grinding
**Level:** Low | **Definition:** Making progress extremely slow or tedious without payment, incentivizing users to pay to skip ahead.
**Visual indicators:** Dramatically different progression rates for free vs paid users; tasks designed to be tediously repetitive; time-gates that can be skipped with money.

### 4.6 Attention Capture
**Level:** Meso | **Definition:** Capturing and holding user attention through mechanisms that bypass conscious choice.
**What to look for:** Features designed to keep users engaged beyond their intent; mechanisms that exploit psychological responses.

#### 4.6.1 Auto-Play
**Level:** Low | **Definition:** Automatically playing content (videos, next episodes, feeds) without user initiation.
**Visual indicators:** Videos that play automatically on page load; auto-advancing to next episode with short countdown; infinite scroll feeds; auto-playing stories.

---

## 5. SOCIAL ENGINEERING

**Level:** High | **Definition:** Using social or psychological pressure to influence user decisions.

### 5.1 Scarcity and Popularity Claims
**Level:** Meso | **Definition:** Claiming that an item is scarce or popular to create pressure to act quickly.
**What to look for:** Stock level indicators; "X people are viewing this"; "selling fast" claims; popularity indicators that may be exaggerated or fabricated.

#### 5.1.1 High Demand
**Level:** Low | **Definition:** Displaying messages that claim high demand for a product or service, whether real or fabricated.
**Visual indicators:** "X people are looking at this right now"; "booked Y times today"; "trending" labels; "in high demand" badges.

### 5.2 Social Proof
**Level:** Meso | **Definition:** Using real or fabricated social signals to influence user decisions.
**What to look for:** Reviews, ratings, testimonials, usage statistics that may be manipulated, selective, or fabricated.

#### 5.2.1 Low Stock
**Level:** Low | **Definition:** Displaying low stock warnings to create urgency, whether real or fabricated.
**Visual indicators:** "Only X left in stock"; "selling fast"; "almost gone"; stock indicators in red/warning colors; "limited availability."

#### 5.2.2 Endorsements and Testimonials
**Level:** Low | **Definition:** Using testimonials, endorsements, or reviews that may be fake, incentivized, or selectively presented.
**Visual indicators:** Reviews without verified purchase badges; celebrity endorsements without disclosure; cherry-picked positive reviews; testimonials with stock photos.

#### 5.2.3 Parasocial Pressure
**Level:** Low | **Definition:** Leveraging perceived personal relationships (with influencers, creators, or fictional personas) to drive user decisions.
**Visual indicators:** Influencer promotions framed as personal recommendations; AI chatbots that simulate friendship; personalized messages from brand mascots.

### 5.3 Urgency
**Level:** Meso | **Definition:** Creating a sense of time pressure to force quick decisions without adequate reflection.
**What to look for:** Countdown timers; limited-time offers; expiring deals; language emphasizing immediacy.

#### 5.3.1 Activity Messages
**Level:** Low | **Definition:** Displaying notifications about other users' recent actions to create social urgency.
**Visual indicators:** "Someone in [city] just purchased..."; "X people bought this in the last hour"; real-time purchase notifications; booking activity popups.

#### 5.3.2 Countdown Timer
**Level:** Low | **Definition:** Displaying a countdown timer to create urgency around an offer or action, which may reset or be artificial.
**Visual indicators:** Timer counting down to "end of sale"; checkout countdown timers; timers that reset when they expire; timers on deals that are always available.

#### 5.3.3 Limited Time Message
**Level:** Low | **Definition:** Displaying messages about limited-time availability without a specific countdown.
**Visual indicators:** "Today only"; "Offer ends soon"; "Limited time offer"; "Don't miss out"; "Last chance" — especially when the offer recurs.

### 5.4 Shaming
**Level:** Meso | **Definition:** Using shame, guilt, or social pressure to influence user decisions.
**What to look for:** Language that makes users feel bad for declining; guilt-inducing decline options; social comparison pressure.

#### 5.4.1 Confirmshaming
**Level:** Low | **Definition:** Using guilt-inducing language on the option to decline an offer.
**Visual indicators:** "No thanks, I don't want to save money"; "I prefer to pay full price"; "No, I don't care about my health"; decline options phrased to shame the user.

### 5.5 Personalization
**Level:** Meso | **Definition:** Using personal data to tailor choices, prices, or information in ways that may not serve the user's interests.
**What to look for:** Dynamic pricing based on browsing history; personalized urgency messages; targeted upsells based on user profile; algorithmically curated options that prioritize profit over user benefit.

---

## Quick Reference Checklist

When auditing, systematically check each high-level category:

- [ ] **OBSTRUCTION**: Is anything unnecessarily hard to do? (cancel, delete account, compare prices, find privacy settings)
- [ ] **SNEAKING**: Is anything hidden, disguised, or added without consent? (hidden fees, disguised ads, sneak-into-basket, misleading context)
- [ ] **INTERFACE INTERFERENCE**: Is the UI steering choices unfairly? (false hierarchy, bad defaults, trick questions, hidden info, confusing language)
- [ ] **FORCED ACTION**: Is the user forced to do something unrelated? (nagging, forced registration, forced sharing, manipulative gamification)
- [ ] **SOCIAL ENGINEERING**: Is social/psychological pressure being applied? (fake scarcity, fake urgency, fake social proof, confirmshaming, manipulative personalization)
