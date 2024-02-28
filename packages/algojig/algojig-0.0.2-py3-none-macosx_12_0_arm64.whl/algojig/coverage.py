import sys
import glob
import json
import os
import hashlib


coverage = {}


# def update_coverage(program):
#     hash = hashlib.sha256(program.bytecode).hexdigest()
#     for filename in glob.glob(f"/tmp/jig/debug_{hash}_*.json"):
#         with open(filename) as f:
#             debug = json.load(f)
#             update_coverage_from_trace(program, debug)
#             if hasattr(program, "teal_program"):
#                 update_coverage_from_trace(program.teal_program, debug)
#         # os.remove(filename)


def update_coverage_from_trace(program, trace):
    if program not in coverage:
        coverage[program] = {}
    for d in trace:
        pc = d["pc"]
        line_no = program.lookup(pc)["line_no"]
        coverage[program][line_no] = True
    if hasattr(program, "teal_program"):
        update_coverage_from_trace(program.teal_program, trace)


def report_coverage(program):
    result = {
        "coverage": coverage[program],
        "source": program.source_lines,
    }
    filename = (program.filename + ".coverage.json").split("/")[-1]
    with open(filename, "w") as f:
        json.dump(result, f)
    output_coverage(filename)


def output_coverage(filename):
    result = json.load(open(filename))
    html = """
    <html>
    <head>
    <style>
    .covered {
        background-color: #EFE;
    }
    .not_covered {
        background-color: #FEE;
    }
    </style>
    </head>
    <body>
    <pre>
    """
    offset = 0 if '.teal' in filename else 1
    skipping = False
    for i, line in enumerate(result["source"]):
        css_class = ""
        ignore_keywords = ("//", "#", "@", "end", "block", "const", "func", "else", "struct")
        skip = skipping or line.strip().startswith(ignore_keywords)
        if not line.strip() or line.strip().startswith(("int", "byte")) and "=" not in line:
            skip = True
        # if line.split('//')[0].strip().endswith(":"):
        #     skip = True
        if not skip:
            css_class = (
                "covered" if result["coverage"].get(str(i + offset)) else "not_covered"
            )
        html += f'{str(i).ljust(4)} <span class="{css_class}">{line}</span>\n'
        if skipping and line.strip().startswith(("end",)):
            skipping = False
        if line.strip().startswith(("switch", "inner_txn", "router", "struct")):
            skipping = True

    html += """
    </pre>
    </body>
    </html>
    """
    with open(filename.replace(".coverage.json", ".coverage.html"), "w") as f:
        f.write(html)


if __name__ == "__main__":
    output_coverage(sys.argv[1])
