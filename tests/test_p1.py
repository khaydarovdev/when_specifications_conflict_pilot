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

    return module.absolute_value


def test_postcondition(function):
    cases = [(-4, 4), (4, 4), (0, 0)]
    return all(function(n) == expected for n, expected in cases)


def test_example(function):
    return function(-4) == -4


def main():
    files = sorted(CANDIDATES.glob("**/*.py"))
    results = []

    print("P1 — Postcondition vs. Example")
    print("-" * 100)
    print(f"{'Candidate':48} {'Postcondition':15} {'Example':10} {'Output for -4'}")
    print("-" * 100)

    for path in files:
        name = str(path.relative_to(ROOT))

        try:
            function = load_function(path)
            post_pass = test_postcondition(function)
            example_pass = test_example(function)
            output = repr(function(-4))

            results.append((post_pass, example_pass))
            print(
                f"{name:48} "
                f"{'PASS' if post_pass else 'FAIL':15} "
                f"{'PASS' if example_pass else 'FAIL':10} "
                f"{output}"
            )
        except Exception as error:
            print(f"{name:48} ERROR: {type(error).__name__}: {error}")

    print("-" * 100)
    print(f"Candidates tested successfully: {len(results)}")
    print(f"Postcondition passed: {sum(r[0] for r in results)}/{len(results)}")
    print(f"Conflicting example passed: {sum(r[1] for r in results)}/{len(results)}")


if __name__ == "__main__":
    main()
