const BASE = "https://raw.githubusercontent.com/TGL-SCRIPTER/faceless-shorts-automation/main/";
const PATHS = {
  control: "TASKS/automation_control.json",
  assignments: "TASKS/daily_assignments.json",
  status: "TASKS/task_status.json",
  publishing: "TASKS/publishing_policy.json"
};
export async function onRequestGet() {
  try {
    const entries = await Promise.all(Object.entries(PATHS).map(async ([key, path]) => {
      const response = await fetch(BASE + path, { headers: { "Accept": "application/json" } });
      if (!response.ok) throw new Error("Could not read " + path + " (" + response.status + ")");
      return [key, await response.json()];
    }));
    return Response.json({ ok: true, source: "github-main", updatedAt: new Date().toISOString(), data: Object.fromEntries(entries) }, {
      headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" }
    });
  } catch (error) {
    return Response.json({ ok: false, error: "Unable to load workflow data." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
