def get_sit_up_with_weights():

    settings = {
        'FEEDBACK_ID_MAP': {0: {}}
    }

    return settings


def get_dumbbell_fly():

    settings = {
        'FEEDBACK_ID_MAP': {0: {}}
    }

    return settings


def get_barbell_curl():

    settings = {
        'FEEDBACK_ID_MAP': {0: {}}
    }

    return settings


def get_dumbbell_lateral_raise():

    _ANGLE_ELBOW_HIP_SHLDR = {
        'NORMAL': (0,  10),
        'TRANS': (11, 39),
        'PASS': (40, 50)
    }

    settings = {

        'REF_ANGLE': _ANGLE_ELBOW_HIP_SHLDR,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 45,
        'KNEE_THRESH': [50, 70, 95],

        'OFFSET_THRESH': 55.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50,

        'FEEDBACK_ID_MAP': {
            0: {'msg': 'LOWER YOUR HIPS',
                'pos': (30, 80),
                'text_color': (0, 0, 0),
                'text_color_bg': (255, 255, 0)},
            1: {'msg': 'KNEE FALLING OVER TOE',
                'pos': (30, 170),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)},
            2: {'msg': 'SQUAT TOO DEEP',
                'pos': (30, 125),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)}
        }

    }

    return settings


def get_seated_tricep_press():
    
    _ANGLE_wrist_shldr_elbow = {
        'NORMAL': (155,  180),
        'TRANS': (130, 156),
        'PASS': (70, 131)
    }
    
    settings = {

        'REF_ANGLE': _ANGLE_wrist_shldr_elbow,

        'SHLDR_THRESH': [30,150],
        'HIP_THRESH': 15,

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50,

        'FEEDBACK_ID_MAP': {
            0: {'msg': 'Keep your arms near your ears',
                'pos': (30, 80),
                'text_color': (0, 0, 0),
                'text_color_bg': (255, 255, 0)},
            1: {'msg': 'Keep your body stright',
                'pos': (30, 170),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)},
        }

    }

    return settings


def get_bent_over_two_arm_dumbbell_row():

    _ANGLE_elbow_hip_shldr = {
        'NORMAL': (30,  55),
        'TRANS': (10, 30),
        'PASS': (0, 10)
    }

    settings = {

        'REF_ANGLE': _ANGLE_elbow_hip_shldr,

        'SHLDR_THRESH': 145,
        'ANKLE_THRESH': 45,
        'HIP_THRESH': 50,

        'OFFSET_THRESH': 70.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50,

        'FEEDBACK_ID_MAP': {
            0: {'msg': 'LOWER YOUR BACK',
                'pos': (30, 80),
                'text_color': (0, 0, 0),
                'text_color_bg': (255, 255, 0)},
            1: {'msg': 'KNEE FALLING OVER TOE',
                'pos': (30, 170),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)},
            2: {'msg': 'STRAIGHTEN YOUR BACK',
                'pos': (30, 200),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)}
        }

    }

    return settings


def get_squat_with_weights():

    _ANGLE_HIP_KNEE_VERT = {
        'NORMAL': (0,  32),
        'TRANS': (35, 65),
        'PASS': (70, 95)
    }

    settings = {

        'REF_ANGLE': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 45,
        'KNEE_THRESH': [50, 70, 95],

        'OFFSET_THRESH': 55.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50,

        'FEEDBACK_ID_MAP': {
            0: {'msg': 'LOWER YOUR HIPS',
                'pos': (30, 80),
                'text_color': (0, 0, 0),
                'text_color_bg': (255, 255, 0)},
            1: {'msg': 'KNEE FALLING OVER TOE',
                'pos': (30, 170),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)},
            2: {'msg': 'SQUAT TOO DEEP',
                'pos': (30, 125),
                'text_color': (255, 255, 230),
                'text_color_bg': (255, 80, 80)}
        }

    }

    return settings
