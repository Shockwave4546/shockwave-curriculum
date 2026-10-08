# Azure / hosting approach: handoff for a fresh session (2026-10-08)

Written so a new session can revisit the whole Azure and hosting direction **without the old chat**.
Everything here was checked on the dates shown; prices are West US 2 pay-as-you-go retail (Azure Retail
Prices API, 2026-10-07) and should be re-checked before a purchase. Nothing in this document has been
deployed to Azure yet except the old Static Web App and test storage listed below.

## 1. What Joe wants to decide

How and where to host the **Shockwave Programming Academy** (the Nuxt app in `shockwave-programming-academy`,
which serves the curriculum) and its **code-execution engine (Piston)**, using as many free tiers as
possible and the **Microsoft Azure Sponsorship credit** for the rest. He has changed his mind more than
once and says he is "never tied to a single specific thing"; he explicitly wants to revisit the whole Azure
approach. **Do not assume any earlier choice is final**, but note what has been tested.

Standing preferences (also in memory): decisions one at a time with ranked options and pros/cons first;
no assumptions (ask); **no new packages or downloads without his approval**; keep the user tiers
**Team -> Admin Mentor -> Mentor / Parent / Student** whatever the host; students are minors.

## 2. Where things stand

| Piece | State |
|---|---|
| Curriculum content | Done and pushed: Ch.1-28 lessons, examples, exercises, 80 narrated lessons |
| Coding exercises | **60 pushed** (Ch.5-13, 15-26, 28), all verified on Piston; Ch.25 runs the real Commands v3 scheduler |
| Academy app | Pushed; all 60 coding exercises interactive **locally** (harness + full-program screens) |
| Piston (local dev machine) | Works (rootful Podman container `piston_api`, data `~/piston-data`). **Currently stopped: `sudo podman start piston_api`** |
| Piston gateway | Built, 24 tests, load-tested; **not deployed anywhere** (`tools/piston/gateway/`) |
| Back end (login, progress, teams) | **Not built.** Waiting on the host decision and on Joe's data-structure draft |
| `/piston/execute` on a deployed site | Missing: coding exercises work only under `nuxt dev` (dev proxy to local Piston) |
| Azure Piston VM, OpenProject VM | **Not created** |

Latest commits: curriculum `4603c1f`, academy `4a6a21c` (both pushed, clean).

### Hosting history in one paragraph
Started on **Azure Static Web Apps (SWA) Free**; the narrated pages made the site (305 MB without mp3
sources, 465 MB with) exceed SWA Free's 250 MB per-environment cap. Investigated Blob, SWA Standard,
Container Apps, a VM, and **DreamHost shared hosting**. DreamHost served the full site with no app changes
(upload 12 s; largest page loads in 665 ms; narration works). Joe then chose to keep everything on
DreamHost with a PHP + MySQL back end and keep only **Piston and OpenProject** on Azure, but later said he
may move the web app back to an Azure VM for ease. The SWA workflow is **disabled** (manual only) so pushes
don't deploy.

## 3. The open decision: where the web app lives

| | **A: DreamHost web + Azure Piston VM** | **B: everything on Azure VMs** | **C: SWA Free + Blob + Functions + Azure SQL free** |
|---|---|---|---|
| Web hosting cost | $0 (existing plan) | web VM ~$35.90/mo (B2als_v2 $27.45 + disk $4.80 + IP $3.65) | $0 |
| Piston VM | ~$35.90/mo (public IP needed) | ~$32.25/mo (private) | ~$35.90/mo (public IP needed) |
| **Total** | **~$36/mo (~$431/yr)** | **~$68/mo (~$818/yr)** | **~$36/mo** |
| Back end | PHP 8.3/8.5 + MySQL (no packages) | Nuxt server mode (one TypeScript codebase); SQLite via the already-used `better-sqlite3` | Azure Functions (managed, HTTP only) + Azure SQL |
| Gateway exposure | **Public**: TLS with a pinned self-signed cert + secret (IP allow-list unreliable) | **Private** (same VNet) | **Public** (managed Functions have no managed identity, Key Vault or documented private network access) |
| Upkeep | none for web | patch + back up web VM, manage TLS cert | few moving parts but 3 services |
| Status | tested and working (static) | not built | not built |
| Catches | second codebase (PHP); public gateway | ~2x cost; ops work | narrated player messaging must change (cross-origin iframe); 3 new packages to approve; serverless SQL pauses when idle; SWA Free sign-in only supports Microsoft/GitHub + 25 invited users, so login would be custom |

Container Apps (scale to zero, ~$5/mo registry, cold start never measured) is **on hold**, not ruled out.
A cold-start test was planned and never run.

Why Azure alone is awkward: the narrated pages (214 MB) are the size problem. They can't be split to a
different origin without breaking two features of the app's iframe code (pause on tab change, mini-player
sizing) unless the player and app switch to `postMessage`.

My recommendation at the time: **A** (half the cost, working today, nothing to patch) unless Joe wants one
language and a fully private gateway (then **B**). Decision not made.

## 4. Verified facts worth keeping

**Azure account** (tenant Dover Shockwave Robotics). Subscriptions: **Microsoft Azure Sponsorship**
`965fa139-3b8a-4202-8680-bc674accfb87` (the default, holds everything), plus two empty Pay-As-You-Go
subscriptions `11f726b0-740e-4157-a35c-ba1b15e934cf` and `caa029b2-b7c2-450e-a06c-a539925c6786`.
Resource group `rg-joe.chan-6204`. Existing resources: Speech/Foundry accounts `joechan-9338-resource`
(S0) and `joechan-speech-f0` (F0) in westus3 (TTS), SWA `shockwave-academy` (Free, westus2, workflow
disabled), storage account `shockwavelatencytest` (a few MB, from the latency test; delete when no longer
needed). **Spend in the last 12 months: $1.06** (September TTS). The **Sponsorship credit balance is not
readable through the API** (see Microsoft's sponsorship page). The older plan assumed a **$2,000/year
Nonprofit credit** that doesn't roll over; it is not the same account and its status here is unverified.

**Prices** (per month, 730 h): B2als_v2 (2 vCPU, 4 GiB, burstable AMD) **$27.45**; B2s $30.37; B2ats_v2
(1 GiB) $6.86; B2as_v2 (8 GiB) $54.90; non-burstable F2s_v2 $61.76, D2as_v5 $62.78; Premium SSD 32 GiB
(P4) $4.80, Standard SSD E4 $2.40; Standard static public IPv4 $3.65; SWA Standard $9.00 (500 MB per
environment); Blob Hot LRS $0.0184/GB-month with the first 100 GB of outbound data free each month;
Container Registry Basic ~$5.07; Front Door Standard $35 base. **B2pls_v2 (Arm) $24.53 but Piston's
published image is amd64-only**; an Arm build would need our own image from an end-of-life Debian base
(about $35/year saved, not worth it yet).

**SWA limits:** Free 250 MB per environment (500 MB total), 100 GB/month bandwidth, 2 custom domains,
managed Functions (HTTP triggers only), preconfigured sign-in (Microsoft/GitHub), custom roles by
invitation (25). Azure SQL free offer: 100,000 vCore-seconds + 32 GB per month, free for the life of the
subscription, auto-pauses at the limit or continues at charge.

**DreamHost** (shell user `dsr_academy`, host `iad1-shared-b8-10.dreamhost.com`, subdomain
`academy.dovershockwave.org`, SSH key `~/.ssh/dreamhost_dsr_academy`): Shared Unlimited (no hard storage
cap); Ubuntu 24.04; PHP 8.3 default and 8.5 (openssl, curl, json, session, pdo_mysql, sodium; no
Composer); command-line `php` is 8.2; Python 3.12.3; Passenger present but off; `rsync` available;
HTTPS works. A full upload (315 MB) took 12 s. The site is behind a **panel password**
(Htaccess/WebDAV; deploys must skip `.htaccess` and `.htpasswd`). PHP's outbound IP is `173.236.249.141`
(one of ~50 on a shared server, so **no reliable IP allow-list**); PHP curl supports certificate pinning.
Note: the test upload there is of the Sept 27 build; the site's contents are stale.

**Piston and the gateway** (details in `tools/piston/README.md` and `tools/piston/gateway/README.md`):
- Piston kills a run at **3 CPU-seconds** and at 3 wall-seconds, and at **1024 bytes** of output
  (`PISTON_OUTPUT_MAX_SIZE`; raise it before real use). It has no login and must never be internet-facing.
- A Java run costs ~0.7-1.0 CPU-s (simple) to ~1.0-1.4 CPU-s (Ch.25 scheduler) after the installer sets
  `-XX:+UseSerialGC -XX:TieredStopAtLevel=1 ...`. Without those flags 3 simultaneous scheduler runs mostly
  failed.
- Measured on 2 CPUs: throughput is flat from 2 runs at once (about 1.4-2.8 runs/s); **more concurrency
  only slows each run**. Wall time at 4 at once: 1.4-2.0 s (simple), up to 2.8 s (scheduler, threads of one
  core). The gateway cap default is **3** (a setting; measure on the real VM with `loadtest.py`).
- Recommended VM: `Standard_B2als_v2` (~$32/mo with disk). Burstable is fine for classroom bursts
  (earns 36 credits/h, banks 864; one run is ~0.02 credit).
- WPILib setup for Ch.25: 8 WPILib jars (2027.0.0-alpha-7) + `quickbuf-runtime-1.4` (Joe approved
  2026-10-06) + our 40-line `command3-test-support` helper + two `--add-opens` flags, all installed by
  `tools/piston/install-wpilib-jars.sh` (needs sudo; restart Piston after). Real controller classes
  (`CommandXboxController`) can't be used headlessly (need WPILib's native library).
- Gateway contract for the back end: `POST /execute` with `Authorization: Bearer <secret>` and
  `X-Student-Id`; same JSON as Piston; only `language/version/files/stdin/args` forwarded; 429/503 with
  `Retry-After`; code never logged.

**The app's coding-exercise runner** (`app/utils/codingRunner.ts`) posts to **`/piston/execute`** on the
same origin; the dev server proxies it to local Piston. Any deployed host must serve that path (check the
student's login, then call the gateway).

## 5. Not done / loose ends

- **Host decision** (section 3), then the **back end** (login with `password_hash`/scrypt, sessions,
  progress, teams) and Joe's **data-structure draft** (Team, Admin Mentor, Mentor, Parent, Student; he is
  writing it; five open design questions were listed: who creates accounts, parent-student links, multiple
  roles/teams, a site-wide admin, password resets by email).
- Create the **Piston VM** (private, no public IP unless option A/C), install Podman + Piston, run the install
  script, deploy the gateway (example systemd unit provided), raise `PISTON_OUTPUT_MAX_SIZE`, then run
  `loadtest.py` to set the cap. Also the **OpenProject VM** from the older plan
  (`~/.claude/plans/azure-piston-openproject-entra-id.md`, the Entra parts are superseded).
- A GitHub Actions deploy for whichever host is chosen (SWA's is manual-only now).
- Fix before real use: the SWA Free app and `shockwavelatencytest` are leftovers; the **Entra ID design is on
  hold** (login moved to MySQL accounts; Piston's gateway uses a shared secret instead of Entra tokens).
- Optional later: full-program polish, a playground at the end of each section (the gateway must keep
  accepting any code), possible Arm Piston image, Container Apps cold-start test.
- Docs that describe the old plan: `shockwave-programming-academy/docs/azure-deployment.md` (history +
  "If moving back to Azure") and `docs/dreamhost-deployment.md` (current state of the test).

## 6. Suggested agenda for the new session

1. Re-state the goals (free tiers first, Sponsorship credit second, minors' data, tiers kept).
2. Re-check the Sponsorship credit balance and any expiry (Joe, in the portal) because the whole cost
   comparison depends on it.
3. Walk the section 3 table; add anything Joe raised since (e.g. whether he'd run Nuxt in server mode, or
   keep DreamHost for static only with Azure Functions for the API).
4. Decide **A / B / C** (or a new option), then the back-end language, then the data structure.
5. Only then create Azure resources (pricing re-check first; create the Piston VM in a region near the web
   host; DreamHost is in Ashburn, VA, so East US is the closest Azure region, West US 2 was used for
   prices here).

## 7. Where to look

| Topic | File |
|---|---|
| Piston setup, limits, VM price table | `tools/piston/README.md` |
| Gateway, settings, measured concurrency | `tools/piston/gateway/README.md` (+ `gateway.py`, `test_gateway.py`, `loadtest.py`, `piston-gateway.service`) |
| Coding exercise design, Ch.25 headless scheduler | `docs/exercise-authoring-conventions.md` |
| Coding exercise briefs and outcomes | `docs/coding-exercises/brief.md` |
| Academy hosting docs | `shockwave-programming-academy/docs/azure-deployment.md`, `docs/dreamhost-deployment.md` |
| Older Azure architecture plan (partly superseded) | `~/.claude/plans/azure-piston-openproject-entra-id.md` |
| Academy status and plan | `~/.claude/plans/shockwave-programming-academy-phase1.md` |
