from datetime import datetime

from flask import Blueprint, abort, render_template, request
from jinja2 import TemplateNotFound


def trace_page_creator(context: dict):
    trace_page = Blueprint("trace_page", __name__, template_folder="templates")

    @trace_page.route("/trace/<traceId>")
    def page(traceId):
        results = context.get("results")
        result = None
        for r in results:
            if r.get("test_run_id") == traceId:
                result = r
                break

        if result is None:
            abort(404)

        result = {
            "Id": 0,
            "Trace": result.get("test_run_id"),
            "Input": result.get("prompt", result.get("input")),
            "Output": result.get("response"),
            "context": result.get("context"),
            "test_name": result.get("test_name"),
            "score": result.get("score"),
            "Complexity Test": result.get(""),
            "Context Precision": result.get(""),
            "Context Recall": result.get(""),
            "Toxicity": result.get(""),
            "Bias": result.get(""),
            "Start Time": datetime.utcnow(),
            "End Time": datetime.utcnow(),
            "Child Span": 0,
            "Status": "Success" if result.get("is_passed") else "Failed",
        }
        try:
            return render_template("trace.html", result=result)
        except TemplateNotFound:
            abort(404)

    return trace_page
