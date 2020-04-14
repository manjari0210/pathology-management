from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Pathology"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Patient",
              "label": _("Patient"),
              "description": _("Patient coming for tests."),
            },
            {
              "type": "doctype",
              "name": "Patient Sample",
              "label": _("Patient Sample"),
              "description": _("Patient with sample given to test."),
            },
            {
              "type": "doctype",
              "name": "Patient Report",
              "label": _("Patient Report"),
              "description": _("Patient report coming from sample given for test."),
            },
            {
              "type": "doctype",
              "name": "Doctor",
              "label": _(""),
              "description": _("Assigning a doctor for checkup."),
            }
          ]
      }
  ]
