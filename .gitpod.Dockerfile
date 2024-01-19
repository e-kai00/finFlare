FROM gitpod/workspace-full

# Install PostgreSQL
RUN sudo apt-get update && \
    sudo apt-get install -y postgresql-12 postgresql-client-12

# Initialize the database and enable automatic start
RUN sudo service postgresql start 12 && \
    sudo -u postgres createuser --superuser gitpod && \
    sudo -u postgres createdb gitpod