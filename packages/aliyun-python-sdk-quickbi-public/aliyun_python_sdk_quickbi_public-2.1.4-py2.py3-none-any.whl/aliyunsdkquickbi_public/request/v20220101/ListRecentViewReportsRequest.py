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

class ListRecentViewReportsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'ListRecentViewReports','2.2.0')
		self.set_method('POST')

	def get_OffsetDay(self): # Integer
		return self.get_query_params().get('OffsetDay')

	def set_OffsetDay(self, OffsetDay):  # Integer
		self.add_query_param('OffsetDay', OffsetDay)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_QueryMode(self): # String
		return self.get_query_params().get('QueryMode')

	def set_QueryMode(self, QueryMode):  # String
		self.add_query_param('QueryMode', QueryMode)
	def get_TreeType(self): # String
		return self.get_query_params().get('TreeType')

	def set_TreeType(self, TreeType):  # String
		self.add_query_param('TreeType', TreeType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
