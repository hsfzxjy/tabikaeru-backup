# Backup Photos for TabiKaeru Game

![cover](./cover.png)

## Highlights

 + **Fast** Photos are compressed and transferred via LAN.
 + **Auto Detection for Duplicated Photos**
 + **No ROOT Required**

## Requirements

### Mobile

You need:

 + a terminal emulator (the script has been tested on [Termux](https://termux.com/), which is highly recommended)
 + to find out the location where the photos are stored. This variable is pre-configured as `/storage/emulated/0/Android/data/jp.co.hit_point.tabikaeru/Picture/`, but may varied across systems. If you have a different location, configure it by editting `tb-backup` file.

### Desktop

You need:

 + Python 3
 + a Linux-like environment

## How to use

 + Install python requirements on your **computer** by `pip install -r requirements.txt`.
 + Put `tb-backup` on your mobile. It's recommended to place it under **the home directory** of your terminal emulator, which can be obtained by executing `echo $HOME`.
 + Make sure your mobile and your computer are connected to **the same** WLAN.
 + Start up the FTP server on your **computer** by executing `./receive.py`.
 + Run the backup script `tb-backup` on your **mobile** by executing `bash tb-backup`.
 + If no error prompted, shut down the server on your **computer** by pressing `<Ctrl+C>`.
 + Process and archive newly uploaded photos by executing `./process.py`. The photos will be stored at `~/storage`, where `~` is the root directory of this repository. Duplicated photos will be automatically omitted.
