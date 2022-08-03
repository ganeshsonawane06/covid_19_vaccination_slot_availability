# Metadata APIs
COWIN_VACCINE_STATES = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
COWIN_VACCINE_DISTRICT = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}"

# Appointment Availability APIs
COWIN_VACCINE_SLOT_BY_PIN = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?"
COWIN_VACCINE_SLOT_BY_DISTRICT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?"
COWIN_VACCINE_SLOT_BY_CALENDER_PIN = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
COWIN_VACCINE_SLOT_BY_CALENDER_DISTRICT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public" \
                                          "/calendarByDistrict?"
COWIN_VACCINE_SLOT_BY_CALENDER_CENTER_ID = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?"