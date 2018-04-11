# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ProfileSetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'ProfileSet','cms')

	def get_EnableInstallAgentNewECS(self):
		return self.get_query_params().get('EnableInstallAgentNewECS')

	def set_EnableInstallAgentNewECS(self,EnableInstallAgentNewECS):
		self.add_query_param('EnableInstallAgentNewECS',EnableInstallAgentNewECS)

	def get_EnableActiveAlert(self):
		return self.get_query_params().get('EnableActiveAlert')

	def set_EnableActiveAlert(self,EnableActiveAlert):
		self.add_query_param('EnableActiveAlert',EnableActiveAlert)

	def get_AutoInstall(self):
		return self.get_query_params().get('AutoInstall')

	def set_AutoInstall(self,AutoInstall):
		self.add_query_param('AutoInstall',AutoInstall)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)