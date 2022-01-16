#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R

def quaternion_to_euler_zyx(q):
    r = R.from_quat([q[0], q[1], q[2], q[3]])
    return r.as_euler('zyx', degrees=True)

if __name__ == "__main__":
    q = [0.0, 0.0, 0.7833, 0.6216]
    e = quaternion_to_euler_zyx(q)
    print("yaw : " + str(e[0]) + " ,pitch : " + str(e[1]) + " ,roll : " + str(e[2]))