#!/usr/bin/env python

import glob
import os

addons = []

os.chdir("kube-addons/")
files = os.listdir(".")

for fle in files:
    if os.path.isdir(fle):
        addons.append(fle)

for addon in addons:
    manifests = glob.glob("%s/*" %addon)
    manifests.sort()
    for manifest in manifests:
        print("Creating %s" %manifest)
        os.popen("kubectl create -f %s" %manifest).read()
