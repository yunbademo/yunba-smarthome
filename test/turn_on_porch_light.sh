if [ $# != 2 ] ; then
  echo usage: `basename ${0}` frequency duty_cycle
  exit 1
fi

msg="{\\\"act\\\":\\\"turn_on_porch_light\\\", \\\"freq\\\":${1}, \\\"dc\\\":${2}}"

#echo "${msg}"
./publish.sh "${msg}"

