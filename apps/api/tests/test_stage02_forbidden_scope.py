from pathlib import Path


STAGE03_CONNECTOR_PROVIDER_TERMS = [
    "openalex",
    "crossref",
    "semantic scholar",
    "arxiv",
]

FORBIDDEN_BEHAVIOR_TERMS = [
    "llm adapter",
    "evidence extraction pipeline",
    "claim graph computation",
    "research delta computation",
    "mcp business tool",
    "stock prediction",
    "investment advice",
    "chatbot ui",
    "generic rag",
    "risk mode",
    "replay engine",
]


def test_no_stage03_plus_runtime_files_exist() -> None:
    root = Path(__file__).resolve().parents[3]
    connector_runtime_dir = root / "apps" / "api" / "finsignalhub_api" / "connectors"
    runtime_files = [
        path
        for path in (root / "apps").rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and "tests" not in path.parts
        and path.suffix in {".py", ".ts", ".tsx", ".js", ".mjs"}
    ]

    behavior_haystack = "\n".join(path.read_text(encoding="utf-8").lower() for path in runtime_files)
    assert not any(term in behavior_haystack for term in FORBIDDEN_BEHAVIOR_TERMS)

    provider_files = [
        path
        for path in runtime_files
        if connector_runtime_dir not in path.parents and path != connector_runtime_dir
    ]
    provider_haystack = "\n".join(path.read_text(encoding="utf-8").lower() for path in provider_files)
    assert not any(term in provider_haystack for term in STAGE03_CONNECTOR_PROVIDER_TERMS)
