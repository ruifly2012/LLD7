# -*- coding: utf-8 -*-
class STAT_GAMECOUNT_INFO_DICT_TYPE(dict):
	""" 玩家每日游戏局数信息在内存中数据结构的重定义 """

	def __init__(self):
		dict.__init__(self)

	def asDict(self):
		data = []
		for v in self.values():
			data.append(v)
		return {'values': data}

	def createFromDict(self, dictData):
		values = dictData['values']
		for game_round_info in values:
			self[(game_round_info['date'], game_round_info['type'])] = dict(game_round_info)
		return self


class STAT_GAMECOUNT_INFO_DICT_PICKLER(object):

	def __init__(self):
		pass

	# 此接口被C++底层调用
	# 引擎将数据交给脚本层管理，脚本层可以将这个字典重定义为任意类型
	# createObjFromDict被调用后，返回的数据将直接赋值到脚本中的变量
	def createObjFromDict(self, dct):
		return STAT_GAMECOUNT_INFO_DICT_TYPE().createFromDict(dct)

	# 此接口被C++底层调用
	# 底层需要从脚本层中获取数据，脚本层此时应该将数据结构还原为固定字典
	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, STAT_GAMECOUNT_INFO_DICT_TYPE)


inst = STAT_GAMECOUNT_INFO_DICT_PICKLER()
