
# File that contains all the JSON data for LimeBike

apm_dashboard = """{
  "dashboard": {
    "metadata": {
      "version": 1
    },
    "title": "APM Performance",
    "icon": "none",
    "visibility": "all",
    "editable": "editable_by_owner",
    "filter": {
      "event_types": [
        "Transaction"
      ],
      "attributes": [
        "appName"
      ]
    },
    "widgets": [
      {
        "visualization": "faceted_line_chart",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT count(*) FROM Transaction FACET name limit 3 SINCE 1 DAYS AGO TIMESERIES"
          }
        ],
        "presentation": {
          "title": "Busiest Transactions",
          "notes": "null"
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 1,
          "column": 1
        }
      },
      {
        "visualization": "billboard",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT average(duration) FROM Transaction  since 1 day ago"
          }
        ],
        "presentation": {
          "title": "Real Time APM Performance",
          "notes": "null",
          "threshold": {
            "red": 0.01,
            "yellow": 0.001
          }
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 1,
          "column": 2
        }
      },
      {
        "visualization": "facet_bar_chart",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT average(duration) FROM Transaction facet name limit 3 since 1 day ago"
          }
        ],
        "presentation": {
          "title": "Slowest Transactions",
          "notes": "null"
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 1,
          "column": 3
        }
      },
      {
        "visualization": "line_chart",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT average(duration) FROM Transaction TIMESERIES since 1 day ago"
          }
        ],
        "presentation": {
          "title": "APM Real Time Perf",
          "notes": "null"
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 2,
          "column": 1
        }
      },
      {
        "visualization": "histogram",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT histogram(duration, width: 0.02,  buckets: 30) FROM Transaction"
          }
        ],
        "presentation": {
          "title": "APM Histogram",
            "notes": "null"
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 2,
          "column": 2
        }
      },
      {
        "visualization": "heatmap",
        "account_id": rpm_account_id,
        "data": [
          {
            "nrql": "SELECT histogram(duration, width: 0.02,  buckets: 20) FROM Transaction facet name  limit 5"
          }
        ],
        "presentation": {
          "title": "Transaction Perf Heatmap",
          "notes": "null"
        },
        "layout": {
          "width": 1,
          "height": 1,
          "row": 2,
          "column": 3
        }
      }
    ]
  }
}"""
