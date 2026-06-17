# STORIES.md

## Project: private-guard
**Goal:** Deliver a privacy‑first, ad‑free, tracking‑free suite that replicates the core functionality of popular web tools while guaranteeing user data never leaves the device or is harvested for advertising.  

---

## Epics & Backlog

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Core Privacy Engine** | Build the foundational library that intercepts, sanitizes, and blocks tracking/ads for all downstream tools. | ✅ |
| **E2 – Private Search** | A privacy‑preserving search front‑end that proxies queries through a zero‑log resolver. | ✅ |
| **E3 – Secure Note‑Taking** | Encrypted, local‑first note app with optional end‑to‑end sync via user‑controlled storage. | ✅ |
| **E4 – Private Media Viewer** | Ad‑free video/audio player that streams via privacy‑preserving proxies and blocks telemetry. | ⏳ |
| **E5 – Settings & Dashboard** | Unified UI for privacy controls, data export, and usage analytics (self‑hosted). | ⏳ |
| **E6 – Extensibility SDK** | Simple plugin system so third‑party tools can integrate the privacy engine. | ⏳ |

---

## User Stories

### Epic E1 – Core Privacy Engine
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E1‑01** | **As a developer, I want a configurable request interceptor, so that I can block trackers and ads across any HTTP client.** | - Provide a middleware (`privacyInterceptor`) for `fetch`, `axios`, and native Node/Browser APIs.<br>- Configurable blocklists (default: EasyList, EasyPrivacy).<br>- Returns original response when not blocked.<br>- Logs blocked URLs to a local, encrypted log file. |
| **E1‑02** | **As a security auditor, I want the engine to run in a sandboxed WebWorker, so that it cannot access the host filesystem unintentionally.** | - All interception runs inside a dedicated WebWorker.<br>- No direct `fs` or `process.env` access from the worker.<br>- Unit tests verify sandbox boundaries. |
| **E1‑03** | **As a power user, I want a “strict mode” toggle, so that all third‑party scripts are automatically stripped.** | - Toggle in the dashboard flips `strictMode` flag.<br>- In strict mode, any `<script>` with a non‑first‑party origin is removed before execution.<br>- Page still loads core functionality; visual regression tests confirm no breakage. |

### Epic E2 – Private Search
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E2‑01** | **As an end‑user, I want to search the web without being profiled, so that my queries stay private.** | - UI with a single search bar.<br>- Queries are sent to a zero‑log resolver (e.g., DuckDuckGo API) via the Core Privacy Engine.<br>- No cookies or fingerprinting scripts are loaded.<br>- Search results displayed with no sponsored links. |
| **E2‑02** | **As a privacy‑concerned user, I want results cached locally, so I can view them offline without re‑issuing the query.** | - Encrypted local cache (IndexedDB) stores the last 50 queries.<br>- Cache respects user‑set TTL (default 7 days).<br>- Cache miss falls back to live query. |
| **E2‑03** | **As a developer, I want the search component to be embeddable, so I can reuse it in other private‑guard tools.** | - Exported React component `PrivateSearch` with props for placeholder, theme, and result limit.<br>- Storybook demo with usage examples. |

### Epic E3 – Secure Note‑Taking
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E3‑01** | **As a user, I want to write notes that are encrypted at rest, so that only I can read them.** | - Notes stored in an encrypted SQLite DB (SQLCipher) or local file encrypted with AES‑256‑GCM.<br>- Encryption key derived from user password via PBKDF2 (min 200k iterations). |
| **E3‑02** | **As a user, I want optional end‑to‑end sync via my own cloud storage (e.g., Dropbox, Nextcloud), so I can access notes on multiple devices.** | - Sync module that uses OAuth‑2 token supplied by user.<br>- Data is encrypted client‑side before upload.<br>- Conflict resolution uses CRDT with deterministic merge. |
| **E3‑03** | **As a user, I want a quick‑search within my notes, so I can find information instantly.** | - Full‑text search runs on decrypted data in memory only.<br>- Search results highlight matches.<br>- No search index persisted unencrypted. |

### Epic E4 – Private Media Viewer
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E4‑01** | **As a viewer, I want to watch videos without ads or tracking pixels, so I can enjoy content uninterrupted.** | - Media player streams via a privacy proxy that strips tracking headers.<br>- No third‑party analytics scripts loaded.<br>- Playback works with HLS/DASH sources. |
| **E4‑02** | **As a user, I want the player to remember my playback position locally, so I can resume later without cloud sync.** | - Playback position stored in encrypted local storage keyed to media URL.<br>- Position restored on next load. |
| **E4‑03** | **As a developer, I want the player component to expose a clean API, so I can embed it in other private‑guard apps.** | - Exported Web Component `<private-media-player>` with attributes `src`, `autoplay`, `controls`.<br>- Events: `play`, `pause`, `ended`, `error`. |

### Epic E5 – Settings & Dashboard
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E5‑01** | **As a user, I want a central dashboard to toggle privacy features, so I can control my protection level.** | - Dashboard lists all active modules (Search, Notes, Media).<br>- Switches for “Strict Mode”, “Telemetry Blocking”, “Cache Size”.<br>- Changes apply instantly without restart. |
| **E5‑02** | **As a user, I want to export my data (notes, logs) in an encrypted archive, so I can back it up safely.** | - Export button creates a `.zip` encrypted with the same password‑derived key.<br>- Archive includes a manifest with SHA‑256 hashes for integrity verification. |
| **E5‑03** | **As a compliance officer, I need an audit log of blocked requests, so I can demonstrate privacy compliance.** | - Immutable, append‑only log stored in an encrypted file.<br>- UI view with filters (date, domain, action).<br>- Log can be signed with a user‑provided PGP key. |

### Epic E6 – Extensibility SDK
| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E6‑01** | **As a third‑party developer, I want an SDK to register custom blocklists, so I can extend privacy coverage for niche services.** | - `registerBlocklist(name: string, patterns: string[])` API.<br>- SDK validates patterns (regex or hostnames).<br>- Updated blocklist takes effect without restart. |
| **E6‑02** | **As a developer, I want to publish plugins that run inside the privacy engine sandbox, so I can add new features safely.** | - Plugin manifest (`plugin.json`) with `id`, `version`, `permissions`.<br>- Runtime loads plugins in isolated WebWorker contexts.<br>- Sample plugin that injects a custom header into allowed requests. |

---

## MVP Scope (First Release)

| Epic | Stories Included |
|------|-------------------|
| **E1** | E1‑01, E1‑02, E1‑03 |
| **E2** | E2‑01, E2‑02, E2‑03 |
| **E3** | E3‑01, E3‑02, E3‑03 |
| **E5** | E5‑01, E5‑02 |
| **E6** | E6‑01 |

*E4 (Media Viewer) and the full audit‑log UI (E5‑03) are deferred to post‑MVP sprints.*

---

## Definition of Done (DoD) for All Stories
1. Code passes unit tests with ≥ 90 % coverage.  
2. Integration tests validate end‑to‑end flow in both browser and Node environments.  
3. Linting and formatting conform to the repo’s ESLint/Prettier config.  
4. Documentation updated (README, API docs, and this STORIES.md).  
5. All new dependencies have approved licenses (Apache‑2.0, MIT, BSD).  
6. Security review completed – no secrets or vulnerable packages.  
7. Feature demo recorded and added to `docs/demos/`.  

--- 

*Prepared by the Private‑Guard product team, 2026‑06‑17.*
