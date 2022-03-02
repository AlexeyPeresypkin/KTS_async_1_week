export PYTHONPATH=.
python3 server.py &
sleep 1
server_process="$(jobs -p)"
python3 client.py
kill "$server_process"
