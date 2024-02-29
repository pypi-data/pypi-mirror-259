import json
import math

from flask import Blueprint, abort, render_template, request
from helpers import pick_matching_keys_from_dict
from jinja2 import TemplateNotFound


def index_page_creator(context: dict):
    index_page = Blueprint("index_page", __name__, template_folder="templates")

    @index_page.route("/")
    def page():
        results = context.get("results")

        # region pagination related code
        page = request.args.get("page", 0, int)
        size = request.args.get("size", len(results), int)
        offset = page * size
        total_pages = 0 if len(results) == 0 else math.ceil(len(results) / size)
        target_results = results[offset : offset + size]
        # endregion

        # region grid data related code
        rows = [
            [
                "Id",
                "Trace",
                "Input",
                "Output",
                "Complexity Test",
                "Context Precision",
                "Context Recall",
                "Toxicity",
                "Bias",
            ],
        ]
        for index, result in enumerate(target_results):
            id = index + 1
            id = f"0{id}" if id < 10 else id
            rows.append(
                {
                    "Id": id,
                    "Trace": result.get("test_run_id"),
                    "Input": result.get("prompt", result.get("input")),
                    "Output": result.get("response"),
                    "Complexity Test": result.get(""),
                    "Context Precision": result.get(""),
                    "Context Recall": result.get(""),
                    "Toxicity": result.get(""),
                    "Bias": result.get(""),
                }
            )
        groups = group_by_test_name(target_results)
        # endregion
        try:
            return render_template(
                "index.html",
                rows=rows,
                target_results=json.dumps(
                    [get_table_data_for_test(t) for t in target_results]
                ),
                total_elements=len(target_results),
                total_pages=total_pages,
                current_page=page,
                uniq_tests=groups,
                count_of_key=count_of_key_creator("is_passed"),
                max=max,
                min=min,
            )
        except TemplateNotFound:
            abort(404)

    return index_page


def group_by_test_name(results: list):
    groups = {}
    for result in results:
        test_name = result.get("test_name")
        if test_name not in groups:
            groups[test_name] = []
        groups[test_name].append(result)
    return groups


def get_table_data_for_test(test: dict):
    score = test.get("score")
    result = {
        "Trace": test.get("test_run_id"),
        "Input": test.get("prompt", test.get("input")),
        "Output": test.get("response"),
        "test": {
            **pick_matching_keys_from_dict(test, ["test_name", "is_passed"]),
            "score": (
                score.get("response_readability_score")
                if isinstance(score, dict)
                else score
            ),
        },
    }
    return result


def count_of_key_creator(key: str):
    def count_of_key(arr: list, value):
        count = 0
        for a in arr:
            if a.get(key) == value:
                count += 1
        return count

    return count_of_key
