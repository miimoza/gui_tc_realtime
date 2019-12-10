api="https://api-ratp.pierre-grimaud.fr/v3"

if [ "$1" = "--help" ]; then
    echo "allez nique bien fort ta mere"
    exit 0
fi

if [ $# -lt 3 ]; then
    echo "usage: ./skedul [mode] [line] [station] [direction]"
    echo " * mode     - 'b': bus, 'm': metro, 'r': rer, 't': tramway, 'n': noctilien]"
    echo " * line     - Line ID"
    echo " * station  - Station name, '-list':list all the stations of the line"
    echo " * direction- 'A', 'R', '-list':list A and R corespondance with station name"   
    exit 1
fi

if [ "$1" = "m" ]; then
    mode="metros"
elif [ "$1" = "b" ]; then
    mode="bus"
elif [ "$1" = "r" ]; then
    mode="rers"
elif [ "$1" = "t" ]; then
    mode="tramways"
elif [ "$1" = "n" ]; then
    mode="noctiliens"
else
    echo "usage: ./skedul [mode] [line] [station] [direction]"
    echo " * mode     - 'b': bus, 'm': metro, 'r': rer, 't': tramway, 'n': noctilien]"
    echo " * line     - Line ID"
    echo " * station  - Station name, '-list':list all the stations of the line"
    echo " * direction- 'A', 'R', '-list':list A and R corespondance with station name"

    exit 1
fi

line=$2

if [ "$3" = "-list" ]; then
    request_stations="$api/stations/$mode/$line"
    wget -O data_station $request_stations > /dev/null 2>&1
    nb_line=$(wc -l data_station | cut -d ' ' -f 1)
    nb_line=$((nb_line - 8))
    for i in $(seq 6 4 $nb_line); do
        head -$i data_station | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2
    done
    rm data_station
    exit 0
fi
station=$3
station=$(echo $station | sed 's/ /+/g')

if [ $# -lt 4 ]; then
    echo "usage: ./skedul [mode] [line] [station] [direction]"
    echo " * mode     - 'b': bus, 'm': metro, 'r': rer, 't': tramway, 'n': noctilien]"
    echo " * line     - Line ID"
    echo " * station  - Station name, '-list':list all the stations of the line"
    echo " * direction- 'A', 'R', '-list':list A and R corespondance with station name"

    exit 1
fi

if [ "$4" = "-list" ]; then
    request_stations="$api/destinations/$mode/$line"
    wget -O data_destination $request_stations > /dev/null 2>&1

    nb_line=$(wc -l data_destination | cut -d ' ' -f 1)
    nb_line=$((nb_line - 8))

    for i in $(seq 5 4 $nb_line); do
        head -$i data_destination | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2 | tr '\n' ' '
        head -$(($i + 1)) data_destination | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2
    done
    rm data_destination
    exit 0
fi

direction=$4

request_schedule="$api/schedules/$mode/$line/$station/$direction"
wget -O data_schedule $request_schedule > /dev/null 2>&1

if [ "$(cat data_schedule)" = "" ]; then
    echo "Request failed";
    echo ""
    echo "usage: ./skedul [mode] [line] [station] [destination]"
    echo " * mode        - 'b': bus, 'm': metro, 'r': rer, 't': tramway, 'n': noctilien]"
    echo " * line        - Line ID"
    echo " * station     - Station name, '-list':list all the stations of the line"
    echo " * destination - 'A', 'R', '-list':list A and R corespondance with station name"
fi


head -6 data_schedule | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2 | tr '\n' ' '
printf ': '
head -5 data_schedule | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2

head -10 data_schedule | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2 | tr '\n' ' '
printf ': '
head -9 data_schedule | tail -1 | cut -d ':' -f 2 | cut -d '"' -f 2
rm data_schedule
