# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class DeleteCpmcPunishRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'DeleteCpmcPunish')
		self.set_method('POST')

	def get_Reason(self): # String
		return self.get_query_params().get('Reason')

	def set_Reason(self, Reason):  # String
		self.add_query_param('Reason', Reason)
	def get_SrcIp(self): # String
		return self.get_query_params().get('SrcIp')

	def set_SrcIp(self, SrcIp):  # String
		self.add_query_param('SrcIp', SrcIp)
	def get_Evidence(self): # String
		return self.get_query_params().get('Evidence')

	def set_Evidence(self, Evidence):  # String
		self.add_query_param('Evidence', Evidence)
	def get_DetectId(self): # String
		return self.get_query_params().get('DetectId')

	def set_DetectId(self, DetectId):  # String
		self.add_query_param('DetectId', DetectId)
	def get_DstPort(self): # Integer
		return self.get_query_params().get('DstPort')

	def set_DstPort(self, DstPort):  # Integer
		self.add_query_param('DstPort', DstPort)
	def get_Rule(self): # String
		return self.get_query_params().get('Rule')

	def set_Rule(self, Rule):  # String
		self.add_query_param('Rule', Rule)
	def get_PunishType(self): # String
		return self.get_query_params().get('PunishType')

	def set_PunishType(self, PunishType):  # String
		self.add_query_param('PunishType', PunishType)
	def get_TriggerType(self): # String
		return self.get_query_params().get('TriggerType')

	def set_TriggerType(self, TriggerType):  # String
		self.add_query_param('TriggerType', TriggerType)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_SourceCode(self): # String
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self, SourceCode):  # String
		self.add_query_param('SourceCode', SourceCode)
	def get_SourceUid(self): # String
		return self.get_query_params().get('SourceUid')

	def set_SourceUid(self, SourceUid):  # String
		self.add_query_param('SourceUid', SourceUid)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_DstIp(self): # String
		return self.get_query_params().get('DstIp')

	def set_DstIp(self, DstIp):  # String
		self.add_query_param('DstIp', DstIp)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_OwnerAliUid(self): # String
		return self.get_query_params().get('OwnerAliUid')

	def set_OwnerAliUid(self, OwnerAliUid):  # String
		self.add_query_param('OwnerAliUid', OwnerAliUid)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_BanPath(self): # String
		return self.get_query_params().get('BanPath')

	def set_BanPath(self, BanPath):  # String
		self.add_query_param('BanPath', BanPath)
	def get_RegName(self): # String
		return self.get_query_params().get('RegName')

	def set_RegName(self, RegName):  # String
		self.add_query_param('RegName', RegName)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_TunnelId(self): # Integer
		return self.get_query_params().get('TunnelId')

	def set_TunnelId(self, TunnelId):  # Integer
		self.add_query_param('TunnelId', TunnelId)
	def get_SrcPort(self): # Integer
		return self.get_query_params().get('SrcPort')

	def set_SrcPort(self, SrcPort):  # Integer
		self.add_query_param('SrcPort', SrcPort)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
