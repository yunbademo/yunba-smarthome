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
./turn_on_living_light.sh 1 60
./turn_off_living_light.sh
./open_front_door.sh
./close_front_door.sh
```

