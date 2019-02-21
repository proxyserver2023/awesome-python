#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Subprocess.Popen: cloning stdout and stderr both to terminal and variables


import subprocess


def run_command(
        command,
        cwd = None
):
    p = subprocess.Popen(
        command,
        cwd=cwd,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    outs, errs = p.communicate()
    rc = p.returncode
    outs = outs.decode('utf-8')
    errs = errs.decode('utf-8')
