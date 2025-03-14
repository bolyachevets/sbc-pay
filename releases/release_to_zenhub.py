from dotenv import load_dotenv
from util import add_issues_to_release, create_release, get_issue_id, get_issues_from_repo, get_workspace_release_for_report

load_dotenv()

auth_issue_ids, _, _ = get_issues_from_repo('sbc-auth')
pay_issue_ids, release_names, release_dates = get_issues_from_repo('sbc-pay', latest_release_only=True)
pay_release_issue_ids = list(set([item for item in pay_issue_ids if item not in auth_issue_ids]))
target_release_name = f'Pay Release - {release_names[0]}'
release_id = get_workspace_release_for_report(target_release_name)
if release_id is None:
    release_id = create_release(target_release_name, release_dates[0])
    print(f'Zenhub release created id: {release_id} - {target_release_name}')
else:
    print(f'Zenhub release found id: {release_id} - {target_release_name}')
for issue in pay_release_issue_ids:
    issue_id = get_issue_id(issue)
    add_issues_to_release(issue_id, release_id)
    print(f'Adding issue {issue} - {issue_id} to Zenhub release {release_id}')
