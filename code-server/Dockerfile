FROM ubuntu:24.04

# Базовые переменные окружения
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LANG en_US.UTF-8
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Базовые зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common \
        curl \
        sudo \
        libpq-dev \
        bash \
        python3-full \
        wget \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        llvm \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
    && dpkg-reconfigure -f noninteractive tzdata

# Установка Python версий
RUN for version in 3.11.11 3.12.3 3.13.0; do \
    wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz && \
    tar -xzf Python-${version}.tgz && \
    cd Python-${version} && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-${version} Python-${version}.tgz; \
    done

# Локализация
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# Создаем виртуальное окружение
RUN python3 -m venv /opt/venv

# Устанавливаем UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Устанавливаем npm и yarn
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install --global yarn

# Устанавливаем code-server
ARG VERSION=4.93.1
RUN wget https://github.com/coder/code-server/releases/download/v${VERSION}/code-server_${VERSION}_amd64.deb && \
    dpkg -i code-server_${VERSION}_amd64.deb && \
    rm code-server_${VERSION}_amd64.deb

# Создаем пользователя
RUN useradd -m -s /bin/bash code-server-user

# Устанавливаем рабочую директорию
WORKDIR /home/code-server-user

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости через uv
RUN uv sync --frozen --no-cache

# Открываем порты
EXPOSE 8080 5173 8000

# Переключаемся на пользователя
USER code-server-user

# Запускаем code-server
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
