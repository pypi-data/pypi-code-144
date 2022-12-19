# coding: utf-8

from __future__ import absolute_import

# import ProjectManClient
from huaweicloudsdkprojectman.v4.projectman_client import ProjectManClient
from huaweicloudsdkprojectman.v4.projectman_async_client import ProjectManAsyncClient
# import models into sdk package
from huaweicloudsdkprojectman.v4.model.add_apply_join_project_for_agc_request import AddApplyJoinProjectForAgcRequest
from huaweicloudsdkprojectman.v4.model.add_apply_join_project_for_agc_response import AddApplyJoinProjectForAgcResponse
from huaweicloudsdkprojectman.v4.model.add_member_request_v4 import AddMemberRequestV4
from huaweicloudsdkprojectman.v4.model.add_member_v4_request import AddMemberV4Request
from huaweicloudsdkprojectman.v4.model.add_member_v4_response import AddMemberV4Response
from huaweicloudsdkprojectman.v4.model.associate_issue_detail import AssociateIssueDetail
from huaweicloudsdkprojectman.v4.model.associated_test_case import AssociatedTestCase
from huaweicloudsdkprojectman.v4.model.attach_wiki_detail import AttachWikiDetail
from huaweicloudsdkprojectman.v4.model.batch_add_member_request_v4 import BatchAddMemberRequestV4
from huaweicloudsdkprojectman.v4.model.batch_add_members_v4_request import BatchAddMembersV4Request
from huaweicloudsdkprojectman.v4.model.batch_add_members_v4_request_body import BatchAddMembersV4RequestBody
from huaweicloudsdkprojectman.v4.model.batch_add_members_v4_response import BatchAddMembersV4Response
from huaweicloudsdkprojectman.v4.model.batch_delelte_issues_request_v4 import BatchDelelteIssuesRequestV4
from huaweicloudsdkprojectman.v4.model.batch_delete_issues_v4_request import BatchDeleteIssuesV4Request
from huaweicloudsdkprojectman.v4.model.batch_delete_issues_v4_response import BatchDeleteIssuesV4Response
from huaweicloudsdkprojectman.v4.model.batch_delete_iterations_v4_request import BatchDeleteIterationsV4Request
from huaweicloudsdkprojectman.v4.model.batch_delete_iterations_v4_request_body import BatchDeleteIterationsV4RequestBody
from huaweicloudsdkprojectman.v4.model.batch_delete_iterations_v4_response import BatchDeleteIterationsV4Response
from huaweicloudsdkprojectman.v4.model.batch_delete_members_v4_request import BatchDeleteMembersV4Request
from huaweicloudsdkprojectman.v4.model.batch_delete_members_v4_request_body import BatchDeleteMembersV4RequestBody
from huaweicloudsdkprojectman.v4.model.batch_delete_members_v4_response import BatchDeleteMembersV4Response
from huaweicloudsdkprojectman.v4.model.batch_update_child_nick_names_request import BatchUpdateChildNickNamesRequest
from huaweicloudsdkprojectman.v4.model.batch_update_child_nick_names_response import BatchUpdateChildNickNamesResponse
from huaweicloudsdkprojectman.v4.model.batch_update_child_user_nick_names_request_body import BatchUpdateChildUserNickNamesRequestBody
from huaweicloudsdkprojectman.v4.model.bug_statistic_response_v4 import BugStatisticResponseV4
from huaweicloudsdkprojectman.v4.model.cancel_project_domain_request import CancelProjectDomainRequest
from huaweicloudsdkprojectman.v4.model.cancel_project_domain_response import CancelProjectDomainResponse
from huaweicloudsdkprojectman.v4.model.chart import Chart
from huaweicloudsdkprojectman.v4.model.check_project_name_request_v4 import CheckProjectNameRequestV4
from huaweicloudsdkprojectman.v4.model.check_project_name_v4_request import CheckProjectNameV4Request
from huaweicloudsdkprojectman.v4.model.check_project_name_v4_response import CheckProjectNameV4Response
from huaweicloudsdkprojectman.v4.model.comment_user_v4 import CommentUserV4
from huaweicloudsdkprojectman.v4.model.commit_record_detail import CommitRecordDetail
from huaweicloudsdkprojectman.v4.model.create_customfield_v1_req import CreateCustomfieldV1Req
from huaweicloudsdkprojectman.v4.model.create_customfields_request import CreateCustomfieldsRequest
from huaweicloudsdkprojectman.v4.model.create_customfields_response import CreateCustomfieldsResponse
from huaweicloudsdkprojectman.v4.model.create_issue_request_v4 import CreateIssueRequestV4
from huaweicloudsdkprojectman.v4.model.create_issue_response_v4_domain import CreateIssueResponseV4Domain
from huaweicloudsdkprojectman.v4.model.create_issue_response_v4_parent_issue import CreateIssueResponseV4ParentIssue
from huaweicloudsdkprojectman.v4.model.create_issue_response_v4_tracker import CreateIssueResponseV4Tracker
from huaweicloudsdkprojectman.v4.model.create_issue_v4_request import CreateIssueV4Request
from huaweicloudsdkprojectman.v4.model.create_issue_v4_response import CreateIssueV4Response
from huaweicloudsdkprojectman.v4.model.create_iteration_request_v4 import CreateIterationRequestV4
from huaweicloudsdkprojectman.v4.model.create_iteration_v4_request import CreateIterationV4Request
from huaweicloudsdkprojectman.v4.model.create_iteration_v4_response import CreateIterationV4Response
from huaweicloudsdkprojectman.v4.model.create_project_domain_request import CreateProjectDomainRequest
from huaweicloudsdkprojectman.v4.model.create_project_domain_request_body import CreateProjectDomainRequestBody
from huaweicloudsdkprojectman.v4.model.create_project_domain_response import CreateProjectDomainResponse
from huaweicloudsdkprojectman.v4.model.create_project_domain_response_body import CreateProjectDomainResponseBody
from huaweicloudsdkprojectman.v4.model.create_project_module_request import CreateProjectModuleRequest
from huaweicloudsdkprojectman.v4.model.create_project_module_request_body import CreateProjectModuleRequestBody
from huaweicloudsdkprojectman.v4.model.create_project_module_response import CreateProjectModuleResponse
from huaweicloudsdkprojectman.v4.model.create_project_v4_request import CreateProjectV4Request
from huaweicloudsdkprojectman.v4.model.create_project_v4_request_body import CreateProjectV4RequestBody
from huaweicloudsdkprojectman.v4.model.create_project_v4_response import CreateProjectV4Response
from huaweicloudsdkprojectman.v4.model.create_system_issue_request_v4 import CreateSystemIssueRequestV4
from huaweicloudsdkprojectman.v4.model.create_system_issue_v4_request import CreateSystemIssueV4Request
from huaweicloudsdkprojectman.v4.model.create_system_issue_v4_response import CreateSystemIssueV4Response
from huaweicloudsdkprojectman.v4.model.creator import Creator
from huaweicloudsdkprojectman.v4.model.custom_feild_record import CustomFeildRecord
from huaweicloudsdkprojectman.v4.model.custom_field import CustomField
from huaweicloudsdkprojectman.v4.model.delete_attachment_request import DeleteAttachmentRequest
from huaweicloudsdkprojectman.v4.model.delete_attachment_response import DeleteAttachmentResponse
from huaweicloudsdkprojectman.v4.model.delete_issue_v4_request import DeleteIssueV4Request
from huaweicloudsdkprojectman.v4.model.delete_issue_v4_response import DeleteIssueV4Response
from huaweicloudsdkprojectman.v4.model.delete_iteration_v4_request import DeleteIterationV4Request
from huaweicloudsdkprojectman.v4.model.delete_iteration_v4_response import DeleteIterationV4Response
from huaweicloudsdkprojectman.v4.model.delete_project_module_request import DeleteProjectModuleRequest
from huaweicloudsdkprojectman.v4.model.delete_project_module_response import DeleteProjectModuleResponse
from huaweicloudsdkprojectman.v4.model.delete_project_v4_request import DeleteProjectV4Request
from huaweicloudsdkprojectman.v4.model.delete_project_v4_response import DeleteProjectV4Response
from huaweicloudsdkprojectman.v4.model.demand_statistic_response_v4 import DemandStatisticResponseV4
from huaweicloudsdkprojectman.v4.model.download_attachment_request import DownloadAttachmentRequest
from huaweicloudsdkprojectman.v4.model.download_attachment_response import DownloadAttachmentResponse
from huaweicloudsdkprojectman.v4.model.download_image_file_request import DownloadImageFileRequest
from huaweicloudsdkprojectman.v4.model.download_image_file_response import DownloadImageFileResponse
from huaweicloudsdkprojectman.v4.model.get_project_info_v4_result_project import GetProjectInfoV4ResultProject
from huaweicloudsdkprojectman.v4.model.get_project_info_v4_result_project_creator import GetProjectInfoV4ResultProjectCreator
from huaweicloudsdkprojectman.v4.model.issue_accessory import IssueAccessory
from huaweicloudsdkprojectman.v4.model.issue_attr_history_record import IssueAttrHistoryRecord
from huaweicloudsdkprojectman.v4.model.issue_comment_v4 import IssueCommentV4
from huaweicloudsdkprojectman.v4.model.issue_completion_rate_response_v4 import IssueCompletionRateResponseV4
from huaweicloudsdkprojectman.v4.model.issue_completion_rate_v4_issue_completion_rates import IssueCompletionRateV4IssueCompletionRates
from huaweicloudsdkprojectman.v4.model.issue_completion_rate_v4_issue_status import IssueCompletionRateV4IssueStatus
from huaweicloudsdkprojectman.v4.model.issue_custom_field import IssueCustomField
from huaweicloudsdkprojectman.v4.model.issue_detail_custom_field import IssueDetailCustomField
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4 import IssueItemSfV4
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_domain import IssueItemSfV4Domain
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_iteration import IssueItemSfV4Iteration
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_module import IssueItemSfV4Module
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_priority import IssueItemSfV4Priority
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_severity import IssueItemSfV4Severity
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_status import IssueItemSfV4Status
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_story_point import IssueItemSfV4StoryPoint
from huaweicloudsdkprojectman.v4.model.issue_item_sf_v4_tracker import IssueItemSfV4Tracker
from huaweicloudsdkprojectman.v4.model.issue_order import IssueOrder
from huaweicloudsdkprojectman.v4.model.issue_project_response_v4 import IssueProjectResponseV4
from huaweicloudsdkprojectman.v4.model.issue_record_v4 import IssueRecordV4
from huaweicloudsdkprojectman.v4.model.issue_record_v4_details import IssueRecordV4Details
from huaweicloudsdkprojectman.v4.model.issue_record_v4_user import IssueRecordV4User
from huaweicloudsdkprojectman.v4.model.issue_request_v4 import IssueRequestV4
from huaweicloudsdkprojectman.v4.model.issue_response_v4 import IssueResponseV4
from huaweicloudsdkprojectman.v4.model.issue_status import IssueStatus
from huaweicloudsdkprojectman.v4.model.issue_status_response_v4 import IssueStatusResponseV4
from huaweicloudsdkprojectman.v4.model.issue_user import IssueUser
from huaweicloudsdkprojectman.v4.model.iteration_history import IterationHistory
from huaweicloudsdkprojectman.v4.model.iteration_history_details import IterationHistoryDetails
from huaweicloudsdkprojectman.v4.model.iteration_history_operator import IterationHistoryOperator
from huaweicloudsdkprojectman.v4.model.list_associated_issues_request import ListAssociatedIssuesRequest
from huaweicloudsdkprojectman.v4.model.list_associated_issues_response import ListAssociatedIssuesResponse
from huaweicloudsdkprojectman.v4.model.list_associated_test_cases_request import ListAssociatedTestCasesRequest
from huaweicloudsdkprojectman.v4.model.list_associated_test_cases_response import ListAssociatedTestCasesResponse
from huaweicloudsdkprojectman.v4.model.list_associated_wikis_request import ListAssociatedWikisRequest
from huaweicloudsdkprojectman.v4.model.list_associated_wikis_response import ListAssociatedWikisResponse
from huaweicloudsdkprojectman.v4.model.list_child_issues_v4_request import ListChildIssuesV4Request
from huaweicloudsdkprojectman.v4.model.list_child_issues_v4_response import ListChildIssuesV4Response
from huaweicloudsdkprojectman.v4.model.list_domain_not_added_projects_v4_request import ListDomainNotAddedProjectsV4Request
from huaweicloudsdkprojectman.v4.model.list_domain_not_added_projects_v4_response import ListDomainNotAddedProjectsV4Response
from huaweicloudsdkprojectman.v4.model.list_domain_not_added_projects_v4_response_body_creator import ListDomainNotAddedProjectsV4ResponseBodyCreator
from huaweicloudsdkprojectman.v4.model.list_domain_not_added_projects_v4_response_body_projects import ListDomainNotAddedProjectsV4ResponseBodyProjects
from huaweicloudsdkprojectman.v4.model.list_issue_associated_commits_request import ListIssueAssociatedCommitsRequest
from huaweicloudsdkprojectman.v4.model.list_issue_associated_commits_response import ListIssueAssociatedCommitsResponse
from huaweicloudsdkprojectman.v4.model.list_issue_comments_v4_request import ListIssueCommentsV4Request
from huaweicloudsdkprojectman.v4.model.list_issue_comments_v4_response import ListIssueCommentsV4Response
from huaweicloudsdkprojectman.v4.model.list_issue_custom_fields_request import ListIssueCustomFieldsRequest
from huaweicloudsdkprojectman.v4.model.list_issue_custom_fields_request_body import ListIssueCustomFieldsRequestBody
from huaweicloudsdkprojectman.v4.model.list_issue_custom_fields_response import ListIssueCustomFieldsResponse
from huaweicloudsdkprojectman.v4.model.list_issue_item_response import ListIssueItemResponse
from huaweicloudsdkprojectman.v4.model.list_issue_records_v4_request import ListIssueRecordsV4Request
from huaweicloudsdkprojectman.v4.model.list_issue_records_v4_response import ListIssueRecordsV4Response
from huaweicloudsdkprojectman.v4.model.list_issue_request_v4 import ListIssueRequestV4
from huaweicloudsdkprojectman.v4.model.list_issue_request_v4_custom_fields import ListIssueRequestV4CustomFields
from huaweicloudsdkprojectman.v4.model.list_issues_sf_v4_request import ListIssuesSfV4Request
from huaweicloudsdkprojectman.v4.model.list_issues_sf_v4_response import ListIssuesSfV4Response
from huaweicloudsdkprojectman.v4.model.list_issues_v4_request import ListIssuesV4Request
from huaweicloudsdkprojectman.v4.model.list_issues_v4_response import ListIssuesV4Response
from huaweicloudsdkprojectman.v4.model.list_iteration_histories_request import ListIterationHistoriesRequest
from huaweicloudsdkprojectman.v4.model.list_iteration_histories_response import ListIterationHistoriesResponse
from huaweicloudsdkprojectman.v4.model.list_project_bug_statics_v4_request import ListProjectBugStaticsV4Request
from huaweicloudsdkprojectman.v4.model.list_project_bug_statics_v4_response import ListProjectBugStaticsV4Response
from huaweicloudsdkprojectman.v4.model.list_project_demand_static_v4_request import ListProjectDemandStaticV4Request
from huaweicloudsdkprojectman.v4.model.list_project_demand_static_v4_response import ListProjectDemandStaticV4Response
from huaweicloudsdkprojectman.v4.model.list_project_domains_request import ListProjectDomainsRequest
from huaweicloudsdkprojectman.v4.model.list_project_domains_response import ListProjectDomainsResponse
from huaweicloudsdkprojectman.v4.model.list_project_issues_records_v4_request import ListProjectIssuesRecordsV4Request
from huaweicloudsdkprojectman.v4.model.list_project_issues_records_v4_response import ListProjectIssuesRecordsV4Response
from huaweicloudsdkprojectman.v4.model.list_project_iterations_v4_request import ListProjectIterationsV4Request
from huaweicloudsdkprojectman.v4.model.list_project_iterations_v4_response import ListProjectIterationsV4Response
from huaweicloudsdkprojectman.v4.model.list_project_members_v4_request import ListProjectMembersV4Request
from huaweicloudsdkprojectman.v4.model.list_project_members_v4_response import ListProjectMembersV4Response
from huaweicloudsdkprojectman.v4.model.list_project_modules_request import ListProjectModulesRequest
from huaweicloudsdkprojectman.v4.model.list_project_modules_response import ListProjectModulesResponse
from huaweicloudsdkprojectman.v4.model.list_project_versions_v4_response_body_iterations import ListProjectVersionsV4ResponseBodyIterations
from huaweicloudsdkprojectman.v4.model.list_project_work_hours_request import ListProjectWorkHoursRequest
from huaweicloudsdkprojectman.v4.model.list_project_work_hours_request_body import ListProjectWorkHoursRequestBody
from huaweicloudsdkprojectman.v4.model.list_project_work_hours_response import ListProjectWorkHoursResponse
from huaweicloudsdkprojectman.v4.model.list_projects_v4_request import ListProjectsV4Request
from huaweicloudsdkprojectman.v4.model.list_projects_v4_response import ListProjectsV4Response
from huaweicloudsdkprojectman.v4.model.list_projects_v4_response_body_creator import ListProjectsV4ResponseBodyCreator
from huaweicloudsdkprojectman.v4.model.list_projects_v4_response_body_projects import ListProjectsV4ResponseBodyProjects
from huaweicloudsdkprojectman.v4.model.list_scrum_project_statuses_request import ListScrumProjectStatusesRequest
from huaweicloudsdkprojectman.v4.model.list_scrum_project_statuses_response import ListScrumProjectStatusesResponse
from huaweicloudsdkprojectman.v4.model.list_status_statistic_request import ListStatusStatisticRequest
from huaweicloudsdkprojectman.v4.model.list_status_statistic_response import ListStatusStatisticResponse
from huaweicloudsdkprojectman.v4.model.list_workitem_status_records_v4_request import ListWorkitemStatusRecordsV4Request
from huaweicloudsdkprojectman.v4.model.list_workitem_status_records_v4_response import ListWorkitemStatusRecordsV4Response
from huaweicloudsdkprojectman.v4.model.list_workitems_request import ListWorkitemsRequest
from huaweicloudsdkprojectman.v4.model.list_workitems_response import ListWorkitemsResponse
from huaweicloudsdkprojectman.v4.model.member_list_v4_members import MemberListV4Members
from huaweicloudsdkprojectman.v4.model.metric_request2 import MetricRequest2
from huaweicloudsdkprojectman.v4.model.metric_request2_dividend import MetricRequest2Dividend
from huaweicloudsdkprojectman.v4.model.metric_request3 import MetricRequest3
from huaweicloudsdkprojectman.v4.model.metric_request3_dividend import MetricRequest3Dividend
from huaweicloudsdkprojectman.v4.model.metric_request_v2 import MetricRequestV2
from huaweicloudsdkprojectman.v4.model.metric_request_v2_dividend import MetricRequestV2Dividend
from huaweicloudsdkprojectman.v4.model.metric_request_v2_dividend_custom_fields import MetricRequestV2DividendCustomFields
from huaweicloudsdkprojectman.v4.model.module_owner import ModuleOwner
from huaweicloudsdkprojectman.v4.model.new_custom_field import NewCustomField
from huaweicloudsdkprojectman.v4.model.project_child_module import ProjectChildModule
from huaweicloudsdkprojectman.v4.model.project_module import ProjectModule
from huaweicloudsdkprojectman.v4.model.remove_project_request import RemoveProjectRequest
from huaweicloudsdkprojectman.v4.model.remove_project_response import RemoveProjectResponse
from huaweicloudsdkprojectman.v4.model.scrum_custom_field import ScrumCustomField
from huaweicloudsdkprojectman.v4.model.scrum_status_flow_direct_to_vo import ScrumStatusFlowDirectToVo
from huaweicloudsdkprojectman.v4.model.scrum_status_flow_vo import ScrumStatusFlowVo
from huaweicloudsdkprojectman.v4.model.show_bug_density_v2_request import ShowBugDensityV2Request
from huaweicloudsdkprojectman.v4.model.show_bug_density_v2_response import ShowBugDensityV2Response
from huaweicloudsdkprojectman.v4.model.show_bugs_per_developer_request import ShowBugsPerDeveloperRequest
from huaweicloudsdkprojectman.v4.model.show_bugs_per_developer_response import ShowBugsPerDeveloperResponse
from huaweicloudsdkprojectman.v4.model.show_completion_rate_request import ShowCompletionRateRequest
from huaweicloudsdkprojectman.v4.model.show_completion_rate_response import ShowCompletionRateResponse
from huaweicloudsdkprojectman.v4.model.show_cur_user_info_request import ShowCurUserInfoRequest
from huaweicloudsdkprojectman.v4.model.show_cur_user_info_response import ShowCurUserInfoResponse
from huaweicloudsdkprojectman.v4.model.show_cur_user_role_request import ShowCurUserRoleRequest
from huaweicloudsdkprojectman.v4.model.show_cur_user_role_response import ShowCurUserRoleResponse
from huaweicloudsdkprojectman.v4.model.show_issue_completion_rate_request import ShowIssueCompletionRateRequest
from huaweicloudsdkprojectman.v4.model.show_issue_completion_rate_response import ShowIssueCompletionRateResponse
from huaweicloudsdkprojectman.v4.model.show_issue_v4_request import ShowIssueV4Request
from huaweicloudsdkprojectman.v4.model.show_issue_v4_response import ShowIssueV4Response
from huaweicloudsdkprojectman.v4.model.show_issues_wrok_flow_config_request import ShowIssuesWrokFlowConfigRequest
from huaweicloudsdkprojectman.v4.model.show_issues_wrok_flow_config_response import ShowIssuesWrokFlowConfigResponse
from huaweicloudsdkprojectman.v4.model.show_iteration_v4_request import ShowIterationV4Request
from huaweicloudsdkprojectman.v4.model.show_iteration_v4_response import ShowIterationV4Response
from huaweicloudsdkprojectman.v4.model.show_project_info_v4_request import ShowProjectInfoV4Request
from huaweicloudsdkprojectman.v4.model.show_project_info_v4_response import ShowProjectInfoV4Response
from huaweicloudsdkprojectman.v4.model.show_project_summary_v4_request import ShowProjectSummaryV4Request
from huaweicloudsdkprojectman.v4.model.show_project_summary_v4_response import ShowProjectSummaryV4Response
from huaweicloudsdkprojectman.v4.model.show_project_work_hours_request import ShowProjectWorkHoursRequest
from huaweicloudsdkprojectman.v4.model.show_project_work_hours_request_body import ShowProjectWorkHoursRequestBody
from huaweicloudsdkprojectman.v4.model.show_project_work_hours_response import ShowProjectWorkHoursResponse
from huaweicloudsdkprojectman.v4.model.show_project_work_hours_response_body_work_hours import ShowProjectWorkHoursResponseBodyWorkHours
from huaweicloudsdkprojectman.v4.model.show_work_item_wrokflow_config_request import ShowWorkItemWrokflowConfigRequest
from huaweicloudsdkprojectman.v4.model.show_work_item_wrokflow_config_response import ShowWorkItemWrokflowConfigResponse
from huaweicloudsdkprojectman.v4.model.simple_project import SimpleProject
from huaweicloudsdkprojectman.v4.model.simple_user import SimpleUser
from huaweicloudsdkprojectman.v4.model.status_attribute import StatusAttribute
from huaweicloudsdkprojectman.v4.model.status_flow_direct_to_vo import StatusFlowDirectToVo
from huaweicloudsdkprojectman.v4.model.status_vo import StatusVo
from huaweicloudsdkprojectman.v4.model.update_child_user_nick_name_request_body import UpdateChildUserNickNameRequestBody
from huaweicloudsdkprojectman.v4.model.update_issue_v4_request import UpdateIssueV4Request
from huaweicloudsdkprojectman.v4.model.update_issue_v4_response import UpdateIssueV4Response
from huaweicloudsdkprojectman.v4.model.update_iteration_request_v4 import UpdateIterationRequestV4
from huaweicloudsdkprojectman.v4.model.update_iteration_v4_request import UpdateIterationV4Request
from huaweicloudsdkprojectman.v4.model.update_iteration_v4_response import UpdateIterationV4Response
from huaweicloudsdkprojectman.v4.model.update_membes_role_v4_request import UpdateMembesRoleV4Request
from huaweicloudsdkprojectman.v4.model.update_membes_role_v4_request_body import UpdateMembesRoleV4RequestBody
from huaweicloudsdkprojectman.v4.model.update_membes_role_v4_response import UpdateMembesRoleV4Response
from huaweicloudsdkprojectman.v4.model.update_nick_name_v4_request import UpdateNickNameV4Request
from huaweicloudsdkprojectman.v4.model.update_nick_name_v4_response import UpdateNickNameV4Response
from huaweicloudsdkprojectman.v4.model.update_project_domain_request import UpdateProjectDomainRequest
from huaweicloudsdkprojectman.v4.model.update_project_domain_response import UpdateProjectDomainResponse
from huaweicloudsdkprojectman.v4.model.update_project_module_request import UpdateProjectModuleRequest
from huaweicloudsdkprojectman.v4.model.update_project_module_request_body import UpdateProjectModuleRequestBody
from huaweicloudsdkprojectman.v4.model.update_project_module_response import UpdateProjectModuleResponse
from huaweicloudsdkprojectman.v4.model.update_project_request_v4 import UpdateProjectRequestV4
from huaweicloudsdkprojectman.v4.model.update_project_v4_request import UpdateProjectV4Request
from huaweicloudsdkprojectman.v4.model.update_project_v4_response import UpdateProjectV4Response
from huaweicloudsdkprojectman.v4.model.update_user_nick_name_request_v4 import UpdateUserNickNameRequestV4
from huaweicloudsdkprojectman.v4.model.upload_attachments_request import UploadAttachmentsRequest
from huaweicloudsdkprojectman.v4.model.upload_attachments_request_body import UploadAttachmentsRequestBody
from huaweicloudsdkprojectman.v4.model.upload_attachments_response import UploadAttachmentsResponse
from huaweicloudsdkprojectman.v4.model.upload_issue_img_request import UploadIssueImgRequest
from huaweicloudsdkprojectman.v4.model.upload_issue_img_request_body import UploadIssueImgRequestBody
from huaweicloudsdkprojectman.v4.model.upload_issue_img_response import UploadIssueImgResponse
from huaweicloudsdkprojectman.v4.model.user_request import UserRequest
from huaweicloudsdkprojectman.v4.model.user_status_statistic import UserStatusStatistic
from huaweicloudsdkprojectman.v4.model.work_item_status_flow_vo import WorkItemStatusFlowVo
from huaweicloudsdkprojectman.v4.model.workitem_custom_field import WorkitemCustomField
from huaweicloudsdkprojectman.v4.model.workitem_status import WorkitemStatus
from huaweicloudsdkprojectman.v4.model.workitem_status_records import WorkitemStatusRecords
from huaweicloudsdkprojectman.v4.model.workitem_status_status import WorkitemStatusStatus
from huaweicloudsdkprojectman.v4.model.workitem_user import WorkitemUser
from huaweicloudsdkprojectman.v4.model.workitems import Workitems
from huaweicloudsdkprojectman.v4.model.workitems_domain import WorkitemsDomain
from huaweicloudsdkprojectman.v4.model.workitems_iteration import WorkitemsIteration
from huaweicloudsdkprojectman.v4.model.workitems_module import WorkitemsModule
from huaweicloudsdkprojectman.v4.model.workitems_status import WorkitemsStatus
from huaweicloudsdkprojectman.v4.model.workitems_tags import WorkitemsTags

