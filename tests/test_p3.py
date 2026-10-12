from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
CANDIDATES = ROOT / "candidates"


def load_function(path):
    spec = importlib.util.spec_from_file_location(
        f"candidate_{path.stem}", path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.first_item


def main():
    files = sorted(CANDIDATES.glob("**/P3_*.py"))
    results = []

    print("P3 — Postcondition vs. Edge Case")
    print("=" * 90)

    for path in files:
        name = str(path.relative_to(ROOT))

        try:
            function = load_function(path)

            # The non-empty input tests the behavior both requirements share.
            nonempty_pass = (
                function(["apple", "banana"]) == "apple"
            )

            # The postcondition requires "" for an empty list.
            postcondition_pass = function([]) == ""

            # The edge-case requirement requires None for an empty list.
            edge_case_pass = function([]) is None

            results.append(
                (nonempty_pass, postcondition_pass, edge_case_pass)
            )

            print(f"\n{name}")
            print(
                "  First item for non-empty list: "
                f"{'PASS' if nonempty_pass else 'FAIL'}"
            )
            print(
                "  Postcondition (empty list -> ''): "
                f"{'PASS' if postcondition_pass else 'FAIL'}"
            )
            print(
                "  Edge case (empty list -> None): "
                f"{'PASS' if edge_case_pass else 'FAIL'}"
            )

        except Exception as error:
            print(f"\n{name}")
            print(f"  ERROR: {type(error).__name__}: {error}")

    total = len(results)

    print("\n" + "=" * 90)
    print(f"Candidates tested successfully: {total}")
    print(
        "First item for non-empty list passed: "
        f"{sum(r[0] for r in results)}/{total}"
    )
    print(
        "Postcondition passed: "
        f"{sum(r[1] for r in results)}/{total}"
    )
    print(
        "Edge case passed: "
        f"{sum(r[2] for r in results)}/{total}"
    )


if __name__ == "__main__":
    main()
