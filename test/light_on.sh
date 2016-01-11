if [ $# != 3 ] ; then
  echo usage: `basename ${0}` name frequency duty_cycle
  exit 1
fi

msg="{\\\"act\\\":\\\"light_on\\\", \\\"name\\\":\\\"${1}\\\", \\\"freq\\\":${2}, \\\"dc\\\":${3}}"

#echo "${msg}"
./publish.sh "${msg}"

