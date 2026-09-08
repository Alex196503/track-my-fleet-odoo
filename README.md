
# Track my Fleet - Odoo MVP

### Summary
This setup delivers a containerized Odoo 17 fleet management module featuring a custom OWL dashboard that displays maintenance counts by status alongside a high-priority maintenance report table. It includes custom models and views built specifically for technician workflows, supported by automated server actions and scheduled cron jobs that trigger overdue email alerts.
For local development and testing the functionalities, the entire application containerization was configured in `docker-compose.yaml`.

### Setup & Access
1. Start the App:
   ```bash
   docker compose up -d --build
2. Access the Mailpit Web UI to view intercepted emails:
   - http://localhost:8025
3. Access the Odoo localhost app to test the functionalities:
   - http://localhost:8000

### Quick note
The mail setup uses Mailpit on port 1025 with no auth, strictly meant for local dev. If you deploy this to production, you'll need to configure a real SMTP server with proper credentials and TLS.

Author: **Moldovan Alex-Cristian**
