#!/usr/bin/env python
import paho.mqtt.publish as publish

publish.single("rv2442JSR", "Hello JSR SOul here", hostname="mqtt.eclipseprojects.io")