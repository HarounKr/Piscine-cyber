# Utilisez une image de base Debian
FROM debian:bullseye-slim

# Mettez à jour et installez Python 3
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]