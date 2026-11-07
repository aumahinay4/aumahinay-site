// Heart, Like, Follow and Share counts for blog posts and tutorial lessons (Cloudflare Pages Function).
// Heart, Like and Share are counted per page; Follow is one count for the whole site.
// Share counts every tap of the Share button (it is not an on/off button).
// Lives at https://aumahinay.dev/api/likes. Needs a Workers KV namespace bound
// to the Pages project as LIKES (Settings > Bindings). Without it, the Heart and
// Like buttons simply stay hidden on the site (Share still works).
//
//   GET  /api/likes?page=/blog/<slug>/&v=<visitor id>
//        -> {"heart": {"count": 3, "on": false}, "like": {"count": 5, "on": true},
//            "follow": {"count": 12, "on": false}, "share": {"count": 2}}
//   POST /api/likes  {"page": "...", "v": "...", "kind": "heart"|"like"|"follow", "on": true|false}
//   POST /api/likes  {"page": "...", "v": "...", "kind": "share"}   (adds one share)
//        -> same answer
//
// Each browser gets a random visitor id (kept in its own storage), so one
// browser counts once per button per page. Nobody signs in and no names or emails are kept.

const PAGE = /^\/(blog|tutorials)\/[a-z0-9-]+\/$/;
const VISITOR = /^[a-f0-9]{32}$/;
const KINDS = ["heart", "like", "follow"];  // on/off buttons, one per browser
const TAPS = ["share"];                      // every tap counts
const SITE_WIDE = { follow: true };  // one follower count for the whole site, whatever page it is tapped on
// Starting numbers shown on every post and lesson; real taps are added on top.
// Only the shown number changes: what is saved on Cloudflare stays the real taps.
const START = { heart: 100, like: 60 };

function withStart(now) {
  const shown = { ...now };
  for (const k of Object.keys(START)) shown[k] = { ...now[k], count: now[k].count + START[k] };
  return shown;
}

function answer(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });
}

// only real, published posts and lessons count: they are listed in the sitemap
async function isRealPage(env, request, page) {
  if (!PAGE.test(page)) return false;
  const res = await env.ASSETS.fetch(new URL("/sitemap.xml", request.url));
  return res.ok && (await res.text()).includes(`${page}</loc>`);
}

async function one(env, kind, page, v) {
  if (SITE_WIDE[kind]) page = "site";
  const [count, mine] = await Promise.all([
    env.LIKES.get(`count:${kind}:${page}`),
    v ? env.LIKES.get(`on:${kind}:${page}:${v}`) : null,
  ]);
  return { count: Math.max(0, parseInt(count || "0", 10)), on: mine !== null };
}

async function state(env, page, v) {
  const [heart, like, follow, share] = await Promise.all([
    ...KINDS.map((k) => one(env, k, page, v)),
    env.LIKES.get(`count:share:${page}`),
  ]);
  return { heart, like, follow, share: { count: Math.max(0, parseInt(share || "0", 10)) } };
}

export async function onRequest({ request, env }) {
  if (!env.LIKES) return answer({ error: "likes are not switched on" }, 503);
  let page, v, kind, on;
  if (request.method === "GET") {
    const q = new URL(request.url).searchParams;
    page = q.get("page") || "";
    v = q.get("v") || "";
  } else if (request.method === "POST") {
    let data;
    try { data = await request.json(); } catch { return answer({ error: "bad request" }, 400); }
    page = String(data.page || "");
    v = String(data.v || "");
    kind = String(data.kind || "");
    on = data.on === true;
    if (!(KINDS.includes(kind) || TAPS.includes(kind)) || !v) return answer({ error: "bad request" }, 400);
  } else {
    return answer({ error: "method not allowed" }, 405);
  }
  if (v && !VISITOR.test(v)) return answer({ error: "bad visitor id" }, 400);
  if (!(await isRealPage(env, request, page))) return answer({ error: "unknown page" }, 404);

  const now = await state(env, page, v);
  if (request.method === "POST" && TAPS.includes(kind)) {
    const count = now[kind].count + 1;
    await env.LIKES.put(`count:${kind}:${page}`, String(count));
    now[kind] = { count };
  } else if (request.method === "POST" && on !== now[kind].on) {
    const count = Math.max(0, now[kind].count + (on ? 1 : -1));
    const where = SITE_WIDE[kind] ? "site" : page;
    const key = `on:${kind}:${where}:${v}`;
    await Promise.all([
      on ? env.LIKES.put(key, "1") : env.LIKES.delete(key),
      env.LIKES.put(`count:${kind}:${where}`, String(count)),
    ]);
    now[kind] = { count, on };
  }
  return answer(withStart(now));
}
