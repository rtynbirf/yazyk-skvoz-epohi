#!/usr/bin/env bash
# ============================================================
# ПУШ ДОМА НА GITHUB — токен живёт только в памяти одной команды.
# НИКОГДА не вставляй токен в чат и в URL: он уходит в GitHub
# напрямую из переменной окружения и нигде не сохраняется.
#
# Использование (на своей машине, в корне репозитория):
#   GITHUB_REPO=username/repo GITHUB_TOKEN=<свежий токен> bash scripts/push_to_github.sh
#
# Требования к токену (fine-grained):
#   Repository access: только нужный репозиторий
#   Permissions: Contents = Read and write, Metadata = Read-only
# ============================================================
set -euo pipefail

: "${GITHUB_REPO:?Укажи GITHUB_REPO=username/repo}"
: "${GITHUB_TOKEN:?Укажи GITHUB_TOKEN=<свежий fine-grained токен>}"

cd "$(dirname "$0")/.."

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo "Пуш: ветка ${BRANCH} -> github.com/${GITHUB_REPO}"

# credential.helper подаёт токен прямо в git через память процесса:
# он не появляется ни в argv команды push, ни в .git/config, ни в логах.
GIT_TERMINAL_PROMPT=0 git \
  -c credential.helper='!f(){ printf "username=x-access-token\npassword=%s\n" "$GITHUB_TOKEN"; };f' \
  push "https://github.com/${GITHUB_REPO}.git" "${BRANCH}:${BRANCH}" --tags

echo "Готово: ${BRANCH} отправлен в ${GITHUB_REPO}. Токен на диск не записан."
