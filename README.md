# Your website — GitHub Pages setup

This folder is the whole site: plain HTML, no build step, no server. GitHub Pages serves it as-is, free, with HTTPS.

| File | What it is | Do I touch it? |
|---|---|---|
| `index.html` | The whole site — text, styles, 3D enzyme, Arabic/English switch | Only through step 3, or by asking me |
| `404.html` | The page shown if someone mistypes a link | No |
| `og.png` | The picture that appears when the link is shared on LinkedIn or WhatsApp | No |
| `favicon.png`, `apple-touch-icon.png` | Your rose monogram as the tab icon and phone icon | No |
| `robots.txt`, `sitemap.xml` | Tell Google the site exists | Step 3 fills in the address |
| `.nojekyll` | Tells GitHub to publish the files exactly as they are | Never delete it |
| `set-url.py` | A helper for step 3 | Run once, then ignore |

---

## Step 1 — Create the repository

1. Sign in at **github.com** (create a free account if you don't have one).
2. Top right **+** → **New repository**.
3. Repository name: `reem-portfolio` · Visibility: **Public** (Pages needs public on the free plan) · leave everything else unticked → **Create repository**.

> If you would rather have the address `https://YOUR-USERNAME.github.io` with nothing after it, name the repository exactly `YOUR-USERNAME.github.io` instead. Everything else below is identical.

---

## Step 2 — Upload the files and switch Pages on

1. On the empty repository page click **uploading an existing file**.
2. Open this folder on your computer, select **all** the files inside it — including the dot-file `.nojekyll` — and drag them into the browser.
   - On Mac, press **Cmd + Shift + .** in Finder to make `.nojekyll` visible before selecting.
   - Drag the *contents* of the folder, not the folder itself.
3. Scroll down, click **Commit changes**.
4. Go to **Settings** (top of the repository) → **Pages** (left sidebar).
5. Under *Build and deployment*: Source = **Deploy from a branch**, Branch = **main**, folder = **/ (root)** → **Save**.
6. Wait about a minute and refresh. GitHub shows: *Your site is live at* `https://YOUR-USERNAME.github.io/reem-portfolio/`

Open it on your phone and your laptop. That address is already public and secure.

---

## Step 3 — Put the real address into the metadata

The site works without this. What it fixes: the picture that appears when you share the link, and how Google lists you.

In this folder, open Terminal and run one line, using your real address:

```
python3 set-url.py https://YOUR-USERNAME.github.io/reem-portfolio
```

Then upload the three changed files (`index.html`, `robots.txt`, `sitemap.xml`) to the repository again — **Add file → Upload files** → drag → Commit. GitHub replaces the old ones.

No Terminal? Open the three files in TextEdit or Notepad, replace every `https://YOUR-DOMAIN` with your address (no slash at the end), save, and upload them the same way.

---

## Step 4 — Your own domain (optional, about $10–15 a year)

A domain on a PhD email signature reads very differently from a github.io address.

1. Buy the name — Cloudflare Registrar (sells at cost), Namecheap or Porkbun. `reemalkhalaileh.com`, or `.science` / `.bio` if the .com is taken.
2. At your registrar's DNS page, add five records:
   - **A** record, name `@` → `185.199.108.153`
   - **A** record, name `@` → `185.199.109.153`
   - **A** record, name `@` → `185.199.110.153`
   - **A** record, name `@` → `185.199.111.153`
   - **CNAME** record, name `www` → `YOUR-USERNAME.github.io`
3. Back in GitHub: **Settings → Pages → Custom domain** → type `reemalkhalaileh.com` → **Save**. GitHub adds a `CNAME` file to the repository by itself.
4. Wait for DNS to propagate (minutes to a few hours), then tick **Enforce HTTPS**. The certificate is free and automatic.
5. Run step 3 again with the new address and upload the three files.

---

## Step 5 — After it's live

- Test on a phone and a laptop: the language button, **Email me**, **LinkedIn**, **Save contact**, and the plain version link at the bottom.
- Paste the address into **opengraph.xyz** to see exactly what LinkedIn will show.
- Add the link to: LinkedIn (Featured section, and Contact info → Website), your email signature, the header of both CVs, and your business card.
- Optional: **search.google.com/search-console** → add property → verify → submit `sitemap.xml`. Google finds the site anyway, this just makes it faster.

---

## Changing the site later

**Small text edits, by yourself:** open your live site and add `#edit` to the address — `https://YOUR-USERNAME.github.io/reem-portfolio/#edit`. The editing toolbar appears: click any text to change it, use *Contact, CV & QR* for your details, then **Save page**. Your browser downloads a new `index.html`; upload it to the repository, replacing the old one. Ordinary visitors never see the edit button.

**Anything bigger:** send me the artifact link and say what you want changed. I rebuild this folder and you upload the new files.

**Keeping the two copies in step:** the Claude artifact and this GitHub copy are now separate. Editing one does not change the other. Ask me to rebuild whenever you want them identical again.

---

## Two things left empty on purpose

- **No phone number.** A number on a public page is harvested by scrapers within weeks and comes back as spam and WhatsApp scams. It belongs on the CV you send to someone who asked for it.
- **No CV file.** A public PDF carries your contact details into Google's index permanently. If you want one later, make a public version with email and LinkedIn only — no phone, no address — and add it through *Edit page → Contact, CV & QR*.

Both are decisions, not gaps.
