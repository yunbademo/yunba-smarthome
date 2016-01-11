# yunba-smarthome

## setup

```bash
sudo chmod a+x setup_env.sh
sudo ./setup_env.sh
```

## run
Edit config.py to change APPKEY, ALIAS, SECKEY, etc. then run:
```bash
sudo python main.py
```

## test
Each test script has different arguments, if the number of arguments is not correct, the usage will be printed.
```bash
cd test
chmod a+x *.sh

./door_open.sh 
./door_close.sh 
./light_off.sh living
./light_off.sh porch
./light_off.sh bedroom
./light_on.sh porch 1 100
./light_on.sh living 1 100
./light_on.sh bedroom 1 100
```

