# Integration Checklist

Before each integration session:

- Pull latest changes.
- Run Python tests.
- Confirm strategy encoding has not changed.
- Confirm world dimensions and boundary rules.
- Disable mutation for deterministic hardware comparisons.
- Use a fixed seed for generated worlds.

During integration:

- Test the smallest world first.
- Compare one generation before many generations.
- Log input frame, output frame, and metrics.
- Measure transfer and compute time separately.
- Capture failures as reproducible test cases.

After integration:

- Commit known-good examples.
- Update docs if interfaces changed.
- Record fallback status.
- Assign owners to failures.
- Preserve demo artifacts.

