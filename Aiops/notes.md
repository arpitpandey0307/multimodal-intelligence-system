***Topic: Automated Batch Pipelines with Apache Spark***

1. Design Principles: 
	->Idempotency: output doesn't change on giving the same input n number of times
	->Schema Drift & Schema Enforcement: accepts only the accepted format and reject the other format
	->Deterministic Reproducibiilty: if we execute something today and after a fixed interval of time, output remains same

2. Batch Processing V/S Streaming Processing: 
	batch processing is on static data , streaming has real time data
	latency: delay takes minutes or hours in batch processing, delay takes milliseconds to seconds in streaming
	tools in batch processing: apache spark, sql, airflow
	tools in streaming: kafka, flink, spark streaming 
	use case: daily retraining in batch processing, real time credit card fraud detection in streaming
	high efficiency(batch), low efficiency(streaming)
	cons of batch: no backtracking
	pros of streaming: fast

***Topic: Automated Batch Pipelines with Apache Spark***

1. Design Principles: 
	->Idempotency: output doesn't change on giving the same input n number of times
	->Schema Drift & Schema Enforcement: accepts only the accepted format and reject the other format
	->Deterministic Reproducibiilty: if we execute something today and after a fixed interval of time, output remains same

2. Batch Processing V/S Streaming Processing: 
	batch processing is on static data , streaming has real time data
	latency: delay takes minutes or hours in batch processing, delay takes milliseconds to seconds in streaming
	tools in batch processing: apache spark, sql, airflow
	tools in streaming: kafka, flink, spark streaming 
	use case: daily retraining in batch processing, real time credit card fraud detection in streaming
	high efficiency(batch), low efficiency(streaming)
	cons of batch: no backtracking
	pros of streaming: fast

APACHE SPARK: divides a single process into parts
functions: .filter()
	   .select()
	
	ARCHITECTURE:
                                     ---------------
                                     | Driver Node |
                                     ---------------
                                      /           \
                              Worker Node 1     Worker Node 2


Driver Node: The orchestrator and "brain" of the Spark application
Worker Node: parallel processing running independently

***Topic: Kafka Broker and Architecture***
                                     Rapido
                                        |
                                ---------------
                                |    Server   |
                                ---------------  
                                        |
      -----------------         ---------------
      |    User DB    |<--------|   Kafka     |
      -----------------         ---------------
                                   /         \
                                User         Rider 


Sending data to the cloud :
~ Producer (Who sends data(user/rider))
~ Topics (Where data is stored)

Reading data :
~ Consumers : who reads
~ offset : like bookmark, tracks upto where we have read

*** Parallel processing ***:-

-> Partitions: A partition is an ordered sequence of messages inside a Kafka topic.
-> Keys: A key is information attached to a Kafka message that can be used to decide which partition should receive that message.


Consumer Groups and Automatic load Balancing

->Team(Consumers) , Group.id=xyz

Streaming data Ingestion with Python & Kafka
--> Message serialization(Data packing)

-->Python dict to JSON
    JSON.dumps()
-->JSON to python dict
    JSON.loads()

Topic 2 -> Data Delivery Gaurantees

->At most once=>Try once

->Atleast once=>1 time or more than 1

->Exactly once=>1 time, strict mode

Apache Airflow Architecture & Core Orchestration
-Streaming->Kafka
-Orcestration->Airflow
			-->Webserver(UI)
			-->Sheduler(Alarm)
			-->DB
			-->Executer

created folder
created virtual environment
activate the ve
install apache airflow
run airflow standalone

DAG->Direacted Acyclic Graph

Operator
->Bash Operator
->Python operator -->Data processing