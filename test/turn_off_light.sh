dd="{\"method\":\"publish_to_alias\", \"appkey\":\"563c4afef085fc471efdf803\", \"seckey\":\"sec-zxhrt0bbwTHkRBsj8b66VL1dbQ52IFKdkfnZzdI6Qli0zPIx\", \"alias\":\"pi_house_shdxiang\", \"msg\":\"{\\\"act\\\":\\\"turn_off_${1}_light\\\"}\"}"
echo ${dd}
curl -l -H "Content-type: application/json" -X POST -d "${dd}" http://rest.yunba.io:8080
