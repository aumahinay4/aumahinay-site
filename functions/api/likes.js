// Like counts for blog posts and tutorial lessons (Cloudflare Pages Function).
// Lives at https://aumahinay.dev/api/likes. Needs a Workers KV namespace bound
// to the Pages project as LIKES (Settings > Bindings). Without it, the heart
// button simply stays hidden on the site.
//
//   GET  /api/likes?page=/blog/<slug>/&v=<visitor id>  -> {"count": 3, "liked": false}
//   POST /api/likes  {"page": "...", "v": "...", "like": true|false}  -> same answer
//
// Each browser gets a random visitor id (kept in its own storage), so one
// browser counts once per page. Nobody signs in and no names or emails are kept.

const PAGE = /^\/(blog|tutorials)\/[a-z0-9-]+\/$/;
const VISITOR = /^[a-f0-9]{32}$/;

function answer(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });
}

// only real, published posts and lessons can be liked: they are listed in the sitemap
async function isRealPage(env, request, page) {
  if (!PAGE.test(page)) return false;
  const res = await env.ASSETS.fetch(new URL("/sitemap.xml", request.url));
  return res.ok && (await res.text()).includes(`${page}</loc>`);
}

async function state(env, page, v) {
  const [count, mine] = await Promise.all([
    env.LIKES.get("count:" + page),
    v ? env.LIKES.get(`liked:${page}:${v}`) : null,
  ]);
  return { count: Math.max(0, parseInt(count || "0", 10)), liked: mine !== null };
}

export async function onRequest({ request, env }) {
  if (!env.LIKES) return answer({ error: "likes are not switched on" }, 503);
  let page, v, like;
  if (request.method === "GET") {
    const q = new URL(request.url).searchParams;
    page = q.get("page") || "";
    v = q.get("v") || "";
  } else if (request.method === "POST") {
    let data;
    try { data = await request.json(); } catch { return answer({ error: "bad request" }, 400); }
    page = String(data.page || "");
    v = String(data.v || "");
    like = data.like === true;
  } else {
    return answer({ error: "method not allowed" }, 405);
  }
  if (v && !VISITOR.test(v)) return answer({ error: "bad visitor id" }, 400);
  if (!(await isRealPage(env, request, page))) return answer({ error: "unknown page" }, 404);

  const now = await state(env, page, v);
  if (request.method === "POST" && v && like !== now.liked) {
    const key = `liked:${page}:${v}`;
    const count = Math.max(0, now.count + (like ? 1 : -1));
    await Promise.all([
      like ? env.LIKES.put(key, "1") : env.LIKES.delete(key),
      env.LIKES.put("count:" + page, String(count)),
    ]);
    return answer({ count, liked: like });
  }
  return answer(now);
}
