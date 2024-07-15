from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

# Set up authentication credentials
auth_provider = PlainTextAuthProvider(username='dev', password='Dev123!@#')

# Connect to the Cassandra cluster
cluster = Cluster(['172.16.4.14'], port=9042, auth_provider=auth_provider)
session = cluster.connect()

# Perform operations on the Cassandra cluster
# ...

# Close the connection
session.shutdown()
cluster.shutdown()
