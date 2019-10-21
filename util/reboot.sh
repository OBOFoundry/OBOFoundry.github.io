# kill whatever is on 25333
PID="$(lsof -t -i:25333)"
while [ "${PID}" !=  "" ];
do
	kill $PID
	# give it time to kill
	sleep 1
	# see if anything else is running
	PID="$(lsof -t -i:25333)"
done

# restart JVM
java -Xmx12G -jar build/robot.jar python &

# make sure it's up
PID="$(lsof -t -i:25333)"
while [ "${PID}" ==  "" ];
do
	sleep 1
	PID="$(lsof -t -i:25333)"
done

echo "JVM started on 25333 with PID ${PID}"