# REQUIREMENTS.md  

## 1. Overview  
**Product:** *private‑guard*  
**Goal:** Deliver a privacy‑first, ad‑free, tracking‑free suite of web‑based tools that replace popular online services (search, email, file sharing, etc.) for users who demand strong personal data protection. The product must be launch‑ready, self‑hostable, and able to integrate with Axentx’s existing AI inference stack (vLLM, SGLang) for optional intelligent features.

---

## 2. Functional Requirements  

| ID | Description |
|----|-------------|
| **FR‑1** | **User Account Management** – Users can create, verify (email + optional phone), login, and delete accounts. All authentication flows must support password‑less options (WebAuthn, OAuth 2.0 with privacy‑preserving providers). |
| **FR‑2** | **Privacy‑Focused Dashboard** – After login, users see a unified dashboard listing all enabled services (Search, Mail, File Share, Calendar). The UI must not load any third‑party scripts or trackers. |
| **FR‑3** | **Secure Search Service** – Provide a web search interface that queries only privacy‑respectful back‑ends (e.g., DuckDuckGo API, SearXNG). No query logging beyond anonymized aggregate statistics stored for < 24 h. |
| **FR‑4** | **End‑to‑End Encrypted Email** – Users can send/receive email via IMAP/SMTP gateways that encrypt messages at rest (AES‑256‑GCM) and in transit (TLS 1.3). Optional client‑side PGP integration. |
| **FR‑5** | **Encrypted File Storage & Sharing** – Users can upload files (max 5 GB per file) stored encrypted with per‑user keys. Sharing generates time‑limited, single‑use URLs that do not expose user identity. |
| **FR‑6** | **Calendar & Task Manager** – Private, server‑side stored calendar/events with optional iCal export. No external analytics. |
| **FR‑7** | **AI‑Assisted Features (optional)** – Leverage Axentx’s vLLM/SGLang stack to provide on‑device suggestions (e.g., email draft assistance) **without** sending raw user data to external APIs. |
| **FR‑8** | **Data Export & Portability** – Users can export all personal data (messages, files, calendar) in standard formats (JSON, mbox, iCal) and delete it permanently. |
| **FR‑9** | **Consent & Preference Center** – Users can toggle optional features (e.g., AI assistance) and view a clear log of data processing activities. |
| **FR‑10** | **Self‑Hosting Installer** – Provide a Docker‑Compose (or Helm) installer that deploys the full stack (frontend, API gateway, storage, AI inference) on a single host or Kubernetes cluster. |
| **FR‑11** | **Audit Logging** – Record all privileged actions (admin changes, key rotations) in an immutable, tamper‑evident log accessible only to super‑users. |
| **FR‑12** | **Compliance Export** – Generate GDPR/CCPA‑compatible data‑subject request reports on demand. |

---

## 3. Non‑Functional Requirements  

| ID | Requirement |
|----|-------------|
| **NFR‑1** | **Performance** – UI page load < 2 s on a 3G connection; API latency ≤ 150 ms for core operations (search, email send/receive, file upload). |
| **NFR‑2** | **Scalability** – System must handle 10 k concurrent users with horizontal scaling via container orchestration. |
| **NFR‑3** | **Security** – All communications TLS 1.3; at‑rest encryption with per‑user keys; secret management via Vault‑compatible backend. |
| **NFR‑4** | **Privacy** – No third‑party analytics, cookies, or fingerprinting. All logs must be anonymized; raw user data never leaves the host environment. |
| **NFR‑5** | **Reliability** – 99.9 % uptime SLA; automatic failover for storage (replicated across 2 nodes). |
| **NFR‑6** | **Observability** – Export metrics (Prometheus) and logs (structured JSON) for health monitoring; include privacy‑safe request counts. |
| **NFR‑7** | **Maintainability** – Codebase follows Axentx’s style guide; CI/CD pipeline with unit, integration, and security tests; 80 % test coverage minimum. |
| **NFR‑8** | **Portability** – Must run on Linux (Ubuntu 22.04+), ARM64 and x86_64 architectures. |
| **NFR‑9** | **Licensing** – All third‑party components must be compatible with Apache‑2.0 or MIT licenses; no GPL‑v3 dependencies. |
| **NFR‑10** | **Data Residency** – Option to configure storage location (EU, US, etc.) to satisfy regional compliance. |

---

## 4. Constraints  

1. **Technology Stack** – Must integrate with existing Axentx AI stack (vLLM, SGLang) for optional features; cannot introduce conflicting runtime versions.  
2. **Dataset Usage** – Any AI‑assisted models must be trained only on Axentx‑provided datasets (auto, instr‑resp, messages, system‑user‑assistant). No external proprietary data.  
3. **Resource Limits** – Initial MVP must run on a single VM with ≤ 8 CPU cores, 16 GB RAM, and 500 GB SSD.  
4. **Regulatory** – Must comply with GDPR, CCPA, and ePrivacy Directive out‑of‑the‑box.  
5. **Open‑Source** – The final product must be released under Apache‑2.0 license, matching Axentx policy.  

---

## 5. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | Users will access the service via modern browsers supporting WebAuthn and ES2022 JavaScript. |
| **A‑2** | The host environment provides a secure OS baseline (Ubuntu 22.04 LTS, SELinux enabled). |
| **A‑3** | Email delivery can rely on existing SMTP relay services that respect privacy (e.g., ProtonMail Bridge) – no need to run a full MTA. |
| **A‑4** | Search back‑ends (DuckDuckGo, SearXNG) provide public APIs without usage caps that meet expected traffic. |
| **A‑5** | AI inference hardware (GPU/CPU) will be provisioned by the Ops team; the product only needs to expose a REST endpoint to the inference service. |
| **A‑6** | Users are willing to run the self‑hosted installer on their own infrastructure for maximum privacy; a managed‑hosting option is out of scope for MVP. |
| **A‑7** | Existing Axentx CI/CD pipelines can be extended to include this repo without major re‑architecture. |

---

## 6. Acceptance Criteria  

* All functional requirements FR‑1 – FR‑12 are demonstrably implemented and pass automated acceptance tests.  
* Non‑functional thresholds (NFR‑1 – NFR‑10) are verified in performance, security, and compliance test suites.  
* The Docker‑Compose installer spins up a fully functional private‑guard instance on a fresh Ubuntu VM in ≤ 10 minutes.  
* Independent security audit (internal or third‑party) reports no critical findings.  
* Documentation (user guide, admin guide, API spec) is complete and versioned alongside the code.  

---  

*Prepared by:* Senior Product/Engineering Lead – Axentx  
*Date:* 2026‑06‑17
