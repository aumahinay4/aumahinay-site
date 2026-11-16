// Cloudflare timer for aumahinay.dev.
// GitHub often skips its own scheduled runs, so this Worker (Cloudflare's
// Cron Triggers are on time) starts the "Deploy to Cloudflare Pages" workflow.
// It passes timer=true, so the workflow publishes only when a new post or
// lesson is due; otherwise it stops without changing the site.
// Needs one secret: GH_TOKEN, a fine-grained GitHub token with
// "Actions: Read and write" on aumahinay4/aumahinay-site only.

const DISPATCH_URL =
  "https://api.github.com/repos/aumahinay4/aumahinay-site/actions/workflows/deploy.yml/dispatches";

async function startDeploy(env) {
  if (!env.GH_TOKEN) {
    console.log("GH_TOKEN secret is missing; nothing started.");
    return;
  }
  const res = await fetch(DISPATCH_URL, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.GH_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "aumahinay-timer",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ref: "main", inputs: { timer: true } }),
  });
  // GitHub answers 204 (or 200) when the run was started.
  if (res.ok) {
    console.log("Deploy workflow started.");
  } else {
    // Throwing marks this cron run as failed in the Cloudflare dashboard.
    throw new Error(`GitHub said ${res.status}: ${await res.text()}`);
  }
}

export default {
  async scheduled(controller, env, ctx) {
    ctx.waitUntil(startDeploy(env));
  },
};
