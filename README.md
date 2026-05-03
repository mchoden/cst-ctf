# 🔓 Security Workshop

19 flags across 6 labs. Find the vulnerabilities. Capture the flags.

## Quick Start

### GitHub Codespaces (recommended)
1. Click green **Code** button → **Create codespace on main**
2. Wait ~60 seconds
3. In **Ports** tab → make port 5000 **Public**
4. Click 🌐 next to port 5000

### Local
```bash
pip install flask PyJWT
bash run.sh
# Open http://localhost:5000
```

## Labs
- **CORS** — Cross-origin misconfigurations (3 flags)
- **CSRF** — Cross-site request forgery (2 flags)
- **Auth** — Authentication bypass (5 flags)
- **API** — API security (3 flags)
- **SSRF** — Server-side request forgery (3 flags)
- **Microservices** — Service trust & lateral movement (3 flags)

## Tools
- Browser + DevTools
- `curl` in terminal
- jwt.io for token analysis
- `md5sum` for hash computation

## Rules
1. Only attack localhost — nowhere else
2. Flags look like `FLAG{...}`
3. Submit flags at http://localhost:5000/flags
4. Hints on each page if you're stuck
5. Work in pairs
