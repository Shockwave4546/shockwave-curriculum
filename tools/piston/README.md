# Piston (code-execution engine): setup, gateway, and VM sizing

Piston runs the students' Java (and Python) for the Coding exercises. This folder has what is needed
to set it up and put it behind a gate. Background: `docs/exercise-authoring-conventions.md` (Coding
exercises, "Ch.25: the real Commands v3 scheduler, headless") and `docs/coding-exercises/brief.md`.

| Piece | What it is |
|---|---|
| [install-wpilib-jars.sh](install-wpilib-jars.sh) | One idempotent script that prepares Piston's Java 25 package: the WPILib 2027 jars, `quickbuf-runtime`, our headless helper, the classpath, and the JVM flags. Run it again on any new Piston host, then restart Piston. |
| [command3-test-support/](command3-test-support) | ~40 lines of our own code (fake opmode and a clock that only moves when told) that lets the Commands v3 scheduler run without a robot. |
| [gateway/](gateway) | The Python gateway: shared secret, cap on simultaneous runs, per-student limits, forwards to Piston. Includes tests, a load-test tool and an example systemd unit. |

Piston itself: `ghcr.io/engineer-man/piston`, run rootful and privileged under Podman (needed for its
sandbox), data in `~/piston-data`, API on `localhost:2000`, **never exposed to the internet**.

## Limits worth knowing

- Piston kills a run at **3 CPU-seconds** (and 3 wall-seconds) and when it writes more than **1024
  bytes** to stdout or stderr (`PISTON_OUTPUT_MAX_SIZE`; raise it before real use).
- A Java run costs about **1.2 CPU-seconds**. With the installer's JVM flags (SerialGC, C1 only) that
  is half of what a default JVM uses; without them, 3 simultaneous runs mostly failed.
- Memory is not the constraint: about 60-100 MB per run.

## Choosing the Piston VM (Azure, West US 2, pay-as-you-go, Linux; prices from the Azure Retail Prices API, 2026-10-07)

All are x64, which Piston's image needs (so no Arm sizes). A VM that runs the gateway needs no public
IP. Add about **$4.80/month** for a 32 GiB Premium SSD (or $2.40 for Standard SSD).

| Size | vCPU | RAM | Type | $/hour | **$/month** | Notes |
|---|---|---|---|---|---|---|
| `Standard_B2ats_v2` | 2 | 1 GiB | burstable (20% baseline) | 0.0094 | **6.86** | too little RAM once Piston, the gateway and the OS run |
| **`Standard_B2als_v2`** | 2 | 4 GiB | burstable (30% baseline) | 0.0376 | **27.45** | **recommended**: cheaper than the planned B2s, newer CPU, same RAM |
| `Standard_B2s` | 2 | 4 GiB | burstable (older) | 0.0416 | 30.37 | the size in the original plan |
| `Standard_B2ls_v2` | 2 | 4 GiB | burstable (Intel) | 0.0416 | 30.37 | no advantage over B2als_v2 here |
| `Standard_B2as_v2` | 2 | 8 GiB | burstable (40% baseline) | 0.0752 | 54.90 | more baseline CPU and RAM |
| `Standard_F2s_v2` | 2 | 4 GiB | **not burstable** | 0.0846 | 61.76 | compute-optimized; full CPU always |
| `Standard_D2as_v5` | 2 | 8 GiB | **not burstable** | 0.0860 | 62.78 | the cheapest non-burstable fallback |
| `Standard_D2as_v6` | 2 | 8 GiB | not burstable | 0.0908 | 66.28 | |
| `Standard_D2s_v5` / `_v6` | 2 | 8 GiB | not burstable (Intel) | 0.0960 / 0.1010 | 70.08 / 73.73 | |
| `Standard_B4als_v2` | 4 | 8 GiB | burstable (30% baseline) | 0.1330 | 97.09 | 4 vCPUs, if 2 prove too few |
| `Standard_D2ads_v6` | 2 | 8 GiB | not burstable | 0.1140 | 83.22 | has a local disk |
| `Standard_F2as_v6` | 2 | 8 GiB | not burstable | 0.1370 | 100.01 | |

**Does "burstable" hurt this workload?** A burstable VM earns CPU credits while idle and spends them
when busy (1 credit = 1 vCPU-minute at full speed). `B2als_v2` earns 36 credits an hour, banks up to
864, and starts with 60 (Microsoft's Basv2 documentation). One run is about 1.2 CPU-seconds, so
0.02 credits: a class at one run per second for an hour spends about 70 credits and earns 36, so the bank
lasts about a full day of continuous heavy use. Typical use (a dozen students, a run every 20-30 s each,
a couple of evenings a week) uses a small fraction of what is earned, so burstable is fine. It only
throttles under many hours of sustained load above roughly 0.5 runs per second.

**Plan:** start with `B2als_v2` (about $27.45 + $4.80 disk = **~$32/month**), run
`gateway/loadtest.py` on it to set `GATEWAY_MAX_CONCURRENT`, and move to `D2as_v5` (~$68 with disk) only if
the VM's CPU-credit balance runs down in real use. All sizes above are pay-as-you-go retail; reservations
or a savings plan would lower them, but the Sponsorship credit applies to pay-as-you-go.
