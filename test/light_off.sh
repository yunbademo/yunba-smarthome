if [ $# != 1 ] ; then
  echo usage: `basename ${0}` name
  exit 1
fi

msg="{\\\"act\\\":\\\"light_off\\\", \\\"name\\\":\\\"${1}\\\"}"

#echo "${msg}"
./publish.sh "${msg}"

