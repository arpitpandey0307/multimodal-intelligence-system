

# cloud_config.py
kafka_config = {
    'bootstrap.servers': 'kafka-2bf89bd6-yourusername-f75f.a.aivencloud.com:10908',
    'security.protocol': 'SSL',
    
    # Use the full absolute paths to your files
    'ssl.ca.location': 'ca.pem',
    'ssl.certificate.location': 'service.cert',
    'ssl.key.location': 'service.key'
}
print("✅ Ready to connect to Aiven Cloud Kafka!")



