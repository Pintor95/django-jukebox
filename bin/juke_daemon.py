#!/usr/bin/env python
"""
Starts the audio daemon server.
"""
import sys
import os
# Setup the Django environment
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# Back to the ordinary imports
from django.conf import settings
from twisted.internet import reactor
from apps.juke_daemon import daemon

print "Starting jukebox daemon..."
daemon.start_daemon_loop()
print "django_jukebox daemon shutdown."