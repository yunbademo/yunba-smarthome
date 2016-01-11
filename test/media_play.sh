if [ $# != 1 ] ; then
  echo usage: `basename ${0}` path
  exit 1
fi

msg="{\\\"act\\\":\\\"media_play\\\", \\\"path\\\":\\\"${1}\\\"}"

#echo "${msg}"
./publish.sh "${msg}"

