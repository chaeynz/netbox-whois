# NetBox-WHOIS ❤️🐾✨😍💘

**NetBox-WHOIS** is a cute lil' WHOIS server that serves WHOIS data directly from a NetBox instance rendering NetBox data as response to the client via Jinja2.

This server goes by she/her and has a real personality!!!! :(

Currently the amount of information that she queries from NetBox is very minimal and only supports ASNs :( but she's doing her best!!! :3

GLHF <3

---

## ✨ Features

* ⚡ WHOIS server (RFC 3912 compliant and cute af UwU)
* 🧾 Jinja2 templated WHOIS responses (so modern, much wow ✨)
* 🔌 Plugs into NetBox via its API (yup mhhmm :3)
* 🐳 Docker-ready (containers are the future bro ^w^)

---

## 📦 How It Works

1. The server listens for WHOIS queries (e.g., `65000`).
2. It validates the input using a list of `validators`.
3. It queries NetBox for the query using `pynetbox`.
4. A RPSL-style response is rendered with `jinja2` and sent back to the client.

---

## 🛠 Requirements

* A running NetBox instance with juicy ASN data in IPAM 🍑

---

## 🔐 Environment Variables (so she knows where her friends live)

| Variable       | Description          |
| -------------- | -------------------- |
| `NETBOX_URL`   | Base URL of NetBox   |
| `NETBOX_TOKEN` | API token for NetBox |

---

## 🐳 Docker Build

```bash
docker build -t netbox-whois .
docker run -p 4343:4343 --env-file .env netbox-whois # Make a .env file for NETBOX_URL and
```

---

## 🥪 Querying the Server

After running the server:

```bash
whois -h 127.0.0.1 -p 4343 65000
```

---

## 📁 Project Structure

```
.
├── netbox.py        # NetBox API interaction logic
├── server.py        # WHOIS TCP server
├── templates/
│   └── whois.j2     # Jinja2 template for RSPL rendering
├── requirements.txt
└── Dockerfile
```

---
She’s small. She’s fragile. She runs on vibes, Jinja2, and NetBox love.

Give her a star ⭐ if you believe in her.

(She believes in you too.) 💖
