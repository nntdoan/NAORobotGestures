# Choregraphe bezier export in Python.
# RUN or WALK

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.00329923, [3, -0.213333, 0], [3, 0.106667, 0]], [0.00329923, [3, -0.106667, 0], [3, 0.106667, 0]], [0.00329923, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00329923, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.00329923, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00329923, [3, -0.0933333, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[-0.106465, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.106465, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.106465, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.106465, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.106465, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.106465, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.106465, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.106465, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LAnklePitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.09, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.09, [3, -0.213333, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.09, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.09, [3, -0.0933333, 0], [3, 0.2, 0]], [0.09, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LAnkleRoll")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.13, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.13, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.13, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.13, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.13, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.13, [3, -0.2, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[-0.416784, [3, -0.0133333, 0], [3, 0.213333, 0]], [-1.32914, [3, -0.213333, 0.235826], [3, 0.106667, -0.117913]], [-1.478, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.32914, [3, -0.106667, 0], [3, 0.0933333, 0]], [-1.478, [3, -0.0933333, 0], [3, 0.106667, 0]], [-1.32914, [3, -0.106667, 0], [3, 0.0933333, 0]], [-1.478, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.416785, [3, -0.2, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[-1.20209, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.149058, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.253073, [3, -0.106667, 0], [3, 0.106667, 0]], [0.149058, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.253073, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.149058, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.253073, [3, -0.0933333, 0.143304], [3, 0.2, -0.307079]], [-1.20209, [3, -0.2, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.3, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.0177417, [3, -0.213333, 0.0331044], [3, 0.106667, -0.0165522]], [0.00118951, [3, -0.106667, 0], [3, 0.106667, 0]], [0.0177417, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00118951, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.0177417, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00118951, [3, -0.0933333, 0], [3, 0.2, 0]], [0.3, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LHipPitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.13, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.13, [3, -0.213333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.2, 0]], [0.13, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LHipRoll")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.1, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.1, [3, -0.213333, 0], [3, 0.106667, 0]], [0.1, [3, -0.106667, 0], [3, 0.106667, 0]], [0.1, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.1, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.1, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.1, [3, -0.0933333, 0], [3, 0.2, 0]], [0.1, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LHipYawPitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.17, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.17, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.17, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.17, [3, -0.2, 0], [3, 0, 0]]])

# names.append("LKneePitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.09, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.09, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.09, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.09, [3, -0.2, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[1.44376, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.982792, [3, -0.213333, 0.250666], [3, 0.106667, -0.125333]], [0.315758, [3, -0.106667, 0], [3, 0.106667, 0]], [0.982791, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.315758, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.982791, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.315758, [3, -0.0933333, 0], [3, 0.2, 0]], [1.44376, [3, -0.2, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.224076, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.388359, [3, -0.213333, 0], [3, 0.106667, 0]], [0.314056, [3, -0.106667, 0], [3, 0.106667, 0]], [0.388358, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.314056, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.388358, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.314056, [3, -0.0933333, 0.0174239], [3, 0.2, -0.037337]], [0.224076, [3, -0.2, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.1, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.984099, [3, -0.213333, 0.283634], [3, 0.106667, -0.141817]], [-1.17635, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.984099, [3, -0.106667, 0], [3, 0.0933333, 0]], [-1.17635, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.984099, [3, -0.106667, 0], [3, 0.0933333, 0]], [-1.17635, [3, -0.0933333, 0], [3, 0.2, 0]], [0.1, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RAnklePitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.09, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.09, [3, -0.213333, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.09, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.09, [3, -0.0933333, 0], [3, 0.2, 0]], [0.09, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RAnkleRoll")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.13, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.13, [3, -0.213333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.2, 0]], [0.13, [3, -0.2, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.416784, [3, -0.0133333, 0], [3, 0.213333, 0]], [1.30147, [3, -0.213333, -0.126243], [3, 0.106667, 0.0631216]], [1.36459, [3, -0.106667, 0], [3, 0.106667, 0]], [1.30147, [3, -0.106667, 0], [3, 0.0933333, 0]], [1.36459, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.30147, [3, -0.106667, 0], [3, 0.0933333, 0]], [1.36459, [3, -0.0933333, 0], [3, 0.2, 0]], [0.416785, [3, -0.2, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[1.20209, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.331613, [3, -0.213333, 0], [3, 0.106667, 0]], [0.410152, [3, -0.106667, 0], [3, 0.106667, 0]], [0.331613, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.410152, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.331613, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.410152, [3, -0.0933333, -0.0785398], [3, 0.2, 0.1683]], [1.20209, [3, -0.2, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.3, [3, -0.0133333, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.106667, 0]], [0.00698725, [3, -0.106667, 0], [3, 0.106667, 0]], [0, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00698725, [3, -0.0933333, 0], [3, 0.106667, 0]], [0, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.00698725, [3, -0.0933333, -0.00698725], [3, 0.2, 0.0149727]], [0.3, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RHipPitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[0.13, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.13, [3, -0.213333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.13, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.13, [3, -0.0933333, 0], [3, 0.2, 0]], [0.13, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RHipRoll")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.1, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.1, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.1, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.1, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.1, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.1, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.1, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.1, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RHipYawPitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.17, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.17, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.17, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.17, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.17, [3, -0.2, 0], [3, 0, 0]]])

# names.append("RKneePitch")
# times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
# keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.09, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.09, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.09, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.09, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.09, [3, -0.2, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[1.44376, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.221891, [3, -0.213333, 0], [3, 0.106667, 0]], [1.56465, [3, -0.106667, 0], [3, 0.106667, 0]], [0.221891, [3, -0.106667, 0], [3, 0.0933333, 0]], [1.56465, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.221891, [3, -0.106667, 0], [3, 0.0933333, 0]], [1.56465, [3, -0.0933333, 0], [3, 0.2, 0]], [1.44376, [3, -0.2, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[-0.224076, [3, -0.0133333, 0], [3, 0.213333, 0]], [-0.137752, [3, -0.213333, 0], [3, 0.106667, 0]], [-0.279197, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.137752, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.279197, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.137752, [3, -0.106667, 0], [3, 0.0933333, 0]], [-0.279197, [3, -0.0933333, 0], [3, 0.2, 0]], [-0.224076, [3, -0.2, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.04, 0.68, 1, 1.32, 1.6, 1.92, 2.2, 2.8])
keys.append([[0.1, [3, -0.0133333, 0], [3, 0.213333, 0]], [1.04022, [3, -0.213333, 0], [3, 0.106667, 0]], [0.493928, [3, -0.106667, 0], [3, 0.106667, 0]], [1.04022, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.493928, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.04022, [3, -0.106667, 0], [3, 0.0933333, 0]], [0.493928, [3, -0.0933333, 0.0997199], [3, 0.2, -0.213685]], [0.1, [3, -0.2, 0], [3, 0, 0]]])

