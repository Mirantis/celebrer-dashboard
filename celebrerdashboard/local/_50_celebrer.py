# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'celebrer'

# If set to True, this dashboard will not be added to the settings.
DISABLED = False

ADD_INSTALLED_APPS = [
    'celebrerdashboard',
    # 'openstack_dashboard.dashboards.celebrerdashboard',
]

ADD_JS_FILES = [
    'celebrerdashboard/js/murano.service.js',
    'celebrerdashboard/js/upload_form.js',
    'celebrerdashboard/js/import_bundle_form.js',
]

