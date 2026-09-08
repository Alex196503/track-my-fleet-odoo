FROM odoo:17.0
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY ./custom_addons/track_my_fleet /mnt/extra-addons/track_my_fleet
USER odoo
EXPOSE 8069
CMD ["odoo", "-d", "edu-myofficeinc75", "-u", "TrackMyFleet"]