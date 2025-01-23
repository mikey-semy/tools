#!/bin/bash

# Активируем виртуальное окружение
source /opt/venv/bin/activate

# Устанавливаем расширения VS Code если нужно
code-server --install-extension ms-python.python
code-server --install-extension ms-python.vscode-pylance

# Запускаем code-server
exec code-server \
  --host 0.0.0.0 \
  --port 8080 \
  --auth password \
  --user-data-dir /home/code-server-user/.local/share/code-server \
  --extensions-dir /home/code-server-user/.local/share/code-server/extensions
