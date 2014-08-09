#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases some **Colour** package colour fitting related examples.
"""

import numpy as np

import colour

# Fitting measured *ColorChecker* colour rendition chart data to a reference one.
reference = np.array(
    [[0.172906, 0.08205715, 0.05711951],
     [0.5680735, 0.29250361, 0.21942],
     [0.10437166, 0.19656122, 0.32946697],
     [0.10089156, 0.14839029, 0.05324779],
     [0.22306044, 0.21697008, 0.43151034],
     [0.10718115, 0.51351274, 0.41399101],
     [0.7464409, 0.20020391, 0.03077999],
     [0.05948985, 0.10659048, 0.39884205],
     [0.56735781, 0.08485298, 0.11940265],
     [0.11178198, 0.04285385, 0.14161263],
     [0.34254479, 0.50627811, 0.0557158],
     [0.79268226, 0.35803827, 0.02544159],
     [0.01865226, 0.05139666, 0.28876921],
     [0.05440562, 0.29876767, 0.07183236],
     [0.45631278, 0.03075616, 0.0408993],
     [0.85385852, 0.56503529, 0.01470045],
     [0.53537579, 0.09006281, 0.30467248],
     [-0.03661893, 0.24753827, 0.39810356],
     [0.91186287, 0.91497635, 0.8939137],
     [0.5797986, 0.592032, 0.59346914],
     [0.3549918, 0.36538033, 0.36757315],
     [0.19011528, 0.19180135, 0.19309001],
     [0.08525591, 0.08890588, 0.09252104],
     [0.03039192, 0.03118624, 0.03278316]])

measured = np.array(
    [[0.1557955891, 0.09715754539, 0.07514556497],
     [0.3911314011, 0.2594341934, 0.2126670778],
     [0.1282482147, 0.1846356988, 0.3150802255],
     [0.1202897355, 0.1345565915, 0.0740839988],
     [0.1936898828, 0.2115894556, 0.3795596361],
     [0.199574247, 0.3608543873, 0.4067812264],
     [0.4889660478, 0.2069168836, 0.05816533044],
     [0.09775521606, 0.1671069264, 0.4714772403],
     [0.3935864866, 0.1223340034, 0.1052642539],
     [0.1078033224, 0.07258529216, 0.1615147293],
     [0.2750267088, 0.3470545411, 0.09728099406],
     [0.439804405, 0.2688055933, 0.05430532619],
     [0.05887211859, 0.1112627164, 0.3855246902],
     [0.1270582527, 0.2578786016, 0.1356646419],
     [0.3561292887, 0.0793325752, 0.05118732154],
     [0.4813197553, 0.4208284318, 0.07120611519],
     [0.3466558456, 0.1517071426, 0.2496980429],
     [0.08261115849, 0.2458871603, 0.4870773256],
     [0.6605490446, 0.6594113708, 0.6637641191],
     [0.4805150926, 0.4787029624, 0.482300818],
     [0.3304535449, 0.3290418386, 0.3322888613],
     [0.1800130457, 0.1797856688, 0.1800441593],
     [0.102839753, 0.1042467952, 0.1038497463],
     [0.04742204025, 0.04772202671, 0.04914225638]])

print(colour.first_order_colour_fit(reference, measured))
