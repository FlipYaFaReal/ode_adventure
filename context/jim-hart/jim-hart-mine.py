"""Mine C:\\Code for verifiable project metrics.

Rules that keep the numbers honest:
  - vendored clones (any nested .git below the project root) are skipped whole
  - build/publish output, coverage reports and agent worktrees are skipped
  - only hand-written source extensions are counted; blank lines are not
"""
import os, json, subprocess, io, sys
from collections import Counter

ROOT = r"C:\Code"

SKIP_DIRS = {
    'node_modules', 'dist', 'dist-electron', '.git', 'bin', 'obj', '.next', 'out',
    'build', 'venv', '.venv', '__pycache__', 'coverage', 'packages', '.vs', 'target',
    '.angular', 'TestResults', '.nuxt', 'vendor', '.turbo', '.svelte-kit', 'Migrations',
    'release', 'releases', 'output', 'artifacts', 'worktrees', '.claude', 'publish',
    'test-publish', 'test-publish-output', 'win-unpacked', 'Debug', 'Release',
    '.gradle', '.idea', 'gradle', 'Properties',
}
SKIP_FILES = {
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'poetry.lock', 'Cargo.lock',
    'LICENSES.chromium.html',
}
# whole projects that are not Jim's work or are not projects at all
NOT_A_PROJECT = {
    'npgsql-temp',          # clone of the Npgsql library
    'Auth0Quickstart',      # vendor sample
    'sample import', 'test', 'voice_clips', 'memory-bank-backup', '.claude',
    'ode-adventure',
}
# Directories excluded by shape rather than by name, so no redacted name has to
# appear in this file: asset stores hold media, not source, and *-dists hold builds.
NOT_A_PROJECT_SUFFIX = ('Assets', '-dists', 'Desires')

CODE_EXT = {
    '.cs': 'C#', '.ts': 'TypeScript', '.tsx': 'TypeScript', '.js': 'JavaScript',
    '.jsx': 'JavaScript', '.mjs': 'JavaScript', '.cjs': 'JavaScript', '.py': 'Python',
    '.java': 'Java', '.sql': 'SQL', '.html': 'HTML', '.css': 'CSS', '.scss': 'CSS',
    '.vue': 'Vue', '.go': 'Go', '.rs': 'Rust', '.rb': 'Ruby', '.php': 'PHP',
    '.sh': 'Shell', '.ps1': 'PowerShell', '.razor': 'Razor', '.cshtml': 'Razor',
    '.glsl': 'GLSL', '.kt': 'Kotlin', '.swift': 'Swift', '.xaml': 'XAML',
}
SPEC_HINTS = ('prd', 'spec', 'plan', 'design', 'adr', 'requirement', 'architecture',
              'workboard', 'decision', 'roadmap', 'rfc', 'brief', 'handoff', 'milestone')


def run(args, cwd):
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                           encoding='utf-8', errors='ignore', timeout=120)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


OWNER = 'Jim Hart'


def owned_by_jim(path):
    """True when a nested repo is Jim's own sub-repo rather than a vendored clone."""
    log = run(['git', 'log', '--format=%an', '--all'], path)
    if not log or not log.strip():
        return True          # empty/unreadable nested repo - keep its files
    authors = {a.strip() for a in log.strip().split(chr(10)) if a.strip()}
    return OWNER in authors


def scan_fs(root):
    loc, files = Counter(), Counter()
    docs, vendored, nested = [], [], []
    for dirpath, dirnames, filenames in os.walk(root):
        # a nested .git below the root is either Jim's own sub-repo or a vendored
        # clone of someone else's code; authorship decides which
        if dirpath != root and '.git' in dirnames:
            if not owned_by_jim(dirpath):
                vendored.append(os.path.relpath(dirpath, root).replace(chr(92), '/'))
                dirnames[:] = []
                continue
            nested.append(os.path.relpath(dirpath, root).replace(chr(92), '/'))
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in filenames:
            if fn in SKIP_FILES or '.min.' in fn:
                continue
            ext = os.path.splitext(fn)[1].lower()
            fp = os.path.join(dirpath, fn)
            try:
                rel = os.path.relpath(fp, root).replace(chr(92), '/')
            except ValueError:
                continue
            if ext == '.md':
                docs.append(rel)
                continue
            lang = CODE_EXT.get(ext)
            if not lang:
                continue
            files[lang] += 1
            try:
                with io.open(fp, encoding='utf-8', errors='ignore') as f:
                    loc[lang] += sum(1 for line in f if line.strip())
            except Exception:
                pass
    specs = sorted(d for d in docs if any(h in d.lower() for h in SPEC_HINTS))
    return dict(loc_by_lang=dict(loc), files_by_lang=dict(files),
                total_loc=sum(loc.values()), total_source_files=sum(files.values()),
                md_count=len(docs), spec_doc_count=len(specs), spec_docs=specs[:50],
                all_md=sorted(docs)[:80], vendored_subtrees=vendored,
                nested_own_repos=nested)


def scan_git(path):
    # Count what is reachable from the checked-out branch, not --all: several repos
    # carry a couple of dozen dependabot branches whose commits would inflate the
    # totals and would drift every time refs are pruned.
    log = run(['git', 'log', '--format=%an|%ad', '--date=short'], path)
    if log is None:
        return None
    lines = [l for l in log.strip().split('\n') if l.strip()]
    if not lines:
        return dict(commits=0)
    dates, authors = [], Counter()
    for l in lines:
        p = l.split('|')
        if len(p) >= 2:
            authors[p[0]] += 1
            dates.append(p[1])
    dates.sort()
    status = run(['git', 'status', '--porcelain'], path) or ''
    subj = run(['git', 'log', '-1', '--format=%s'], path) or ''
    first_subj = run(['git', 'log', '--reverse', '--format=%s'], path) or ''
    allrefs = run(['git', 'rev-list', '--count', '--all'], path) or ''
    return dict(commits=len(lines), first_commit=dates[0], last_commit=dates[-1],
                commits_all_refs=int(allrefs.strip() or 0),
                active_days=len(set(dates)), authors=dict(authors),
                uncommitted_files=len([s for s in status.split('\n') if s.strip()]),
                last_commit_subject=subj.strip(),
                first_commit_subject=first_subj.split('\n')[0].strip())


results = {}
for name in sorted(os.listdir(ROOT)):
    p = os.path.join(ROOT, name)
    if not os.path.isdir(p) or name in NOT_A_PROJECT or name.startswith('.'):
        continue
    if name.endswith(NOT_A_PROJECT_SUFFIX):
        continue
    sys.stderr.write(name + '\n')
    sys.stderr.flush()
    entry = dict(name=name, has_git=os.path.isdir(os.path.join(p, '.git')))
    entry['git'] = scan_git(p) if entry['has_git'] else None
    entry['fs'] = scan_fs(p)
    results[name] = entry

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mined2.json')
with io.open(out, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=1)
print('wrote', out, len(results), 'projects')
