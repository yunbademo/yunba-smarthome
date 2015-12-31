APPKEY="563c4afef085fc471efdf803"
ALIAS="pi_house"
SECKEY="sec-zxhrt0bbwTHkRBsj8b66VL1dbQ52IFKdkfnZzdI6Qli0zPIx"

data="{\"method\":\"publish_to_alias\", \"appkey\":\"${APPKEY}\", \"seckey\":\"${SECKEY}\", \"alias\":\"${ALIAS}\", \"msg\":\"${1}\"}"

echo ${data}
curl -l -H "Content-type: application/json" -X POST -d "${data}" http://rest.yunba.io:8080

echo

