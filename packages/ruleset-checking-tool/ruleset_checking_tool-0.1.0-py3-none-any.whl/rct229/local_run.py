import json

import jsonschema
import pandas as pd

from rct229.reports.ashrae901_2019_detail_report import ASHRAE9012019DetailReport
from rct229.reports.ashrae901_2019_summary_report import ASHRAE9012019SummaryReport
from rct229.rule_engine.engine import evaluate_all_rules, evaluate_all_rules_rpd
from rct229.rule_engine.rulesets import RuleSet

# from rct229.rule_engine.utils import _load_json
from rct229.ruletest_engine.run_ruletests import (
    run_ashrae9012019_tests,
)  # generate_ashrae9012019_software_test_report

# from rct229.schema.schema_store import SchemaStore
# from rct229.schema.schema_enums import SchemaEnums
from rct229.schema.schema_enums import SchemaEnums
from rct229.schema.schema_store import SchemaStore


def run_test_helper(output_dir):
    run_ashrae9012019_tests()
    print("Calculation completed")


def run_local(user_path, baseline_path, proposed_path, rulesetdoc):

    if rulesetdoc == RuleSet.ASHRAE9012019_RULESET:
        SchemaStore.set_ruleset(RuleSet.ASHRAE9012019_RULESET)
        SchemaEnums.update_schema_enum()

    # report = evaluate_all_rules([user_rmr_obj, baseline_rmr_obj, proposed_rmr_obj])
    report = evaluate_all_rules([user_path, baseline_path, proposed_path])
    # report_module = ASHRAE9012019DetailReport()
    # report_module.generate(
    #     report,
    #     "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\output",
    # )
    report_module = ASHRAE9012019SummaryReport()
    report_module.generate(
        report,
        "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\output",
    )
    print("Calculation completed")


# run_local(
#     "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\chicago_demo\\user_model.json",
#     "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\chicago_demo\\baseline_model.json",
#     "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\chicago_demo\\proposed_model.json",
#     "ashrae9012019",
# )


def run_local_json(user, baseline, proposed, saving_dir, rulesetdoc="ashrae9012019"):
    if rulesetdoc == RuleSet.ASHRAE9012019_RULESET:
        SchemaStore.set_ruleset(RuleSet.ASHRAE9012019_RULESET)
        SchemaEnums.update_schema_enum()

    report = evaluate_all_rules_rpd([user, baseline, proposed])
    print("Calculation completed")
    report_module = ASHRAE9012019DetailReport()
    report_module.generate(
        report,
        "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\output",
    )

    return report


user_path = "C:\\Users\\xuwe123\\OneDrive - PNNL\\Documents\\Projects\\RCT-229\\OSSTD_Demo\\medium_office_proposed.json"
baseline_path = "C:\\Users\\xuwe123\\OneDrive - PNNL\\Documents\\Projects\\RCT-229\\OSSTD_Demo\\medium_office_baseline.json"
proposed_path = "C:\\Users\\xuwe123\\OneDrive - PNNL\\Documents\\Projects\\RCT-229\\OSSTD_Demo\\medium_office_proposed.json"

# run_local(user_path, baseline_path, proposed_path, "ashrae9012019")

output_doc = "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\output\\ashrae901_2019_detail_report.json"


def validate_schema():
    with open(
        "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\rct229\\schema\\RCT_project_output_test_report.schema.json"
    ) as json_file:
        output_report_schema = json.load(json_file)

    with open(
        "C:\\Users\\xuwe123\\Documents\\GitHub\\ruleset-checking-tool\\examples\\output\\ashrae901_2019_detail_report.json"
    ) as json_file:
        report = json.load(json_file)
    # Create a resolver which maps schema references to schema objects
    schema_store = {
        "RCT_project_output_test_report.schema.json": output_report_schema,
    }
    resolver = jsonschema.RefResolver.from_schema(
        output_report_schema, store=schema_store
    )
    # Create a validator
    Validator = jsonschema.validators.validator_for(output_report_schema)
    validator = Validator(output_report_schema, resolver=resolver)
    try:
        # Throws ValidationError on failure
        validator.validate(report)
        return {"passed": True, "error": None}
    except jsonschema.exceptions.ValidationError as err:
        return {"passed": False, "error": "schema invalid: " + err.message}


# validate_schema()
