# Publish runs as a single job, version guard retained

The 2026-07-31 adversarial review of the v5 branch flagged publish.yml's shape as its one HIGH finding: a single tag-triggered job holds `id-token: write` while checking out the tag and running `uv build`, and PEP 517 makes building code execution inside the trusted-publishing boundary. The recommended fix was the standard split — a credential-free pack job that verifies, tests, builds, and uploads artifacts, and a publish job that only downloads and publishes.

The decision declines the split and keeps one job, adding a fail-fast guard that verifies the tag against both version declarations (`pyproject.toml` and `pangu.__version__`) before anything builds. Three reasons. First, the split never defends the front door: anyone able to push a `v*` tag ships a legitimate-looking release through either shape, and for a solo-maintainer repo the tag push is the realistic compromise path. Second, the threat the split does close — build-time code exfiltrating the short-lived, project-scoped OIDC token — is small here: the build backend is `uv_build`, and the marginal hardening is not worth two jobs plus an artifact handoff. Third, the guard covers the failure that actually happens: a mis-tag or version drift would publish a release PyPI never allows re-uploading, and the in-repo version-drift test cannot catch it because CI never runs on tag refs. pangu.js made the same decision the same day (its ADR 0014), so both repos publish through the same shape.

Alternatives rejected:

- The pack/publish split: maximum isolation, but ceremony against a threat the front door dwarfs.
- Adding a master-ancestry check on the tagged commit: deliberately omitted; release discipline is merge-then-tag, and the version guard already blocks the mis-tag consequences that matter.

## Consequences

- `uv build` (and the build backend it fetches per `[build-system].requires`) executes while the job can mint the PyPI OIDC token. Accepted for a solo maintainer; revisit if the repo gains a second committer.
- Tags are never tested by CI before publishing — only the version guard runs. Accepted: the tag is cut from a merged, CI-passed master by convention.
- Security reviews will flag this shape again; this ADR is the standing answer, to be re-litigated only with new facts.
