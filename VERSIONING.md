# GitHub Action Versioning and Release

This repository is published as a composite GitHub Action and can be used in other repositories through the `uses: <owner>/<repo>@<version>` construct.

## Versioning Scheme

Semantic versioning (SemVer) is used:
- MAJOR (X.y.z) — incompatible changes (breaking);
- MINOR (x.Y.z) — new features, backward compatible;
- PATCH (x.y.Z) — bug fixes, without changing public interface.

It's recommended to maintain "floating" tags to simplify pinning:
- `v1` — always points to the latest stable release within major version 1;
- optionally `v1.2` — latest release for specific minor branch.

Action consumers are recommended:
- for stability and build repeatability — pin to specific release tag: `@v1.2.3`;
- for getting fixes without API changes — pin to major tag: `@v1`;
- for maximum strict fixation — pin to commit SHA.

## How to Release a New Version

1. Merge changes into the `main` branch.
2. Create a new annotated tag with version:
   ```bash
   git tag -a v1.2.3 -m "Release v1.2.3"
   git push origin v1.2.3
   ```
3. Update the "floating" major tag (and minor tag if needed):
   ```bash
   # Move v1 tag to new release
   git tag -d v1 || true
   git push origin :refs/tags/v1 || true
   git tag -a v1 -m "Major tag for 1.x" v1.2.3
   git push origin v1

   # (Optional) update v1.2 tag
   git tag -d v1.2 || true
   git push origin :refs/tags/v1.2 || true
   git tag -a v1.2 -m "Minor tag for 1.2.x" v1.2.3
   git push origin v1.2
   ```
4. Create GitHub Release based on tag `v1.2.3` (optional, for release notes).

## Version Bump Rules

- Change Action input parameters (inputs) or behavior with breaking effect — bump MAJOR.
- Add new inputs/features without breaking old ones — bump MINOR.
- Fix bugs/texts/documentation — bump PATCH.

## What is Considered "Public Interface" of this Action

- File `action.yml` (names and default values of `inputs` and `outputs`).
- Expected Python version and dependency installation method.
- Semantics of returned artifacts/outputs (e.g., `summary_file`, `raw_output`).

## Tips for Users

- Include artifact upload and/or summary step following the documentation examples if using the Action directly.
- For simple execution without additional setup, you can use the provided reusable workflow `workflow_call`.

## Support

- Issues with `breaking-change` label are created in advance before MAJOR release.
- Deprecated parameters are marked in README with removal timeline (deprecation window) when possible.
