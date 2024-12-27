#!/usr/bin/env python3
#
# wp-profile.py - Set profile of [default] device from command-line
#
# Currently the script outputs command to be ran, instead of runnig it.
#
# This script is based on post of ironhouzi at LinuxMusicians forum on topic
# Fedora Pipewire Low Latency Audio Configuration Reference Guide V.1.02
# https://linuxmusicians.com/viewtopic.php?p=171612#p171612
#

import json, sys, subprocess, re

#DEVICE_ID=$(wpctl inspect @DEFAULT_AUDIO_SINK@ | \
#    grep "device.id" | \
#    awk -F'"' '{gsub(/"/, "", $NF); print $2}')

devid = re.search(
    r'"([0-9]+)"',
    subprocess.run(
        "wpctl inspect @DEFAULT_AUDIO_SINK@ | grep \"device.id\"",
        shell=True,
        check=True, capture_output=True).stdout.decode('utf-8')).group(0)
#print(devid)

#DEVICE_STATE=$(pw-dump ${DEVICE_ID})

state = subprocess.run(
    'pw-dump ' + devid,
    shell=True,
    check=True, capture_output=True).stdout.decode('utf-8')
#print(state)

state_parsed = json.loads(state)
#print(repr(state_parsed))
#print(json.dumps(state_parsed, indent=4))

#for d in state_parsed:
#    if d["type"].endswith("Device"):
##        print('-----------------------')
##        print(d)
#        props = d['info']['props']
#        print('hw:' + str(props['alsa.card']) + " " + props['alsa.card_name'])

#sys.exit(0)

dev, = (d for d in state_parsed if d["type"].endswith("Device"))

print()
props = dev['info']['props']
print("Default audio device is hw:" + str(props['alsa.card']) +
      " \"" + props['alsa.card_name'] + "\"")
print()

#dev, = (d for d in json.load(sys.stdin) if d["type"].endswith("Device"))

print("\"" + props['alsa.card_name'] + "\" profiles:")
print()

for p in dev["info"]["params"]["EnumProfile"]:
#    print(p)
    print(str(p['index']) + ': [' + p['name'] + "] \"" + p['description'] + "\"")
    print("  priority: " + str(p['priority']))
#    print("  classes: " + str(p['classes']))

profile, = (p for p in dev["info"]["params"]["EnumProfile"] if p["name"] == "pro-audio")

print()
#print("To set pro-audio profile of default audio device run:")
#print()
print("Executing: wpctl set-profile", dev["id"], profile["index"])
#print("wpctl set-profile", dev["id"], profile["index"])
print()

state = subprocess.run(
    "wpctl set-profile " + str(dev["id"]) + " " +  str(profile["index"]),
    shell=True,
    check=True, capture_output=True).stdout.decode('utf-8')
