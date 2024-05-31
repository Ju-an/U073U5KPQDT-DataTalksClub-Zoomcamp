# Setup

0. Install docker compose:

   ```
   curl -SL https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
   
   chmod +x ~/.docker/cli-plugins/docker-compose
   ```

1. Clone repo:

   ```
   git clone https://github.com/mage-ai/mlops.git
   ```

1. Change directory into the cloned repo:

   ```
   cd mlops
   ```

1. Launch Mage and the database service (PostgreSQL):

   ```
   ./scripts/start.sh
   ```

1. Open [`http://localhost:6789`](http://localhost:6789) in your browser.
