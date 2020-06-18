# region [Imports]

import pprint

import random


# endregion [Imports]


# region [Constants]

# debug 0 = off
# debug 1 = extra printouts



# endregion [Constants]

# region [Debug]






# endregion [Debug]

# region [Class_Name]

class GiRandDataPope:

    # endregion [Class_Name]
    # region [ClassDocString]
    """$TM_CURRENT_LINE [TODO]

    [TODO]

    Arguments:
        $TM_CURRENT_LINE {[type]} -- [description]

    Returns:
        [type] -- [description]

    Yields:
        [type] -- [description]"""

    # endregion [ClassDocString]
    # region [Class_Init]
    def __init__(self):
        self.word_pool = ['greatly', 'electric', 'adjective', 'end', 'diagram', 'mill', 'deer', 'found', 'sunlight',
'rise', 'settle', 'support', 'completely', 'from', 'divide', 'production', 'satisfied', 'crop',
'broke', 'sleep', 'certainly', 'section', 'baseball', 'different', 'audience', 'choose', 'hearing',
'atom', 'top', 'living', 'promised', 'folks', 'doing', 'rise', 'joy', 'comfortable', 'father', 'view',
'farm', 'about', 'success', 'shore', 'successful', 'studying', 'noise', 'airplane', 'grow', 'package',
'pocket', 'blue', 'graph', 'matter', 'mine', 'load', 'bridge', 'citizen', 'floating', 'lips', 'those',
'clothes', 'iron', 'seeing', 'rich', 'cool', 'period', 'imagine', 'castle', 'development', 'gasoline', 'ask', 'cowboy',
'short', 'camp', 'somehow', 'press', 'including', 'chance', 'test', 'higher', 'few', 'slipped', 'clearly', 'paragraph', 'parts',
'bow', 'found', 'arrangement', 'share', 'men', 'light', 'handsome', 'at', 'alive', 'these', 'rich', 'there', 'say', 'college', 'what',
'current', 'cow', 'play', 'fix', 'mirror', 'pile', 'cause', 'screen', 'they', 'came', 'railroad', 'special', 'meat', 'square', 'pilot',
'accident', 'nobody', 'am', 'garden', 'combination', 'climate', 'select', 'now', 'forgot', 'blank', 'grow', 'smallest', 'how', 'trouble',
'longer', 'sheet', 'oxygen', 'run', 'chart', 'world', 'remember', 'sleep', 'safe', 'gently', 'recently', 'essential', 'wooden', 'two', 'basket',
'thee', 'fireplace', 'told', 'around', 'past', 'beneath', 'shade', 'mental', 'parts', 'influence', 'electric', 'provide', 'tone', 'when', 'enough',
'symbol', 'notice']

        self.num_pool = self.num_gen(30)
        self.letter_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    # endregion [Class_Init]
    # region [Class_Methods]

    def num_gen(self, amount):
        return [i for i in range(amount)]

    def randdict(self, pool_key, pool_value, key_amount, value_amount):
        _rand_dict = {}
        if pool_key == 'word': _key_list = random.sample(self.word_pool, k=key_amount)
        elif pool_key == 'num': _key_list = random.sample(self.num_pool, k=key_amount)
        elif pool_key == 'letter': _key_list = random.sample(self.letter_pool, k=key_amount)


        if pool_value == 'word': _value_list = self.word_pool
        elif pool_value == 'num': _value_list = self.num_pool
        elif pool_value == 'letter': _value_list = self.letter_pool

        for key in _key_list:
            if value_amount == 1:
                _rand_dict[key] = random.choice(_value_list)
            else:
                _rand_dict[key] = random.choices(_value_list, k=value_amount)
        return _rand_dict

    def randdict_of_dicts(self, pool_key_major, pool_key_minor, pool_list, key_amount_major, key_amount_minor, value_amount):
        _rand_dict = {}
        if pool_key_major == 'word': _key_list = random.sample(self.word_pool, k=key_amount_major)
        elif pool_key_major == 'num': _key_list = random.sample(self.num_pool, k=key_amount_major)
        elif pool_key_major == 'letter': _key_list = random.sample(self.letter_pool, k=key_amount_major)


        for key in _key_list:
            _rand_dict[key] = self.randdict(pool_key_minor, pool_list, key_amount_minor, value_amount)
        return _rand_dict




    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return 'placeholder'  #TODO

    def __str__(self):
        return 'placeholder' #TODO

    # endregion [Class_Dunder]





# region [Main]






























# endregion [Main]
