# Choregraphe bezier export in Python.
# emphasis

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.6, 1, 1.6])
keys.append([[-0.413643, [3, -0.2, 0], [3, 0.133333, 0]], [-0.00698132, [3, -0.133333, 0], [3, 0.2, 0]], [-0.113446, [3, -0.2, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.6, 1])
keys.append([[0, [3, -0.2, 0], [3, 0.133333, 0]], [-0.106465, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LAnklePitch")
# times.append([0.6, 1])
# keys.append([[0.09, [3, -0.2, 0], [3, 0.133333, 0]], [0.09, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LAnkleRoll")
# times.append([0.6, 1])
# keys.append([[-0.13, [3, -0.2, 0], [3, 0.133333, 0]], [-0.13, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.6, 1])
keys.append([[-0.410388, [3, -0.2, 0], [3, 0.133333, 0]], [-0.410388, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.6, 1])
keys.append([[-1.1937, [3, -0.2, 0], [3, 0.133333, 0]], [-1.1937, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.6, 1])
keys.append([[0.3, [3, -0.2, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LHipPitch")
# times.append([0.6, 1])
# keys.append([[0.13, [3, -0.2, 0], [3, 0.133333, 0]], [0.13, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LHipRoll")
# times.append([0.6, 1])
# keys.append([[0.1, [3, -0.2, 0], [3, 0.133333, 0]], [0.1, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LHipYawPitch")
# times.append([0.6, 1])
# keys.append([[-0.17, [3, -0.2, 0], [3, 0.133333, 0]], [-0.17, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("LKneePitch")
# times.append([0.6, 1])
# keys.append([[-0.09, [3, -0.2, 0], [3, 0.133333, 0]], [-0.09, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.6, 1])
keys.append([[1.47236, [3, -0.2, 0], [3, 0.133333, 0]], [1.47236, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.6, 1])
keys.append([[0.185419, [3, -0.2, 0], [3, 0.133333, 0]], [0.185419, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.6, 1])
keys.append([[0.1, [3, -0.2, 0], [3, 0.133333, 0]], [0.1, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RAnklePitch")
# times.append([0.6, 1])
# keys.append([[0.09, [3, -0.2, 0], [3, 0.133333, 0]], [0.09, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RAnkleRoll")
# times.append([0.6, 1])
# keys.append([[0.13, [3, -0.2, 0], [3, 0.133333, 0]], [0.13, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.6, 1])
keys.append([[0.410388, [3, -0.2, 0], [3, 0.133333, 0]], [0.410388, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.6, 1])
keys.append([[1.1937, [3, -0.2, 0], [3, 0.133333, 0]], [1.1937, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.6, 1])
keys.append([[0.3, [3, -0.2, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RHipPitch")
# times.append([0.6, 1])
# keys.append([[0.13, [3, -0.2, 0], [3, 0.133333, 0]], [0.13, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RHipRoll")
# times.append([0.6, 1])
# keys.append([[-0.1, [3, -0.2, 0], [3, 0.133333, 0]], [-0.1, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RHipYawPitch")
# times.append([0.6, 1])
# keys.append([[-0.17, [3, -0.2, 0], [3, 0.133333, 0]], [-0.17, [3, -0.133333, 0], [3, 0, 0]]])

# names.append("RKneePitch")
# times.append([0.6, 1])
# keys.append([[-0.09, [3, -0.2, 0], [3, 0.133333, 0]], [-0.09, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.6, 1])
keys.append([[1.47236, [3, -0.2, 0], [3, 0.133333, 0]], [1.47236, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.6, 1])
keys.append([[-0.185419, [3, -0.2, 0], [3, 0.133333, 0]], [-0.185419, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.6, 1])
keys.append([[0.1, [3, -0.2, 0], [3, 0.133333, 0]], [0.1, [3, -0.133333, 0], [3, 0, 0]]])
