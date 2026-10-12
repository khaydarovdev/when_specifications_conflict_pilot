from pathlib import Path
import contextlib
import importlib.util
import io

ROOT = Path(__file__).resolve().parent.parent
CANDIDATES = ROOT / "candidates"


def load_function(path):
    spec = importlib.util.spec_from_file_location(
        f"candidate_{path.stem}", path
    )
    module = importlib.util.module_from_spec(spec)

    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)

    return module.sort_in_place


def test_candidate(function):
    original = [3, 1, 2]
    before = original.copy()

    returned = function(original)
    expected = sorted(before)

    postcondition_pass = (
        original == expected
        and returned is original
        and returned == expected
    )

    invariant_pass = original == before

    return postcondition_pass, invariant_pass, returned, original


def main():
    files = sorted(CANDIDATES.glob("**/P2_*.py"))
    results = []

    print("P2 — Postcondition vs. Invariant")
    print("=" * 110)

    for path in files:
        name = str(path.relative_to(ROOT))

        try:
            function = load_function(path)
            post, invariant, returned, original = test_candidate(function)

            results.append((post, invariant))

            print(f"\n{name}")
            print(f"  Postcondition: {'PASS' if post else 'FAIL'}")
            print(f"  Invariant:     {'PASS' if invariant else 'FAIL'}")
            print(f"  Returned:      {returned!r}")
            print(f"  Original list: {original!r}")

        except Exception as error:
            print(f"\n{name}")
            print(f"  ERROR: {type(error).__name__}: {error}")

    print("\n" + "=" * 110)
    print(f"Candidates tested successfully: {len(results)}")
    print(f"Postcondition passed: {sum(r[0] for r in results)}/{len(results)}")
    print(f"Invariant passed: {sum(r[1] for r in results)}/{len(results)}")


if __name__ == "__main__":
    main()
