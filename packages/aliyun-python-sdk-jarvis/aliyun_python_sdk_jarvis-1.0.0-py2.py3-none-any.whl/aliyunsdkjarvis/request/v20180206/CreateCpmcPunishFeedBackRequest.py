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

class CreateCpmcPunishFeedBackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'CreateCpmcPunishFeedBack')
		self.set_method('POST')

	def get_SrcIP(self): # String
		return self.get_query_params().get('SrcIP')

	def set_SrcIP(self, SrcIP):  # String
		self.add_query_param('SrcIP', SrcIP)
	def get_DstPort(self): # Integer
		return self.get_query_params().get('DstPort')

	def set_DstPort(self, DstPort):  # Integer
		self.add_query_param('DstPort', DstPort)
	def get_ProtocolName(self): # String
		return self.get_query_params().get('ProtocolName')

	def set_ProtocolName(self, ProtocolName):  # String
		self.add_query_param('ProtocolName', ProtocolName)
	def get_PunishType(self): # String
		return self.get_query_params().get('PunishType')

	def set_PunishType(self, PunishType):  # String
		self.add_query_param('PunishType', PunishType)
	def get_SourceCode(self): # String
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self, SourceCode):  # String
		self.add_query_param('SourceCode', SourceCode)
	def get_FeedBack(self): # Integer
		return self.get_query_params().get('FeedBack')

	def set_FeedBack(self, FeedBack):  # Integer
		self.add_query_param('FeedBack', FeedBack)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_DstIP(self): # String
		return self.get_query_params().get('DstIP')

	def set_DstIP(self, DstIP):  # String
		self.add_query_param('DstIP', DstIP)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_GmtCreate(self): # String
		return self.get_query_params().get('GmtCreate')

	def set_GmtCreate(self, GmtCreate):  # String
		self.add_query_param('GmtCreate', GmtCreate)
	def get_SrcPort(self): # Integer
		return self.get_query_params().get('SrcPort')

	def set_SrcPort(self, SrcPort):  # Integer
		self.add_query_param('SrcPort', SrcPort)
