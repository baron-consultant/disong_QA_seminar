"""Inspect or enable Pages using the existing Git credential helper.

Credentials are kept in memory and are never printed or written to files.
"""
import argparse
import json
import os
import subprocess
import urllib.error
import urllib.request

REPO = 'baron-consultant/disong_QA_seminar'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['inspect', 'enable', 'status'])
    args = parser.parse_args()
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    proc = subprocess.run(
        ['git', 'credential', 'fill'],
        input='protocol=https\nhost=github.com\n\n',
        capture_output=True, text=True, env=env, timeout=30,
    )
    values = dict(line.split('=', 1) for line in proc.stdout.splitlines() if '=' in line)
    token = values.get('password')
    if not token:
        print('No existing non-interactive GitHub credential. Local work is ready; authentication is required for publishing.')
        return 2

    def api(path, method='GET', body=None):
        request = urllib.request.Request(
            'https://api.github.com' + path,
            data=json.dumps(body).encode() if body is not None else None,
            method=method,
            headers={'Authorization': 'Bearer ' + token,
                     'Accept': 'application/vnd.github+json',
                     'Content-Type': 'application/json',
                     'User-Agent': 'seminar-pages-setup'},
        )
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read()
                return json.loads(data) if data else {}
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            try:
                message = json.loads(error.read()).get('message', '')
            except (ValueError, UnicodeError):
                message = ''
            print(f'GitHub API {method} {path}: HTTP {error.code}; {message}')
            raise SystemExit(3)

    if args.action == 'inspect':
        user = api('/user')
        repo = api('/repos/' + REPO)
        print(json.dumps({'login': user.get('login') if user else None,
                          'user_id': user.get('id') if user else None,
                          'repo': {k: repo.get(k) for k in ['full_name', 'private', 'default_branch', 'permissions', 'has_pages']} if repo else None}, ensure_ascii=False))
        return 0
    pages = api('/repos/' + REPO + '/pages')
    if args.action == 'enable' and pages is None:
        pages = api('/repos/' + REPO + '/pages', 'POST', {'source': {'branch': 'main', 'path': '/'}})
    print(json.dumps({k: pages.get(k) for k in ['html_url', 'status', 'source', 'build_type']} if pages else {'pages': 'not enabled'}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
