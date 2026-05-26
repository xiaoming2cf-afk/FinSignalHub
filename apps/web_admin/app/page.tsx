const statuses = [
  {
    label: "API",
    value: "Health only",
    note: "FastAPI scaffold boundary"
  },
  {
    label: "MCP",
    value: "Server info",
    note: "Tools disabled in Stage 01"
  },
  {
    label: "Compose",
    value: "Configured",
    note: "Runtime checks remain gated"
  }
];

export default function Home() {
  return (
    <main className="page">
      <section className="shell" aria-labelledby="stage-title">
        <p className="eyebrow">FinSignalHub Stage 01</p>
        <h1 id="stage-title">Repo Scaffold</h1>
        <p className="summary">
          Inspect-only shell for the Research Mode-first evidence-stream plugin.
          Business workflows remain disabled until later approved stages.
        </p>
        <div className="status-grid" aria-label="Scaffold status">
          {statuses.map((item) => (
            <div className="status-item" key={item.label}>
              <p className="status-label">{item.label}</p>
              <p className="status-value">{item.value}</p>
              <p className="status-note">{item.note}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}

