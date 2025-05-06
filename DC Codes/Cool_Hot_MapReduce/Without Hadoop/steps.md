How to Run This Without Hadoop
	1.	Make sure the scripts are executable:

chmod +x mapper.py reducer.py


	2.	Run the mapper and reducer scripts using a pipe:

cat sample.txt | python3 mapper.py | python3 reducer.py
