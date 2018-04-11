import json

with open("variants.json") as variants_file:
    variants = json.load(variants_file)

with open("output/performance.json") as performance_log_file:
    performance_log = json.load(performance_log_file)

for (name, variant) in variants.items():
    max_time = variant["max_allowed_render_time"]
    actual_time = performance_log[name]
    assert actual_time <= max_time, (
        "%s rendered in %s seconds which exceeds the max allowed time of %s" % (name, actual_time, max_time)
    )

print("Performance OK.")