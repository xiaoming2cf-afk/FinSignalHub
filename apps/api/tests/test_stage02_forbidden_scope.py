from pathlib import Path


FORBIDDEN_TERMS = [
    "openalex",
    "crossref",
    "semantic scholar",
    "arxiv",
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
    runtime_files = [
        path
        for path in (root / "apps").rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and "tests" not in path.parts
        and path.suffix in {".py", ".ts", ".tsx", ".js", ".mjs"}
    ]

    haystack = "\n".join(path.read_text(encoding="utf-8").lower() for path in runtime_files)
    assert not any(term in haystack for term in FORBIDDEN_TERMS)
